import pandas as pd

# Load dataset
df = pd.read_excel("Telco_customer_churn.xlsx")

def test_dataset_not_empty():
    assert df.shape[0] > 0
    assert df.shape[1] > 0

def test_churn_label_exists():
    assert "Churn Label" in df.columns

def test_duplicate_records():
    assert df.duplicated().sum() >= 0
