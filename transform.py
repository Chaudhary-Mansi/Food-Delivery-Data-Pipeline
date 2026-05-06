from pyspark.sql.functions import col, when

def transform(df):
    # Remove null values
    df = df.dropna()

    # Remove duplicates
    df = df.dropDuplicates()

    # Create delivery delay flag
    df = df.withColumn(
        "delivery_delay",
        when(col("delivery_time") > col("expected_time"), 1).otherwise(0)
    )

    # Create revenue column
    df = df.withColumn(
        "revenue",
        col("price") * col("quantity")
    )

    return df