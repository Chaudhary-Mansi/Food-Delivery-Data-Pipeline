# Food Delivery Data Pipeline 🚀

📌 Overview

This project implements an end-to-end data engineering pipeline for a food delivery platform using PySpark and Apache Airflow. It simulates real-world data-processing workflows used in large-scale systems such as Swiggy and Zomato.

The pipeline extracts raw order data from a CSV source (representing ingestion from distributed storage such as HDFS), processes and transforms it using PySpark to generate key business metrics such as revenue and delivery delays, and stores the transformed data in Parquet format for efficient analytics.

Apache Airflow is used to orchestrate and schedule the pipeline, enabling automated and reliable execution. The overall design follows ETL principles and is built with scalability, modularity, and production-readiness in mind.

**🚀 Features**

- **Scalable Data Processing with PySpark**
Processes large volumes of order data using distributed computing, ensuring efficient and scalable transformations.

- **End-to-End ETL Pipeline**
Implements a complete Extract → Transform → Load workflow, from raw data ingestion to analytics-ready storage.

- **Business-Centric Transformations**
Generates key metrics such as revenue calculation and delivery delay indicators to support data-driven decision-making.

- **Optimized Storage using Parquet**
Stores processed data in columnar Parquet format for faster querying and improved storage efficiency.

- **Workflow Orchestration with Apache Airflow**
Automates and schedules data pipelines using DAGs, ensuring reliability and repeatability.

- **Modular and Maintainable Codebase**
Separates extraction, transformation, and loading logic into independent modules for better scalability and reusability.

- **Production-Ready Design Approach**
Follows industry best practices such as idempotent processing, structured logging, and clean architecture.

**🏗️ Architecture (Interview-Ready Explanation)**
The pipeline follows a modular ETL architecture designed to simulate real-world data engineering systems.

**1. Data Ingestion (Extract Layer)**
Raw order data is ingested from a CSV file, representing data coming from distributed storage systems like HDFS or cloud object storage. PySpark is used to read the data into a distributed DataFrame for parallel processing.

**2. Data Transformation (Processing Layer)**
The transformation layer is implemented using PySpark and includes:

Data cleaning (handling null values)
Feature engineering (calculating revenue and delivery delay flags)
Schema standardization

This layer ensures that raw data is converted into structured, analytics-ready datasets.

**3. Data Storage (Load Layer)**
The transformed data is written in Parquet format, which:

Improves query performance
Reduces storage footprint
Aligns with data lake best practices

This simulates storing data in systems like Amazon S3, HDFS, or data warehouses.

**4. Workflow Orchestration (Airflow Layer)**
Apache Airflow is used to:

Define the ETL workflow as a DAG
Schedule daily pipeline execution
Manage dependencies between tasks

This ensures the pipeline runs reliably in a production-like environment.

**5. Scalability & Design Considerations**
Designed for distributed execution using Spark
Modular structure for easy extension (e.g., Kafka, Hive)
Supports batch processing with scope for real-time upgrades

**⚙️ Tech Stack**
PySpark
Python
Apache Airflow
Parquet (Data Storage)

**▶️ How to Run**
pip install -r requirements.txt
python src/main.py

**📁 Project Structure**
```
food-delivery-data-pipeline/
│
├── dags/ 
|   |
│   └── etl_dag.py
│
├── src/ 
|   |
│   ├── extract.py
|   |
│   ├── transform.py
|   |
│   ├── load.py
|   |
│   └── main.py
│
├── data/    
|   |
│   ├── raw_orders.csv           
|   |
│   └── processed/               
│
├── logs/                         
│  |
├── config.py 
|  |
├── requirements.txt  
|  |
├── README.md    
|  |
├── .gitignore  
```
