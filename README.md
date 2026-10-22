<div align="center">

# 🍱 One Click Crave

**"What should I eat today?" answered in one click, tuned to your dietary rules and your order history.**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-app-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-logistic%20regression-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)

</div>

---

## ✨ Features

| | |
|---|---|
| 🍽️ **Dine in or order online** | Pick how you're eating and which restaurant |
| 🎲 **Surprise me** | A random combo built from the menu, one item per category |
| 🔁 **My usual** | A logistic-regression model trained on your logged orders predicts your usual; falls back to a rule-based combo if there isn't enough history |
| 🥦 **Dietary filters** | Vegetarian only, no onion, no garlic, low spice |
| 🔗 **Quick search links** | For online orders, a one-click search for each item on Swiggy |
| ✅ **Learns from you** | Confirm a meal and it's saved to `order_history.csv` for next time |

Built-in menus: McDonald's, Taco Bell, Starbucks, Domino's, Kimling, Third Wave Coffee, Kiosk Kaffee and Demitasse.

---

## 🚀 Quick start

```bash
git clone https://github.com/aryankhanna1409/one-click-crave.git
cd "one-click-crave/One Click Crave"

pip install -r requirements.txt
streamlit run app.py
```

---

## 📁 Project layout

| File | Role |
|---|---|
| `app.py` | Streamlit interface (shown in the browser as **MealMuse**) |
| `combo_generator.py` | Rule-based combos, the ML prediction and order logging |
| `swiggy_linker.py` | Builds the search links for online ordering |
| `menu_data.json` | Restaurants and their menus by category |
| `user_prefs.json` | Your dietary preferences |
| `order_history.csv` | Past orders used to train the "usual" model |

`One Click Crave (old)/` keeps the earlier version of the app for reference.

---

<div align="center">

Because choosing is the hardest part of dinner

</div>
