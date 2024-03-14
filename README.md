# Description

Salary data is important for many businesses as it can play a significant role in distribution of their resources. For example, a high end product needs to market their goods only to people with high income. A charitable organization may be focused to invest in areas where people make less money. Likewise, it will also help businesses to determine prices of its products and forecast sales. Governments may also be interested to know the status-quo of their citizens to carry out effective economic and development plans.
Since the project determines whether a person makes more than 50K or not, we are determining the dependent categorical variable. Here, we will first collect the relevant data set. Once we collect the data, we will prepare the data using pandas, numpy and visualize the data to determine the relationship between the variables. After studying the data set, we will preprocess the data using python where we will eliminate the outliers and manage missing values. Once we successfully preprocess the data, we will make use of python’s supervised learning packages and algorithms to build our model. Once we prepare the model, we will access the model based upon its accuracy, sensitivity, and specificity. If the model meets our requirements, we will deploy the model to make predictions on income level of individuals.

# About Dataset

The original dataset was obtained from the 1994 U.S. Census database. The census is performed every decade within the United States. It gathers information on the population living within the country. The information captured from the census consists of data on age, gender, country of origin, marital status, housing conditions, marriage, education, employment, etc. The sneakpeak of the dataset is as follows:

![image](https://github.com/niranjan122345/desktop-tutorial/assets/143377183/1dba6525-40ba-4f2c-b93b-f4d0ac22696d)

# Features

* Image based income prediction: upload image of income prediction
* Demo video: Visual walkthrough to guide users
  
# Demo video: https://github.com/niranjan122345/desktop-tutorial/assets/143377183/21e0d265-8497-40fe-9b22-82e10c41a97f

# Screenshot: !(https://github.com/niranjan122345/desktop-tutorial/assets/143377183/2d13a9cd-6097-42e4-90e7-d2f91c8806f2)

# Approach

    * Data description

        * We will be using Income prediction dataset in the kaggle repository. This data set is satisfying our data requirement.

    * Data splitting

       * We split the data here for our train and test data for further uses.

    * Data Preprocessing

      * As our data is full of categorical values, so we can convert all those to numerical values by label encoding.

    * Model training

     * We trained various model in our notebook and svc was good on it.

    * Model saving

     * We will save our model that we can use them for prediction purpose.

    * data for prediction purpose

     * Now our application on cloud is ready for doing prediction.

    * Data processing and prediction

     * Client data will also go along the same process. Data pre processing and according to that we will predict those data.
 # Implication project for future studies

      Dataset gathers income information about people living in America in 1994. The data tracks age, education, marital status, hours worked and shares how much money an individual brings home based on those characteristics. The implications of this project may help society to determine what a person living in America needs to do to acquire a better income, while also bringing to light possible discrimination. It shows how working more hours has a better chance of improving your earning potential. It also shows a correlation between being married and income. Generally, it seems married couples on average have a better chance of making more than 50,000 than a single person. The project also shows the racial inequality in the 1994’s. Whites had a greater percentage of people with incomes greater than 50,000. Another socioeconomic issue brought forth is how men were three times more likely to have incomes greater than 50,000 as compared to women.

This model can be used to analyze data of any year. We can update the datasource and use the same code to derive our socioeconomic conclusions. By adding more recent observations of individuals to the dataset, we can also build a predictive model which takes present salary data into consideration.
