# Databricks notebook source
# MAGIC %md ##Create a gold data store in Delta Lake tables
# MAGIC Scripts to create SQL table from Delta file locations.

# COMMAND ----------

##Create payments gold data store
if spark.catalog.tableExists("staging_payments") == True :
    spark.sql("DROP TABLE staging_payments")
spark.sql("CREATE TABLE staging_payments USING DELTA LOCATION '/delta/payments'")

# COMMAND ----------

##Create riders gold data store
if spark.catalog.tableExists("staging_riders") == True :
    spark.sql("DROP TABLE staging_riders")
spark.sql("CREATE TABLE staging_riders USING DELTA LOCATION '/delta/riders'")

# COMMAND ----------

##Create stations gold data store
if spark.catalog.tableExists("staging_stations ") == True :
    spark.sql("DROP TABLE staging_stations ")
spark.sql("CREATE TABLE staging_stations USING DELTA LOCATION '/delta/stations'")

# COMMAND ----------

##Create trips gold data store
if spark.catalog.tableExists("staging_trips") == True :
    spark.sql("DROP TABLE staging_trips ")
spark.sql("CREATE TABLE staging_trips USING DELTA LOCATION '/delta/trips'")

# COMMAND ----------

