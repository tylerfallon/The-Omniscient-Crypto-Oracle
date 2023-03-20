### Bobbi
#### Completed Tasks
##### Created Initial Repository
Initial repository and branches created for all team members. Uploaded basic info files for project. 
<img src="https://user-images.githubusercontent.com/114044192/223879860-72f8e615-601f-4909-9744-3801437744a0.png" width=50% height=50%>

##### Team Name/Logo
Created a few logos for Team to vote on - utilizing team first initial came up with Take A Byte Data  
<img src="https://user-images.githubusercontent.com/114044192/223880647-cf9df5a5-55af-4e1a-aaf6-9cd433fe12bd.jpg" width=20% height=20%>
<img src="https://user-images.githubusercontent.com/114044192/223880696-93a31a6d-3d18-47ae-ac23-393ac8d8bbf0.png" width=20% height=20%>

##### Gather datasets
Initial data sets for daily and monthly all downloaded from investing.com. At next team meeting, we discovered the data did not go back far enough for the monthly dataset for all 5 of the cryptocurrencies. Switched to coinmetrics to find consistant data each spanning at least 10 years prior for all 5 cryptocurrencies. The daily datasets from investing.com each had 2 years of data to use for the trending by day of week, therefore an alternate data source was not needed. 

##### Time Series Research & Resources
Completed research to find resources for using time series data for our dataset and code examples for different objectives for our project. All resources pointed to Long Short-Term Memory (LSTM) - (RNN model), Gated Recurrent Unit (GRU) - (RNN model), and MAE (mean absolute error) at minimum for our Machine Learning process. 

##### Clean/Transform data for Daily (process completed for each dataset)
1. Converted to datetime and added column for the day name 

![image](https://user-images.githubusercontent.com/114044192/223883033-1b214dbc-cded-413e-b6e4-54c86060a72f.png)

2. Identified data types, replaced non numeric characters and convert price from object to float where needed

![image](https://user-images.githubusercontent.com/114044192/223883138-b2200c80-15c1-4919-926e-cb94568c6ed5.png)
![image](https://user-images.githubusercontent.com/114044192/223883479-bbd10b9a-0101-4800-8afa-7fd87a4740ff.png)
![image](https://user-images.githubusercontent.com/114044192/223883218-f293aab1-80d1-4017-a46a-8ec37665d5f7.png)

3. Check for null values (none found) and remove unneeded columns

![image](https://user-images.githubusercontent.com/114044192/223883701-8be0f34b-3cf3-46d8-9f5e-ad4135c19678.png)
![image](https://user-images.githubusercontent.com/114044192/223883766-694ad7cc-6360-4f2f-ac0f-32cab15d1873.png)

4. Duplicate Day column and transform new column to numberic values

![image](https://user-images.githubusercontent.com/114044192/223884062-d96cadf8-c2a6-4f79-9484-45a2984b20fe.png)
![image](https://user-images.githubusercontent.com/114044192/223884142-78e7f095-d703-4308-9f8e-b69a07c20fcb.png)
![image](https://user-images.githubusercontent.com/114044192/223884164-ab0ec214-dd68-449f-b4af-fdaa6cf24da1.png)

5. Group by day and sort by new numerical day column so days appear in correct order

![image](https://user-images.githubusercontent.com/114044192/223884414-f0ee07c3-deef-41b2-a7fe-3c668254e88b.png)
![image](https://user-images.githubusercontent.com/114044192/223884441-5e2ccb1d-9cd7-462a-8a67-5cd32fa5df16.png)

6. Drop numberical day column and generate line graph with results

![image](https://user-images.githubusercontent.com/114044192/223884767-5750483a-a943-49d4-91ba-5080d0cee868.png)

##### Create line graphs showing day of the week trends for each crypto
![image](https://user-images.githubusercontent.com/114044192/223884809-f680644c-b7c4-4a7e-a5de-05424cd52e1d.png)
![Dogecoin Daily](https://user-images.githubusercontent.com/114044192/223884894-1f037697-25fd-4c04-a9f5-c28ebe337072.png)
![ETH Daily](https://user-images.githubusercontent.com/114044192/223884903-3595e265-1081-4cc2-8db1-1ba381f4c079.png)
![LiteCoin Daily](https://user-images.githubusercontent.com/114044192/223884912-b3edd12b-a4fc-413b-b003-f04c0300ffb9.png)
![XRP Daily](https://user-images.githubusercontent.com/114044192/223884926-722eb05b-8d66-471b-88b4-7de6109fd01d.png)

##### Definitions
Pulled basic definitions and graphics from Investopedia.com

##### Project Documents
Formatted main ReadMe for group
Formatted and populated Group Template
Created PowerPoint for Presentation

##### Team collaboration
Assisted in rerunning ML code and saving as csv
Took screenshots of MK Prediction graphics
Outlining Presentation
