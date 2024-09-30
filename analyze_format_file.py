import pandas as pd
import matplotlib.pyplot as plt

# Load the DataFrame with error handling
def load_dataframe(filepath):
    try:
        df = pd.read_parquet(filepath)
        return df
    except Exception as e:
        print(f"Error loading the DataFrame: {e}")
        return None

class TableFormat:
    def __init__(self, df):
        self.df = df
        self.metadata = []

    def collect_metadata(self):
        for column in self.df.columns:
            col_data = {
                'Column Name': column,
                'Data Type': str(self.df[column].dtype),  # Convert dtype to string for better display
                'Max Value': self.df[column].max(),
                'Min Value': self.df[column].min(),
                'Number of Nulls': self.df[column].isnull().sum(),
                'Number of Blanks': (self.df[column] == '').sum(),
                'Duplicates': self.df[column].duplicated().sum(),
                'Unique Count': self.df[column].nunique(),
            }
            self.metadata.append(col_data)

    def display_metadata(self):
        metadata_df = pd.DataFrame(self.metadata)

        # Set display options
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        
        print(metadata_df)

        # Save the metadata as an image
        self.save_metadata_image(metadata_df)

    def save_metadata_image(self, metadata_df):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText=metadata_df.values,
                         colLabels=metadata_df.columns,
                         cellLoc='center',
                         loc='center')
        plt.savefig('metadata_image.png', bbox_inches='tight', dpi=300)
        plt.close()
        print("Metadata saved as 'metadata_image.png'")

# Get file path from user input
filepath = input("Enter the path to the Parquet file: ")
df = load_dataframe(filepath)

if df is not None:  # Proceed only if the DataFrame was loaded successfully
    table_format = TableFormat(df)
    table_format.collect_metadata()
    table_format.display_metadata()
