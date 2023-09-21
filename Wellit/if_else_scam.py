import pandas as pd

# Define the name you want to search for
search_name = "DASUK"

# Load the CSV file into a DataFrame
file_path = "SIH - Sheet1.csv"  # Replace with the actual file path
df = pd.read_csv(file_path)

# Search for the name in the "village" column
result = df[df['Village'] == search_name]

# Check if any matches were found
if not result.empty:
    # Assuming the depth column is named "depth," you can change this if needed
    depth_value = result.iloc[0]['Depth']

    may_decade_bgl = result.iloc[0]['May_decade_bgl']
    aug_decade_bgl = result.iloc[0]['Aug_decade_bgl']
    nov_decade_bgl = result.iloc[0]['Nov_decade_bgl']
    jan_decade_bgl = result.iloc[0]['Jan_decade_bgl']

    may_bgl = result.iloc[0]['May_bgl']
    aug_bgl = result.iloc[0]['Aug_bgl']
    nov_bgl = result.iloc[0]['Nov_bgl']
    jan_bgl = result.iloc[0]['Jan_bgl']

    may_rise = result.iloc[0]['May_rise']
    aug_rise = result.iloc[0]['Aug_rise']
    nov_rise = result.iloc[0]['Nov_rise']
    jan_rise = result.iloc[0]['Jan_rise']

else:
    print(f"No entry found for {search_name} in the 'village' column.")
