import pandas as pd 
df = pd.read_csv('sampledata.csv')

class DataProfiling:
    def __init__(self):
        self.results = []  # Constructor currently does nothing

    def column_count(self, dataframe):
        return len(dataframe.columns)
    def datatype(self, dataframe):
        for column in dataframe.columns:
            dtype = dataframe[column].dtype
            self.results.append((column, dtype))
    def maxvalue(self, dataframe):
        self.results.clear() 
        for column in dataframe.columns:
            if pd.api.types.is_numeric_dtype(dataframe[column]):
                mval = dataframe[column].max()  
                self.results.append((column, mval))  
            else:
                self.results.append((column, None)) 


# Create an instance of DataProfiling
profiling = DataProfiling()

# Get the column count
count = profiling.column_count(df)
print(f"Number of columns: {count}")

profiling.datatype(df)

# Print all results
print("Data types of each column:")
for column, dtype in profiling.results:
    print(f"{column}: {dtype}")

profiling.maxvalue(df)

# Print maximum values
print("Maximum values of each column:")
for column, mval in profiling.results:
    print(f"{column}: {mval}")