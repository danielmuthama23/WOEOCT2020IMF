

# WOEOCT2020IMF

## Overview

This project involves analyzing the World Economic Outlook (WEO) dataset from the International Monetary Fund (IMF), with a focus on predicting and clustering various economic indicators. The work is conducted using Python, following the PEP8 style guide, and is primarily done in Jupyter notebooks.

## Dataset

- [WEO October 2020 Database - IMF](https://www.imf.org/en/Publications/WEO/weo-database/2020/October/download-entire-database)
- [WEO October 2020 Data File](https://www.imf.org/~/media/Files/Publications/WEO/WEO-Database/2020/02/WEOOct2020all.ashx)

## Goal

The primary goal of this project is to learn how to analyze economic data, perform clustering, and predict GDP per capita using machine learning techniques.

## Technologies Used

- [Pandas](https://pandas.pydata.org/)
- [Anaconda](https://www.anaconda.com/products/individual)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [NumPy](https://numpy.org/doc/stable/user/quickstart.html)
- [Jupyter Notebook](https://jupyter.org/)

## Tasks

### Data Analysis & Machine Learning

1. **Identify Top 10 Countries by GDP Per Capita Growth:**
   - Find the top 10 countries that had the most significant growth in "Gross domestic product per capita" over the last decade.

2. **Visualize OECD Countries' Population Growth:**
   - Plot the "Population" growth of OECD countries over the last decade.

3. **Save GDP Growth Charts:**
   - Generate and save PNG charts showing GDP growth figures.

4. **Clustering Countries:**
   - Create 5 clusters of countries based on GDP and "Volume of exports of goods".
   - Plot the clusters (x-axis: GDP, y-axis: Volume of Exports).
   - Label the top 5 countries by GDP within each cluster.

5. **Feature Analysis for 2015 Data:**
   - Identify the data fields from the year 2015 that are present in most countries.

6. **Predictor Development:**
   - Create a predictor (using Scikit-learn) to forecast GDP per capita, excluding other GDP-related fields.
   - Calculate and display the Mean Squared Error (MSE) for both training and testing datasets.
   - List the fields used during training.
   - Identify the top 5 features that contribute the most to predictions.
   - Train another predictor using only these top 5 features.
   - Save the predictor to a file.

### HTTP API Development

#### Goal

Learn how to serve the trained machine learning model via a web API.

#### Technologies Used

- [Scikit-learn](https://scikit-learn.org/stable/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)

#### Tasks

1. **Create HTTP Endpoint (WEB API):**
   - Develop a Flask-based endpoint that accepts a JSON body with the following fields: "continent", "population", "Gross national savings", and the top 5 features identified in Task 6.
   - Example JSON request:
     ```json
     {
       "gross_nation_savings": 10,
       "continent": "Europe",
       ...
     }
     ```
   - The response should be a JSON object containing the predicted GDP per capita.

2. **Automated Testing:**
   - Write an automated test using the `unittest` package to ensure that the endpoint works as expected.
   - Reference for testing with Flask: [Flask Testing Documentation](https://flask.palletsprojects.com/en/1.1.x/testing/#the-first-test)

---

