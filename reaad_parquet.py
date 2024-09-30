import pandas as pd

#df=pd.read_parquet('C:\\Users\\ravi.singh2\\Desktop\\Project_data_VJL\\SALESFORCE_DATA\\RmaLine.parquet')
df=pd.read_parquet('C:\\Users\\ravi.singh2\\Desktop\\Project_data_VJL\\SALESFORCE_DATA\\RmaHeader.parquet')
df=dict(df)
df=df.columns()
#df=df.to_json()

df=type(df)
read5rows=df
# .head(5)
print(read5rows)
print(df)