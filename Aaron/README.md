# Aaron

## Data Gathering
Initially gathered data for not yet agreed upon project. This included data on suicide and cyrpto currency. As a team we then discussed what topic we going to go with at that time it was determined that we would go with crypto currency. When merging our data to the main branch the suicide data was not merged as it was no longer needed.

## Data Cleaning
After we gathered the crypto data I was tasked with cleaning the data for use in machine learning and for part of the dashboard. I encountered a couple of challenges that I needed to overcome. 

1. combining all 5 files into one combined working data set. This was accomplished in 2 parts. 

  Part 1 was identifying all the files that I needed to combine. I found a library that I could use to pull the files into a list. The library was glob below is how I used the library to pull all 5 file.

![glob](https://user-images.githubusercontent.com/113067853/225770265-30d3d33f-29e4-4f64-bd94-d58d13645d9d.PNG)

  Part 2 was to combine all 5 files into one DataFrame. I had a challenge doing this as most of the files had different number of headers. To solve this I needed to pull in the join parameter and set it to inner. This would only bring in columns from every data set that they all had in common.  

![combined](https://user-images.githubusercontent.com/113067853/225770893-a26d022a-4846-4169-adee-43c2bc9f2c85.PNG)

2. Creating machine learning data set and dashboard the main challenge I encounter was calculating the percent of change column. After creating the working data set for machine learning and the dashboard the data was not indexed correctly. This caused the calculation to error.

![index 1](https://user-images.githubusercontent.com/113067853/225773857-57170a01-e9db-4655-be67-59e2013b8fdc.PNG)

  After re-indexing the data the loop that calculated the percent of change ran correctly. 
  
![index 2](https://user-images.githubusercontent.com/113067853/225774221-24b41fba-6f88-4677-93f6-1056b89b21d7.PNG)
![percent of change](https://user-images.githubusercontent.com/113067853/225774380-3e45ed66-8d3b-44ee-91b2-e766443ce3fb.PNG)

## Images
I was also tasked with reviewing David's code and gathering the graph plots for each the currencies to be used in the dashboard. 
