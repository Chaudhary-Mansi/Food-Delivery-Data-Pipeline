from config import RAW_DATA_PATH

def extract(spark):
    # Use the session passed from main.py
    df = spark.read.csv(RAW_DATA_PATH, header=True, inferSchema=True)
    return df