# Real-Time-Salary-Predictor-For-Data-Scientists-In-Pakistan
We have managed to get real time access to the data science jobs available all across Pakistan. We have preprocessed and analyzed the data to get the distinct job title, salary range and other features. We have designed the appropriate model to generate salary predictor for the raw job data fields not containing salary.

We have scrapped the pk.indeed.com to generate simple scrapper for data science job fields in Islamabad. Then we extended it to all the cities across pakistan. Here is the sneakpeak of the raw data generated.

![Image of RawData](https://hmp.me/dbvx)

We have preprocesssed the data to extract some insights from the synopsis or job description as well as found out the minimum , maximum and average salary from the rows where the salary is given. We have also divided the data into with salary and without salary data. Here is the cleaned data used for exploratory analysis and modeling

![Image of Yaktocat](https://camo.githubusercontent.com/a3e6f6c156e9034578dc4c225c5b114128bec7ec/68747470733a2f2f686d702e6d652f64627679)

We have managed to get the useful insights from the cleaned data above. Here is the sneak peak of exploratory analysis of data.

![Image of Yaktocat](https://camo.githubusercontent.com/cb9c0f7b4b440c0a2bf39b69f6d07e09a97ce63a/68747470733a2f2f686d702e6d652f6462767a)
![Image of Yaktocat](https://hmp.me/dbv0)

We have tried out label-encoding as well as one-hot encoding during the modeling process. We have implemented Binary Decision Tree Model as well as the Random Forest Model. The random forest gives us the better on the spilited training and test data. So, we have decided to deploy the random forest model on all the job fields with and without salaries. Here is the result

![Image of Yaktocat](https://hmp.me/dbv1)

