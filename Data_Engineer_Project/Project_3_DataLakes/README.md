# Building an Azure Data Lake for Bike Share Data Analytics

## Project Overview:

- Divvy is a bike sharing program in Chicago, Illinois USA that allows riders to purchase a pass at a kiosk or use a mobile application to unlock a bike at stations around the city and use the bike for a specified amount of time. The bikes can be returned to the same station or to another station. The City of Chicago makes the anonymized bike trip data publicly available for projects like this where we can analyze the data.

- Since the data from Divvy are anonymous, we have created fake rider and account profiles along with fake payment data to go along with the data from Divvy. The dataset looks like this:

![image](https://user-images.githubusercontent.com/114274480/223376036-628457bb-f42e-4ab7-9a35-8f8fa039731d.png)

(Relational ERD for the Divvy Bikeshare Dataset (with fake data tables))

- The goal of this project is to develop a data warehouse solution using Azure Synapse Analytics. You will:

  - Design a star schema based on the business outcomes listed below;
  - Import the data into Azure Databricks using Delta Lake to create a Bronze data store;
  - Create a gold data store in Delta Lake tables;
  - Transform the data into the star schema for a Gold data store;
 
## The business outcomes you are designing for are as follows:
- Analyze how much time is spent per ride
  - Based on date and time factors such as day of week and time of day
  - Based on which station is the starting and / or ending station
  - Based on age of the rider at time of the ride
  - Based on whether the rider is a member or a casual rider
- Analyze how much money is spent
  - Per month, quarter, year
  - Per member, based on the age of the rider at account start
- EXTRA CREDIT - Analyze how much money is spent per member
  - Based on how many rides the rider averages per month
  - Based on how many minutes the rider spends on a bike per month

# Execution Azure Data Warehouse Project
About data (csv file) is used in project. Can be download at [here](https://video.udacity-data.com/topher/2022/March/622a5fc6_azure-data-warehouse-projectdatafiles/azure-data-warehouse-projectdatafiles.zip)
## I. Star Schema Design
### Image of the star schema I designed based on the relational diagram and the business problems outlined
![start drawio (4)](https://user-images.githubusercontent.com/114274480/225688461-8950bca7-735c-4283-b4c5-8a754eef0d13.png)


## II. Import the data into Azure Databricks using Delta Lake to create a Bronze data store;
Here is a screenshot of importing data into Azure Databricks using Delta Lake to create a Bronze data store
 ![image](https://user-images.githubusercontent.com/114274480/225583164-aa08f233-11ac-424e-ac3a-cb325b4a032e.png)
## III. Create a gold data store in Delta Lake tables;
Using spark SQL to create staging_table
  
 ![image](https://user-images.githubusercontent.com/114274480/225587989-9f62c940-3912-47f2-8d8a-c30cc4cf23d5.png)
 
## IV. Transform the data into the star schema for a Gold data store;
- Use Spark and Databricks to run ELT processes by creating dimension tables and fact tables
 ![image](https://user-images.githubusercontent.com/114274480/225689683-7d6130b2-9536-4dd4-b032-c692019ce076.png)

