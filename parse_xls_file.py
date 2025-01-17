import pandas as pd

########################################################################################################
# Creating the DataFrame
data = pd.DataFrame([
    {'Attribute': 'wrap_name', 'Value': 'my_ip', 'Description': ''},
    {'Attribute': 'owner', 'Value': 'schilka', 'Description': 'TBD'},
    {'Attribute': 'instance_list', 'Value': '[{ctrl : 1}, {mem : 2}]', 'Description': ''},
    {'Attribute': 'param_def', 'Value': '{top : \n [\n {DATA_WIDTH      : {default : 8}}\n ]\n}', 'Description': ''}
])

#Substitute missing values to an empty string
data.fillna('', inplace=True) 

# Function to get the value associated with a specific attribute
def get_value_by_attribute(data, k_col_hdr, v_col_hdr, attribute_name):
    result = data.loc[data[col_hdr] == attribute_name, v_col_hdr].values
    if result.size > 0:
        return result[0]
    else:
        return None

# Example usage
k_col_hdr      = 'Attribute'
v_col_hdr      = 'Value'
attribute_name = 'owner'
value = get_value_by_attribute(data, k_col_hdr, v_col_hdr, attribute_name)
print(f"Value associated with attribute '{attribute_name}': {value}")

######################################################################################################
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
