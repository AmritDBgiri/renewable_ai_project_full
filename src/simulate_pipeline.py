import numpy as np
import pandas as pd
from tqdm import tqdm

from .data_loader import load_data
from .features import add_lag_features, train_test_split_time
from .models_forecasting import ForecastModels
from .optimizer import optimize_one_hour
from .metrics import reliability, losses, ebitda_margin


def run_pipeline(csv_path: str, test_year: int = 2023):
    # 1. Load + feature engineering
    df_raw = load_data(csv_path)
    df_feat = add_lag_features(df_raw)

    train_df, test_df = train_test_split_time(df_feat, split_year=test_year)

    # 2. Train models
    models = ForecastModels()
    models.fit(train_df)
    models.evaluate(test_df)

    # Use only the test year for simulation
    test_df = test_df[test_df["timestamp"].dt.year == test_year].copy()
    timestamps = sorted(test_df["timestamp"].unique())

    all_dem, all_short, all_gen, all_disp = [], [], [], []
    total_revenue = 0.0
    total_cost = 0.0

    for ts in tqdm(timestamps, desc="Simulating"):
        hour_df = test_df[test_df["timestamp"] == ts].copy()

        gen_hat, dem_hat, price_hat = models.forecast_hour(hour_df)

        p, u = optimize_one_hour(gen_hat, dem_hat, price_hat)

        gen_hat = np.array(gen_hat)
        dem_hat = np.array(dem_hat)
        p = np.array(p)
        u = np.array(u)

        revenue_h = price_hat * p.sum()
        cost_gen_h = 1000 * p.sum()  # simple cost
        total_revenue += revenue_h
        total_cost += cost_gen_h

        all_dem.append(dem_hat)
        all_short.append(u)
        all_gen.append(gen_hat)
        all_disp.append(p)

    demand_arr = np.stack(all_dem)
    short_arr = np.stack(all_short)
    gen_arr = np.stack(all_gen)
    disp_arr = np.stack(all_disp)

    rel = reliability(demand_arr, short_arr)
    loss_ratio = losses(gen_arr, disp_arr)
    margin = ebitda_margin(total_revenue, total_cost)

    print("\n=== RESULTS ===")
    print(f"Reliability: {rel * 100:.2f}%")
    print(f"Loss ratio: {loss_ratio * 100:.2f}%")
    print(f"EBITDA margin (approx): {margin * 100:.2f}%")

    return {
        "reliability": rel,
        "loss_ratio": loss_ratio,
        "ebitda_margin": margin,
        "total_revenue": total_revenue,
        "total_cost": total_cost,
    }


if __name__ == "__main__":
    from pathlib import Path

    csv_path = Path(__file__).resolve().parents[1] / "data" / "synthetic" / "renewable_data.csv"
    results = run_pipeline(str(csv_path))
    print(results)
