import tabula
import pandas as pd
# Read the PDF file into a list of pandas DataFrames
df_list = tabula.read_pdf("TableData.pdf", multiple_tables=True, pages="all")

# Loop through the list of DataFrames
for i, df in enumerate(df_list):
  # Drop the 'Unnamed' column from each DataFrame
  df = df.drop(columns=['Unnamed: 0'])

# Concatenate the modified DataFrames into a single DataFrame
df = pd.concat(df_list)

#remove colums with no data 
df = df.dropna(how='all', axis=1)

# Save the combined DataFrame to a CSV file
df.to_csv("modified_data.csv", index=False)
##kabhi kabhi......


