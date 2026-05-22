# 📦 Vendor Invoice Intelligence Portal

An AI-powered internal analytics portal that leverages machine learning to predict freight costs and flag invoices for manual approval — reducing financial leakage and streamlining finance operations.

---

## 🚀 Features

- **Freight Cost Prediction** — Predicts freight cost for vendor invoices using invoice dollar value
- **Invoice Risk Flagging** — Classifies invoices as safe for auto-approval or requiring manual review
- **Interactive UI** — Built with Streamlit for easy use by non-technical finance teams

---

## 🧠 ML Models

| Model | Algorithm | Purpose |
|-------|-----------|---------|
| `predict_freight_model.pkl` | Linear Regression | Predict freight cost from invoice dollars |
| `predict_flag_invoice.pkl` | Random Forest Classifier | Flag invoices for manual approval |

### Model Performance (Invoice Flag Classifier)
```
Accuracy: 89%

              precision    recall  f1-score
           0       0.87      0.98      0.92
           1       0.96      0.71      0.82
    accuracy                           0.89
```

---

## 📁 Project Structure

```
invoice flagging/
│
├── app.py                      # Streamlit frontend application
├── predict_freight.py          # Freight cost prediction module
├── predict_invoice_flag.py     # Invoice flag prediction module
├── data_preprocessing.py       # Data loading & feature engineering
├── modeling_evalution1.py      # Model training & evaluation
├── train1.py                   # Training pipeline entry point
├── invoice_flagging.ipynb      # EDA & experimentation notebook
│
├── models/
│   ├── predict_freight_model.pkl
│   ├── predict_flag_invoice.pkl
│   └── scaler.pkl
│
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/invoice-intelligence.git
cd invoice-intelligence
```

### 2. Install Dependencies
```bash
pip install streamlit pandas numpy scikit-learn joblib
```

### 3. Train the Models
Make sure your `inventory.db` database is available, then run:
```bash
python train1.py
```
This will generate the `.pkl` model files inside the `models/` folder.

### 4. Run the App
```bash
python -m streamlit run app.py
```

---

## 📊 Input Features

### Freight Cost Prediction
| Feature | Description |
|---------|-------------|
| `Dollars` | Invoice dollar amount |

### Invoice Flag Prediction
| Feature | Description |
|---------|-------------|
| `invoice_quantity` | Number of units in invoice |
| `invoice_dollars` | Total invoice amount |
| `freight` | Freight cost on invoice |
| `total_item_quantity` | Total quantity across all items in PO |
| `total_item_dollars` | Total dollar value across all items in PO |

---

## 🗄️ Database

The project uses a SQLite database (`inventory.db`) with the following tables:

- `vendor_invoice` — Invoice-level records (quantity, dollars, freight, dates)
- `purchases` — Purchase order line items (brand, quantity, dollars, dates)

> **Note:** The database file is excluded from version control via `.gitignore`.

---

## 🏷️ Risk Flagging Logic

An invoice is labeled as **high risk (flag = 1)** if:
- The difference between `invoice_dollars` and `total_item_dollars` exceeds **$5**
- The average receiving delay exceeds **10 days**

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Streamlit** — Frontend UI
- **Scikit-learn** — ML models
- **Pandas / NumPy** — Data processing
- **Joblib** — Model serialization
- **SQLite** — Data storage

---

## 📌 Notes

- `models/` folder and `.pkl` files are excluded from Git — run `train1.py` to regenerate
- Database file (`inventory.db`) is excluded from Git for security
- Make sure database path in `data_preprocessing.py` matches your local setup

---

## 👤 Author

**Your Name**  
BS Computer Science
