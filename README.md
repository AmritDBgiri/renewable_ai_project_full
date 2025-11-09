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
