# Databricks notebook source
# MAGIC %md ##Transform the data into the star schema for a Gold data store;

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import TimestampType
from pyspark.sql import functions as f
from pyspark.sql.types import StringType

# COMMAND ----------

# MAGIC %md ####Table fact_payments

# COMMAND ----------

#Create dataframe
payments_df = spark.table("staging_payments")
payments_df.show(5)

# COMMAND ----------

#Create table
spark.sql("DROP TABLE IF EXISTS fact_payments")
payments_df.write.format("delta")   \
                 .mode("overwrite") \
                 .saveAsTable("fact_payment")

# COMMAND ----------

# MAGIC %md ####Table dim_stations

# COMMAND ----------

#Create dataframe
stations_df = spark.table("staging_stations")
stations_df.show(5)

# COMMAND ----------

#Create table
spark.sql("DROP TABLE IF EXISTS dim_stations")
stations_df.write.format("delta")   \
                 .mode("overwrite") \
                 .saveAsTable("dim_stations")

# COMMAND ----------

# MAGIC %md ####Table dim_riders

# COMMAND ----------

#Create dataframe
rider_df = spark.table("staging_riders")
rider_df.show(5)

# COMMAND ----------

#Create table
spark.sql("DROP TABLE IF EXISTS dim_riders")
rider_df.write.format("delta")   \
                 .mode("overwrite") \
                 .saveAsTable("dim_riders")

# COMMAND ----------

# MAGIC %md ####Table fact_trips

# COMMAND ----------

trips = spark.table("staging_trips")
fact_trips = trips.join(rider_df, trips.rider_id == rider_df.rider_id, "left" ) \
            .withColumn('duration', round((unix_timestamp("ended_at") - unix_timestamp('started_at'))/60)) \
            .withColumn('rider_age', round(datediff(to_date(rider_df.account_start_date), to_date(rider_df.birthday))/365.25)) \
            .select("trip_id","staging_trips.rider_id","rideable_type","started_at","ended_at","duration","rider_age","start_station_id","end_station_id")
fact_trips.show(5)

# COMMAND ----------

#Create table
spark.sql("DROP TABLE IF EXISTS fact_trips")
fact_trips.write.format("delta")   \
                 .mode("overwrite") \
                 .saveAsTable("fact_trips")

# COMMAND ----------

# MAGIC %md ###Create dimDate table

# COMMAND ----------

# Get min date from trips
min_date = trips.selectExpr('MIN(started_at) AS started_at').first().asDict()['started_at']
# Get max date from trips
max_date = trips.selectExpr('MAX(started_at) AS started_at').first().asDict()['started_at']
expression = f"sequence(to_date('{min_date}'), to_date('{max_date}'), interval 1 day)"
dim_date = spark.createDataFrame([(1,)], ["date_id"])

dim_date = dim_date.withColumn("dateinit", f.explode(f.expr(expression)))
dim_date = dim_date.withColumn("date", f.to_timestamp(dim_date.dateinit, "yyyy-MM-dd"))

dim_date = dim_date \
            .withColumn("day_of_week", f.dayofweek(dim_date.date)) \
            .withColumn("day_of_month", f.dayofmonth(dim_date.date)) \
            .withColumn("month", f.month(dim_date.date)) \
            .withColumn("quarter", f.quarter(dim_date.date)) \
            .withColumn("year", f.year(dim_date.date)) \
            .withColumn("date_id", dim_date.date.cast(StringType())) \
            .drop(f.col("dateinit")) \
            .drop(f.col("date")) 
dim_date.show(5)

# COMMAND ----------

#Create table
spark.sql("DROP TABLE IF EXISTS dim_date")
fact_trips.write.format("delta")   \
                 .mode("overwrite") \
                 .saveAsTable("dim_date")

# COMMAND ----------

