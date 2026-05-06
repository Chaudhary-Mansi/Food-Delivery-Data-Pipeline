from config import PROCESSED_DATA_PATH

def load(df):
    df.write.mode("overwrite").parquet(PROCESSED_DATA_PATH)