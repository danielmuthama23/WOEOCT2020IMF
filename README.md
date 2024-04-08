# WOEOCT2020IMF

## Overall

All work should follow the PEP8 style guide
Jupyter notebook part

## Dataset
https://www.imf.org/en/Publications/WEO/weo-database/2020/October/download-entire-database
https://www.imf.org/~/media/Files/Publications/WEO/WEO-Database/2020/02/WEOOct2020all.ashx

## Goal
Learn to analyze the data

## Technologies used
https://pandas.pydata.org/
https://www.anaconda.com/products/individual
https://scikit-learn.org/stable/
https://numpy.org/doc/stable/user/quickstart.html
https://jupyter.org/

## Tasks
Find top 10 countries that grew "Gross domestic product per capita" the most over the last decade
Draw OECD countries' "Population" growth over the last decade
Save the GDP growth figures in separate charts and save them as PNG files
Create 5 clusters out of the countries using GDP and "Volume of exports of goods"
draw the charts (x-axis - GDP, y - volume)
Add labels for the top 5 countries according to the GDP on the dots representing countries in each cluster
Find all the data fields from the year 2015 that are present in most of the countries
Create a predictor (use scikit) to predict GDP per capita (exclude other GDP-related fields). 
Show prediction error (MSE) on the training and the testing data sets
Name the fields that were used during training
Find the top 5 fields/features that contribute the most to the predictions
Train another predictor that uses those top 5 features
Save the predictor in a file

## HTTP API development
## Goal
Learn to serve the trained model

## Used technologies
https://scikit-learn.org/stable/
https://flask.palletsprojects.com/en/1.1.x/

## Tasks

Create HTTP endpoint (WEB API) (use Flask):
The endpoint should accept JSON body using these fields: "continent, population, Gross national savings" and previously found top 5 features (6d task)
example: {"gross_nation_savings": 10, "continent": "Europe" …. }
The returned response (JSON) should contain field shows the predicted GDP per capita
Write an automated test (use unittest package) using flask (https://flask.palletsprojects.com/en/1.1.x/testing/#the-first-test) that would check whether the endpoint works



