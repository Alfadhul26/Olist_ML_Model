
from datetime import datetime, timedelta
import pandas as pd
import joblib

cat_cols = ["customer_state", "seller_state", "main_product_category"]

num_cols = [
    'customer_zip_code_prefix', 'n_items', 'n_unique_products', 'n_sellers',
    'total_price', 'total_freight', 'total_weight_g', 'max_item_weight_g',
    'total_volume_cm3', 'avg_photos_qty', 'avg_description_length',
    'freight_ratio', 'seller_zip_code_prefix', 'purchase_month',
    'purchase_dayofweek', 'purchase_hour', 'is_weekend',
    'same_state', 'same_city'
]

feature_cols = num_cols + cat_cols


def typical_values(rows):
    by_category = rows.groupby("main_product_category")
    return {
        "product": by_category[
            ["total_price", "total_weight_g", "max_item_weight_g",
             "total_volume_cm3", "avg_photos_qty", "avg_description_length"]
        ].median(),
        "seller": by_category[
            ["seller_state", "seller_zip_code_prefix"]
        ].agg(lambda s: s.mode()[0]),
        "state": rows.groupby("customer_state")[
            ["customer_zip_code_prefix", "total_freight"]
        ].median(),
    }


def make_row(t, category, state, month, dayofweek, hour):
    product = t["product"].loc[category].to_dict()
    seller = t["seller"].loc[category].to_dict()
    place = t["state"].loc[state].to_dict()

    return {
        **product,
        **seller,
        **place,
        "n_items": 1,
        "n_unique_products": 1,
        "n_sellers": 1,
        "freight_ratio": place["total_freight"] / product["total_price"],
        "purchase_month": month,
        "purchase_dayofweek": dayofweek,
        "purchase_hour": hour,
        "is_weekend": int(dayofweek >= 5),
        "same_state": int(state == seller["seller_state"]),
        "same_city": 0,
        "customer_state": state,
        "main_product_category": category
    }


def now_brazil():
    try:
        from zoneinfo import ZoneInfo
        return datetime.now(
            ZoneInfo("America/Sao_Paulo")
        ).replace(tzinfo=None)
    except Exception:
        return datetime.now()


def predict_delivery(category, state, bundle, when=None):
    t = bundle["typical"]

    if category not in t["product"].index or state not in t["state"].index:
        raise ValueError("Unknown category or state")

    when = when or now_brazil()

    row = pd.DataFrame([
        make_row(
            t, category, state,
            when.month, when.weekday(), when.hour
        )
    ])[feature_cols]

    days = max(float(bundle["model"].predict(row)[0]), 1.0)

    return {
        "days": round(days, 1),
        "date": (when + timedelta(days=round(days))).date(),
        "typical_error_days": round(bundle["typical_error_days"], 1)
    }
