# Databricks notebook source
# DBTITLE 1,Write data payments to Delta file system
payments_df = spark.read.format("csv") \
     .option("inferSchma","false") \
     .option("header","true") \
     .option("step",",")      \
     .load("/FileStore/payments.csv") \
     .toDF("payment_id","date","amount","rider_id")
payments_df = payments_df.dropDuplicates(payments_df.columns)

#Verify data
payments_df.printSchema
display(payments_df.limit(10))

# COMMAND ----------

## Write data to the 'delta' location
payments_df.write.format("delta") \
           .mode("overwrite") \
           .option("overwriteSchema", "true") \
           .save("/delta/payments")

# COMMAND ----------

# DBTITLE 1,Write data riders to Delta file system
riders_df = spark.read.format("csv") \
     .option("inferSchma","false") \
     .option("header","true") \
     .option("step",",")      \
     .load("/FileStore/riders.csv") \
     .toDF("rider_id","address","first_name","last_name","birthday","account_start_date","account_end_date","is_member")
riders_df = riders_df.dropDuplicates(riders_df.columns)

#Verify data
riders_df.printSchema
display(riders_df.limit(10))

# COMMAND ----------

## Write data to the 'delta' location
riders_df.write.format("delta") \
           .mode("overwrite") \
           .option("overwriteSchema", "true") \
           .save("/delta/riders")

# COMMAND ----------

# DBTITLE 1,Write data stations to Delta file system
stations_df = spark.read.format("csv") \
     .option("inferSchma","false") \
     .option("header","true") \
     .option("step",",")      \
     .load("/FileStore/stations.csv") \
     .toDF("station_id","name","latitude","longitude")
stations_df = stations_df.dropDuplicates(stations_df.columns)

#Verify data
stations_df.printSchema
display(stations_df.limit(10))

# COMMAND ----------

## Write data to the 'delta' location
stations_df.write.format("delta") \
           .mode("overwrite") \
           .save("/delta/stations")

# COMMAND ----------

# DBTITLE 1,Write data trips to Delta file system
trips_df = spark.read.format("csv") \
     .option("inferSchma","false") \
     .option("header","true") \
     .option("step",",")      \
     .load("/FileStore/trips.csv") \
     .toDF("trip_id","rideable_type","started_at","ended_at","start_station_id","end_station_id","rider_id")
trips_df = trips_df.dropDuplicates(trips_df.columns)

#Verify data
trips_df.printSchema
display(trips_df.limit(10))

# COMMAND ----------

## Write data to the 'delta' location
trips_df.write.format("delta") \
           .mode("overwrite") \
           .save("/delta/trips")

# COMMAND ----------

