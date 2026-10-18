# Olist Delivery Time Prediction

- Predicts how many days an order will take to arrive, using only what is known when the customer chooses a product. Built on the public [Olist Brazilian e-commerce dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (96,470 delivered orders, 2016–2018).
- Deployed Model: https://olitsml.streamlit.app

## Problem
Olist shows customers an estimated delivery of **23.7 days**, while orders actually arrive in **12.6 days** on average. A model that predicts delivery time gives customers a shorter, more accurate date.

## Results
| | Average error (test set) |
|---|---|
| Olist's current estimate | 12.7 days |
| Linear Regression (baseline) | 5.25 days |
| Gradient Boosting (final model) | **4.71 days** |

## Project structure
```
data/            olist_delivery_model_dataset.csv
notebooks/       EDA.ipynb, Modelling.ipynb
deployment/      Delivery_Model_Deployment.ipynb, app.py, delivery_model.pkl
presentation/    Slide deck: problem statement, business case and technical summary
```
| File | Purpose |
|---|---|
| `notebooks/EDA.ipynb` | Cleaning, EDA, and building the one-row-per-order modelling dataset |
| `notebooks/Modelling.ipynb` | Model comparison, tuning and error analysis |
| `deployment/Model_for_Deployment.ipynb` | Trains the final model and saves it |
| `deployment/app.py` | Streamlit app: pick a product category and a state, get an estimated delivery date |

## Method
- **Data:** orders, items, products, sellers, customers and payments joined into one row per order.
- **Missing values:** filled with the median (numbers) or most common value (categories); no orders are dropped.
- **Split:** 64% train, 16% validation, 20% test, `random_state=42`.
- **Metric:** Mean Absolute Error (MAE), the average number of days the prediction is off.
- **Deployment:** the customer enters a category and a state; other inputs are filled with typical values for that category and state.

## Limitations
- Very slow orders (20+ days) are under-predicted.
- About 36% of orders arrive after the predicted date, so a safety margin (for example +6 to +8 days) is recommended.
- Data is from 2016–2018; retrain on recent orders before real use.