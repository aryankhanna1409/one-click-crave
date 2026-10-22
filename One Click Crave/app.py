import streamlit as st
import json
from combo_generator import (
    suggest_rule_based_combo,
    predict_combo_with_ml,
    log_order,
)
from swiggy_linker import make_links

# Load menu and preferences
with open("menu_data.json", "r") as f:
    menu = json.load(f)

with open("user_prefs.json", "r") as f:
    prefs = json.load(f)

# --- Streamlit UI ---
st.set_page_config(page_title="MealMuse 🍽️", layout="centered")
st.title("🍱 What Should I Eat Today?")

mode = st.radio("How are you eating?", ["Dine In", "Order Online"])
restaurant = st.selectbox("Pick a place", list(menu.keys()))
choice = st.radio("What do you feel like?", ["My Usual", "Surprise Me!"])

# Show dietary preferences
with st.expander("Dietary Preferences"):
    prefs["veg_only"] = st.checkbox("Vegetarian Only", value=prefs["veg_only"])
    prefs["no_onion"] = st.checkbox("No Onion", value=prefs["no_onion"])
    prefs["no_garlic"] = st.checkbox("No Garlic", value=prefs["no_garlic"])
    prefs["low_spice"] = st.checkbox("Low Spice", value=prefs["low_spice"])

# --- Generate Combo ---
if st.button("🎲 Generate Combo"):
    if choice == "Surprise Me!":
        combo = suggest_rule_based_combo(restaurant, prefs)
    else:
        combo = predict_combo_with_ml(restaurant, mode.lower()) or suggest_rule_based_combo(restaurant, prefs)

    # Keep the combo in session state so it survives the rerun triggered by the Confirm button
    st.session_state["combo"] = combo
    st.session_state["combo_ctx"] = (mode, restaurant)
    st.session_state["saved"] = False

combo = st.session_state.get("combo")
if combo:
    combo_mode, combo_restaurant = st.session_state["combo_ctx"]

    st.success("Here's your combo:")
    for item in combo:
        st.write(f"🍴 {item}")

    if combo_mode == "Order Online":
        st.markdown("**Quick Search Links:**")
        for item in combo:
            st.markdown(make_links(combo_restaurant, item), unsafe_allow_html=True)

    # --- Confirm Button ---
    if st.button("✅ Confirm this meal"):
        log_order(combo_mode.lower(), combo_restaurant, combo)
        st.session_state["saved"] = True

    if st.session_state.get("saved"):
        st.success("Saved to history. I’ll remember this for next time!")

