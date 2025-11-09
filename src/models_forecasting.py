import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

GEN_FEATURES = ["solar", "wind", "hour", "doy", "weekday"]
DEMAND_FEATURES = ["solar", "wind", "hour", "doy", "weekday"]
PRICE_FEATURES = ["hour", "doy", "weekday", "demand", "gen"]


class ForecastModels:
    def __init__(self):
        self.gen_model = RandomForestRegressor(n_estimators=100, random_state=0)
        self.dem_model = RandomForestRegressor(n_estimators=100, random_state=0)
        self.price_model = RandomForestRegressor(n_estimators=100, random_state=0)

    def fit(self, train_df: pd.DataFrame):
        # Generation model
        self.gen_model.fit(train_df[GEN_FEATURES], train_df["gen"])

        # Demand model
        self.dem_model.fit(train_df[DEMAND_FEATURES], train_df["demand"])

        # Price model on aggregated data (one row per timestamp)
        price_df = train_df.groupby("timestamp").agg({
            "hour": "first",
            "doy": "first",
            "weekday": "first",
            "demand": "sum",
            "gen": "sum",
            "price": "mean",
        }).reset_index()

        self.price_model.fit(price_df[PRICE_FEATURES], price_df["price"])

    def evaluate(self, test_df: pd.DataFrame):
        gen_pred = self.gen_model.predict(test_df[GEN_FEATURES])
        dem_pred = self.dem_model.predict(test_df[DEMAND_FEATURES])
        print("Gen MAE:", mean_absolute_error(test_df["gen"], gen_pred))
        print("Demand MAE:", mean_absolute_error(test_df["demand"], dem_pred))

    def forecast_hour(self, hour_df: pd.DataFrame):
        """
        hour_df: one row per zone for a single timestamp
        """
        gen_hat = self.gen_model.predict(hour_df[GEN_FEATURES])
        dem_hat = self.dem_model.predict(hour_df[DEMAND_FEATURES])

        agg = hour_df.iloc[0:1].copy()
        agg["demand"] = hour_df["demand"].sum()
        agg["gen"] = hour_df["gen"].sum()
        price_hat = float(self.price_model.predict(agg[PRICE_FEATURES])[0])

        return gen_hat, dem_hat, price_hat
