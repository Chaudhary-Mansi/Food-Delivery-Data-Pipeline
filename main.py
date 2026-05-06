from pyspark.sql import SparkSession
from src.extract import extract
from src.transform import transform
from src.load import load

def run_pipeline():
    # Centralize SparkSession management
    spark = SparkSession.builder \
        .appName("FoodDeliveryETL") \
        .getOrCreate()
    
    try:
        # Pass the spark session to the extract function
        df = extract(spark)
        df_transformed = transform(df)
        load(df_transformed)
    finally:
        # Ensure resources are released even if an error occurs
        spark.stop()

if __name__ == "__main__":
    run_pipeline()