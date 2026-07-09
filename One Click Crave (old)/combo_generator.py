import random
import json
import pandas as pd
from datetime import datetime
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# Load the complete menu data
def load_menu():
    with open("menu_data.json", "r") as f:
        return json.load(f)

# Load dietary preferences (veg, no onion/garlic, spice)
def load_prefs():
    with open("user_prefs.json", "r") as f:
        return json.load(f)

# Suggest a meal combo using rules
def suggest_rule_based_combo(restaurant, prefs):
    menu = load_menu()[restaurant]
    combo = []

    for category, items in menu.items():
        if isinstance(items, list):
            filtered = []

            for item in items:
                text = item.lower()
                if prefs["veg_only"] and any(meat in text for meat in ["chicken", "fish", "egg", "mutton", "bacon"]):
                    continue
                if prefs["no_onion"] and "onion" in text:
                    continue
                if prefs["no_garlic"] and "garlic" in text:
                    continue
                if prefs["low_spice"] and "spicy" in text:
                    continue
                filtered.append(item)

            # Fallback to full list if all filtered out
            if not filtered:
                filtered = items

            choice = random.choice(filtered)
            combo.append(choice)

    return combo

# Log the chosen combo to order history
def log_order(mode, restaurant, combo):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_row = {"datetime": now, "mode": mode, "restaurant": restaurant, "items": "; ".join(combo)}

    try:
        df = pd.read_csv("order_history.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["datetime", "mode", "restaurant", "items"])

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv("order_history.csv", index=False)

# Use a simple ML model to predict your preferred combo
def predict_combo_with_ml(restaurant, mode):
    try:
        # Try ML first
        df = pd.read_csv("order_history.csv")
        if df.empty or len(df) < 5:
            raise ValueError("Not enough data for ML")

        df["feature"] = df["restaurant"] + "_" + df["mode"]
        le = LabelEncoder()
        X = le.fit_transform(df["feature"]).reshape(-1, 1)
        y = df["items"]

        model = LogisticRegression(max_iter=1000)
        model.fit(X, y)

        test_feat = le.transform([f"{restaurant}_{mode}"]).reshape(-1, 1)
        prediction = model.predict(test_feat)[0]
        return prediction.split("; ")

    except Exception:
        # Fallback to manual favorite combos
        try:
            with open("fav_combos.json", "r") as f:
                favs = json.load(f)
            return favs.get(restaurant, None)
        except Exception as e:
            print("Failed to load fallback combos:", e)
            return None

