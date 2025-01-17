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

########################################################################################################
import pandas as pd
import json

def convert_json_to_excel(json_file, excel_file):
    """Converts JSON data with multiple worksheets to an Excel file."""

    with open(json_file, 'r') as f:
        data = json.load(f)

    writer = pd.ExcelWriter(excel_file)

    for sheet_name, sheet_data in data.items():
        df = pd.DataFrame(sheet_data)
        df.to_excel(writer, sheet_name=sheet_name, index=False)

    writer.save()

# Example usage
json_file = 'icon.json'  # Replace with your JSON file
excel_file = 'output.xlsx'
convert_json_to_excel(json_file, excel_file)
######################################################################################################
import pandas as pd
import re
import ast

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

string = '[{A:1},{B:3}]'

def string_quotes(data):
    processed_string = re.sub(r'(\w+)', r'"\1"', data)

    # Convert the processed string to a list of dictionary elements
    try:
        result = ast.literal_eval(processed_string)
    except (ValueError, SyntaxError):
        print("Invalid input string format")
        
    return result

str = string_quotes(string)
print(str)

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
