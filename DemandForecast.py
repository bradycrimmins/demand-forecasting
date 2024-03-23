import pandas as pd
from snowflake.connector import connect as snowflake_connect
from google.cloud import bigquery

# Snowflake connection and query execution
snowflake_conn = snowflake_connect(user='<user>', password='<password>', account='<account>')
snowflake_query = "SELECT date, product_id, quantity_sold FROM sales_data"
df_sales = pd.read_sql(snowflake_query, snowflake_conn)
snowflake_conn.close()

# Google BigQuery connection and query execution
client = bigquery.Client()
bigquery_query = """
SELECT date, product_id, promotion_flag
FROM `project.dataset.promotions`
"""
df_promotions = client.query(bigquery_query).to_dataframe()

# Merge datasets on 'date' and 'product_id'
df = pd.merge(df_sales, df_promotions, on=['date', 'product_id'], how='left')

# Fill missing values in 'promotion_flag' with 0 (no promotion)
df['promotion_flag'] = df['promotion_flag'].fillna(0)

# Convert 'date' to datetime and sort the dataframe
df['date'] = pd.to_datetime(df['date'])
df.sort_values('date', inplace=True)

# Creating additional time features for the model
df['dayofweek'] = df['date'].dt.dayofweek
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

# Aggregating data at a daily level for forecasting
df_daily = df.groupby('date').agg({'quantity_sold': 'sum', 'promotion_flag': 'max', 'dayofweek': 'first', 'month': 'first', 'year': 'first'}).reset_index()
from fbprophet import Prophet

# Prepare dataframe for Prophet
df_prophet = df_daily.rename(columns={'date': 'ds', 'quantity_sold': 'y'})

# Initialize Prophet with daily seasonality
model = Prophet(daily_seasonality=True)
model.add_regressor('promotion_flag')
model.add_regressor('dayofweek')
model.add_regressor('month')
model.add_regressor('year')

# Fit the model
model.fit(df_prophet)

# Create future dataframe including regressors
future_dates = model.make_future_dataframe(periods=90)
future_dates = future_dates.merge(df_daily[['date', 'promotion_flag', 'dayofweek', 'month', 'year']], left_on='ds', right_on='date', how='left').fillna(method='ffill').drop(columns=['date'])

# Predict future sales
forecast = model.predict(future_dates)

# Plot the forecast
fig1 = model.plot(forecast)
