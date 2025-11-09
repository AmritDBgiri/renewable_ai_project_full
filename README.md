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
│   ├─ synthetic/
│   │   └─ renewable_data.csv              # Generated 5-year dataset (solar, wind, demand)
│   └─ raw/                                # Placeholder for real data (optional)
│
├─ notebooks/
│   ├─ EDA_and_model_check.ipynb           # Main notebook (EDA, forecasting, optimization results)
│   └─ .ipynb_checkpoints/                 # Auto-saved notebook states
│
├─ src/
│   ├─ __init__.py                         # Marks this as a Python package
│   ├─ config.py                           # Constants and configuration (zones, capacity, etc.)
│   ├─ generate_synthetic_data.py          # Creates synthetic dataset
│   ├─ data_loader.py                      # Handles loading and preprocessing
│   ├─ features.py                         # Adds lag features and time splits
│   ├─ models_forecasting.py               # Builds ML forecasting models
│   ├─ optimizer.py                        # Linear optimization (dispatch, storage, bidding)
│   ├─ metrics.py                          # Performance metrics (reliability, losses, EBITDA)
│   ├─ bidding.py                          # Optional dynamic bidding simulation
│   └─ simulate_pipeline.py                # End-to-end forecasting + optimization simulation
│
├─ .gitignore                              # Ignores .venv, __pycache__, etc.
├─ README.md                               # Project overview and run instructions
├─ requirements.txt                        # (recommended) Python package list
└─ LICENSE                                 # (optional) Open-source license




---

## 🧠 How to Run

### 1️⃣ Create and activate virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate


2️⃣ Install dependencies
pip install pandas numpy scikit-learn pulp tqdm matplotlib

3️⃣ Generate data
python -m src.generate_synthetic_data

4️⃣ Run forecasting + optimization
python -m src.simulate_pipeline

5️⃣ View report

Open the Jupyter Notebook:

jupyter notebook notebooks/EDA_and_model_check.ipynb

📊 Results (Sample)
Metric	Value
Reliability	78.8%
Loss Ratio	0.00%
EBITDA Margin	60.27%
🚀 Next Steps

Integrate real IMD weather & IEX price data

Replace regression models with LSTMs

Deploy dashboard with Streamlit or FastAPI

👨‍💻 Author

Amrit Kumar Giri
B.Tech, IIIT Bhagalpur
📧 amritgiri@example.com

🌐 github.com/AmritDBgiri
