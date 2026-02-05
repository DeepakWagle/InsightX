import pandas as pd
from pathlib import Path

DATA_DIR=Path(__file__).parent.parent / "data"

def load_raw(name):
    path=DATA_DIR/"raw"/name
    return pd.read_csv(path)

def load_processed(name):
    path=DATA_DIR/"processed"/name
    return pd.read_csv(path)

def save_processed(df, name):
    path=DATA_DIR/"processed"
    path.mkdir(parents=True, exist_ok=True)
    df.to_csv(path/name, index=False)
    