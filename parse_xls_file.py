import pandas as pd

# Load the Excel file
excel_file = 'your_excel_file.xlsx'

# Parse all sheets
xlsx = pd.ExcelFile(excel_file)

# Dictionary to hold dataframes for each sheet
dfs = {}

# Loop through each sheet in the Excel file
for sheet_name in xlsx.sheet_names:
    # Parse the sheet and store it in the dictionary
    dfs[sheet_name] = pd.read_excel(xlsx, sheet_name=sheet_name)

# Now, dfs will have a DataFrame for each sheet in the Excel file
# Example: print contents of each dataframe
for sheet, df in dfs.items():
    print(f"Contents of sheet '{sheet}':")
    print(df)
    print("\n")
