# Real-Time-Salary-Predictor-For-Data-Scientists-In-Pakistan
We have managed to get real time access to the data science jobs available all across Pakistan. We have preprocessed and analyzed the data to get the distinct job title, salary range and other features. We have designed the appropriate model to generate salary predictor for the raw job data fields not containing salary.

We have scrapped the pk.indeed.com to generate simple scrapper for data science job fields in Islamabad. Then we extended it to all the cities across pakistan. Here is the sneakpeak of the raw data generated.

![Image of RawData](https://hmp.me/dbvx)

We have preprocesssed the data to extract some insights from the synopsis or job description as well as found out the minimum , maximum and average salary from the rows where the salary is given. We have also divided the data into with salary and without salary data. Here is the cleaned data used for exploratory analysis and modeling

![Image of Yaktocat](https://hmp.me/dbvy)

We have managed to get the useful insights from the cleaned data above. Here is the sneak peak of exploratory analysis of data.

![Image of Yaktocat](https://hmp.me/dbvz)
![Image of Yaktocat](https://hmp.me/dbv0)

We have tried out label-encoding as well as one-hot encoding during the modeling process. We have implemented Binary Decision Tree Model as well as the Random Forest Model. The random forest gives us the better on the spilited training and test data. So, we have decided to deploy the random forest model on all the job fields with and without salaries. Here is the result

![Image of Yaktocat](https://hmp.me/dbv1)

