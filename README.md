# demand-forecasting
# Sales Forecasting with Promotional Impact Analysis

This project presents a comprehensive approach to forecasting sales by integrating sales data from Snowflake and promotional data from Google BigQuery. The core of this analysis lies in understanding how promotions affect sales and incorporating this insight into the sales forecasting model. This README outlines the process from data retrieval and preprocessing to model fitting and forecasting with Facebook's Prophet library.

## Overview

The code provided performs several key steps in the data analytics and forecasting process:

1. **Data Retrieval**: Fetches sales data from Snowflake and promotional data from Google BigQuery, showcasing the ability to integrate data from multiple cloud sources.

2. **Data Preprocessing**: Merges the sales and promotional datasets based on `date` and `product_id`. It handles missing values, converts dates to a proper datetime format, and sorts the DataFrame for time series analysis.

3. **Feature Engineering**: Creates time-related features (`dayofweek`, `month`, `year`) essential for capturing seasonal trends in sales data. 

4. **Data Aggregation**: Aggregates data at a daily level, preparing it for the forecasting model with daily granularity.

5. **Sales Forecasting**: Utilizes Facebook's Prophet library to forecast sales while considering promotional impacts and seasonal factors. Custom regressors are added to the model to account for promotions and time-related features.

6. **Visualization**: Generates a plot of the forecasted sales to visualize predicted trends and the effects of promotions.

## Requirements

- Python 3.x
- pandas
- snowflake-connector-python
- google-cloud-bigquery
- fbprophet

Ensure you have the necessary Python packages installed, along with valid credentials for Snowflake and Google Cloud Platform to access the respective databases.

## Usage

1. **Credentials Setup**: Replace `<user>`, `<password>`, and `<account>` with your Snowflake credentials. For Google BigQuery, ensure your GCP credentials JSON file is correctly configured and accessible to the script.

2. **Query Execution**: The script executes predefined SQL queries to fetch sales data from Snowflake and promotional data from BigQuery. Adjust these queries based on your specific schema and requirements.

3. **Model Training and Forecasting**: The script automatically processes the data, fits the Prophet model, and generates a 90-day sales forecast considering promotional impacts.

4. **Forecast Visualization**: A plot of the forecast is generated, illustrating the predicted sales trends.

## Customization

- **SQL Queries**: Modify the SQL queries to match your database schema and analysis needs.
- **Forecasting Horizon**: Adjust the `periods` parameter in `make_future_dataframe` to change the forecasting horizon.
- **Model Parameters**: Customize the Prophet model by adding or removing regressors, adjusting seasonality configurations, or incorporating holidays.

## Conclusion

This project provides a template for performing advanced sales forecasting by leveraging data from multiple cloud sources and incorporating external factors such as promotions. It demonstrates the power of combining traditional time series analysis with modern machine learning techniques for predictive analytics in the supply chain domain.
