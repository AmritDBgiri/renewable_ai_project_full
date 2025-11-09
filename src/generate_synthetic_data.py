import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from .config import NUM_ZONES, YEARS, HOURS_PER_YEAR, ZONE_CAPACITY_MW, SEED


def generate_synthetic_dataset(save_path: str):
    np.random.seed(SEED)

    start = datetime(2019, 1, 1)
    hours = YEARS * HOURS_PER_YEAR
    timestamps = [start + timedelta(hours=h) for h in range(hours)]

    rows = []
    for ts in timestamps:
        hour = ts.hour
        doy = ts.timetuple().tm_yday
        weekday = ts.weekday()

        # base price pattern (INR/MWh)
        base_price = 2500 + 500 * np.sin(2 * np.pi * hour / 24)
        base_price += 300 * np.sin(2 * np.pi * doy / 365)
        base_price *= np.random.uniform(0.8, 1.2)

        for z in range(NUM_ZONES):
            # simple solar pattern
            solar = max(0, np.sin(2 * np.pi * (hour - 6) / 24))
            solar *= 1 + 0.3 * np.sin(2 * np.pi * doy / 365)
            solar += 0.1 * np.random.randn()

            # simple wind pattern
            wind = 0.6 + 0.2 * np.sin(2 * np.pi * doy / 365 + z)
            wind += 0.2 * np.random.randn()
            wind = max(0, wind)

            # demand pattern
            demand = 600 + 200 * np.sin(2 * np.pi * (hour - 18) / 24)
            demand += 150 * np.sin(2 * np.pi * doy / 365)
            if weekday >= 5:  # weekend slightly lower
                demand *= 0.9
            demand += np.random.normal(0, 80)
            demand = max(50, demand)

            # generation from capacity
            gen = ((solar + wind) / 2.0) * ZONE_CAPACITY_MW[z]
            gen += np.random.normal(0, 50)
            gen = max(0, gen)

            price = base_price * np.random.uniform(0.95, 1.05)

            rows.append({
                "timestamp": ts,
                "zone": z,
                "solar": solar,
                "wind": wind,
                "demand": demand,
                "gen": gen,
                "price": price,
                "hour": hour,
                "doy": doy,
                "weekday": weekday,
            })

    df = pd.DataFrame(rows)
    df.to_csv(save_path, index=False)
    print("✅ Saved synthetic data to", save_path)


if __name__ == "__main__":
    from pathlib import Path

    out_path = Path(__file__).resolve().parents[1] / "data" / "synthetic" / "renewable_data.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    generate_synthetic_dataset(str(out_path))
