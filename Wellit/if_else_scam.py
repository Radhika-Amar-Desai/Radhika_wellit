import pandas as pd

# Define the name you want to search for
search_name = "BArora"

# Load the CSV file into a DataFrame
file_path = "RadhikaData1.csv"  # Replace with the actual file path
df = pd.read_csv(file_path)

df['VILLAGE'] = df['VILLAGE'].str.upper()
# Search for the name in the "village" column
result = df[df['VILLAGE'] == search_name.upper()]

# Check if any matches were found
if not result.empty:
    depth_value = result.iloc[0]['DEPTH']

    may_bgl = result.iloc[0]['MAY_bgl']
    aug_bgl = result.iloc[0]['AUG_bgl']
    nov_bgl = result.iloc[0]['NOV_bgl']
    jan_bgl = result.iloc[0]['JAN_bgl']

    may_rise = result.iloc[0]['MAY_flu']
    aug_rise = result.iloc[0]['AUG_flu']
    nov_rise = result.iloc[0]['NOV_flu']
    jan_rise = result.iloc[0]['JAN_flu']

    if sum ( [ may_rise , aug_rise , nov_rise , jan_rise ] ) < 0:
        print ( "Well cannot be constructed." )
    else:
        print ( "Well can be constructed." )  

else:
    print ( "Oops Village not found." )
