# Cloud Data Warehouses with Azure

## Project Overview:

- Divvy is a bike sharing program in Chicago, Illinois USA that allows riders to purchase a pass at a kiosk or use a mobile application to unlock a bike at stations around the city and use the bike for a specified amount of time. The bikes can be returned to the same station or to another station. The City of Chicago makes the anonymized bike trip data publicly available for projects like this where we can analyze the data.

- Since the data from Divvy are anonymous, we have created fake rider and account profiles along with fake payment data to go along with the data from Divvy. The dataset looks like this:

![image](https://user-images.githubusercontent.com/114274480/223376036-628457bb-f42e-4ab7-9a35-8f8fa039731d.png)

(Relational ERD for the Divvy Bikeshare Dataset (with fake data tables))

- The goal of this project is to develop a data warehouse solution using Azure Synapse Analytics. You will:

  - Design a star schema based on the business outcomes listed below;
  - Import the data into Synapse;
  - Transform the data into the star schema;
  - and finally, view the reports from Analytics.
 
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
![image](https://user-images.githubusercontent.com/114274480/223498439-10375c62-d4ce-470b-9d64-e51735f40259.png)
## II. Extract Step
This is screenshot about Azure Blob Storage, include:
 -  public.payment
 -  public.rider
 -  public.trip
 -  public.station
 ![image](https://user-images.githubusercontent.com/114274480/223499761-fac82d93-a2b4-415b-a087-dc9a23b2a0d5.png)
## III. Load Step
Load data from Azure Blob Storage into external tables in the data warehouses:
 ![image](https://user-images.githubusercontent.com/114274480/223500572-ba1d22cc-ff81-4ab8-a82a-f796a314dba7.png)
 - There are [four separate script files](https://github.com/hiiamanh/Learning_Data_Engineering/tree/develop/Data_Engineer_Project/Project_2_Data_Warehouse/SQL_ScriptCreateExternalTable). The SQL files should create tables using CREATE EXTERNAL TABLE (not just CREATE TABLE). The scripts should point to the four files in Blob Storage from the extract step.
