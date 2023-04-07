# Data Integration Pipelines for NYC Payroll Data Analytics
## I. Project Overview
The City of New York would like to develop a Data Analytics platform on Azure Synapse Analytics to accomplish two primary objectives:

Analyze how the City's financial resources are allocated and how much of the City's budget is being devoted to overtime.
Make the data available to the interested public to show how the City’s budget is being spent on salary and overtime pay for all municipal employees.
You have been hired as a Data Engineer to create high-quality data pipelines that are dynamic, can be automated, and monitored for efficient operation. The project team also includes the city’s quality assurance experts who will test the pipelines to find any errors and improve overall data quality.

The source data resides in Azure Data Lake and needs to be processed in a NYC data warehouse in Azure Synapse Analytics. The source datasets consist of CSV files with Employee master data and monthly payroll data entered by various City agencies

![image](https://user-images.githubusercontent.com/114274480/230604792-2f117c8e-1394-486c-b9db-864acc289d68.png)

## II. Implement 
### 1. Creating Resources
  a. Created an Azure Data Lake Gen2 with folders and uploaded [.csv files](https://video.udacity-data.com/topher/2022/May/6283aff5_data-nyc-payroll/data-nyc-payroll.zip) to folders.
  
  ![image](https://user-images.githubusercontent.com/114274480/230605220-352f442b-c947-4f41-aabb-b79000e248a2.png)
  
  b. Create an Azure Data Factory Resource

![image](https://user-images.githubusercontent.com/114274480/230605654-8dcb93d8-3bb0-4484-a938-caf14638799b.png)
  
  c. Create a SQL Database to store the current year of the payroll data

![image](https://user-images.githubusercontent.com/114274480/230606313-a7ce526b-fc0d-4ce4-a3e3-20baa11506f4.png)

  d. Create A Synapse Analytics workspace
In the SQL dedicated pool, Create master data tables and payroll transaction tables 

![image](https://user-images.githubusercontent.com/114274480/230606535-6ea92ce3-9939-4462-96c3-9524196dcf87.png)

### 2: Create Linked Services

![image](https://user-images.githubusercontent.com/114274480/230606817-3376d47b-a367-49a6-9ca5-078e64d1d89f.png)

### 3: Create Datasets in Azure Data Factory

![image](https://user-images.githubusercontent.com/114274480/230606912-b6784b75-c12f-4a4b-8f33-4c76448dac4a.png)

### 4: Create Data Flows

- Create pipelines for Employee, Title, Agency, and year 2021 Payroll transaction data to Synapse Analytics containing the data flows.
![image](https://user-images.githubusercontent.com/114274480/230607113-ae520e79-aab6-4f76-aaa0-39889f8d662d.png)

![image](https://user-images.githubusercontent.com/114274480/230608491-b20375a8-e65f-4b1e-bdda-69cf32a443c4.png)


- Create Pipeline to load 2021 Payroll data into transaction table in the SQL DB
![image](https://user-images.githubusercontent.com/114274480/230607251-134c8f1b-1f03-4e80-9035-bc465516e946.png)

### 5: Data Aggregation and Parameterization
Extract the 2021 year data and historical data, merge, aggregate and store it in Synapse Analytics. The aggregation will be on Agency Name, Fiscal Year and TotalPaid.
- The aggregate data flow activities 
![image](https://user-images.githubusercontent.com/114274480/230607637-3c2870fc-c33a-4270-8c93-c1e85b65a9ee.png)

- Finished pipeline
![image](https://user-images.githubusercontent.com/114274480/230607735-1d7bf8d2-dd8a-4ee3-a71c-9e8995d82784.png)

- Data is loaded into Synapse
![image](https://user-images.githubusercontent.com/114274480/230607913-92ddfda6-16df-4e17-8996-760de40e5fd2.png)


