import os

# Get the absolute path of the directory containing config.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Prepend 'file://' to force PySpark to read/write to the local disk instead of HDFS
RAW_DATA_PATH = f"file://{os.path.join(BASE_DIR, 'data/raw_orders.csv')}"
PROCESSED_DATA_PATH = f"file://{os.path.join(BASE_DIR, 'data/processed/orders_parquet')}"