# 🌞 Renewable AI Project — Smart Energy Optimization

This project develops an **AI-powered renewable energy management system** that optimizes solar and wind energy dispatch, storage, and bidding using ML-based forecasting and mathematical optimization.

---

## 📋 Objectives
- Improve grid **reliability** by 15%
- Reduce **energy losses** by 20%
- Maintain **profitability (EBITDA > 15%)** despite fluctuating market prices

---

## ⚙️ Features
- Synthetic data generation (5 years of hourly data)
- ML-based forecasting of demand and generation
- Storage optimization and dispatch scheduling
- Dynamic bidding simulation
- Full pipeline automation with metrics reporting

---

## 🧩 Project Structure
renewable_ai_project_full/
│
├─ data/
│ ├─ synthetic/ → generated datasets
│ └─ raw/ → real data (if available)
│
├─ notebooks/
│ └─ EDA_and_model_check.ipynb → main analysis & report
│
├─ src/
│ ├─ generate_synthetic_data.py
│ ├─ models_forecasting.py
│ ├─ optimizer.py
│ ├─ simulate_pipeline.py
│ ├─ metrics.py
│ ├─ bidding.py
│ └─ config.py
│
└─ README.md
