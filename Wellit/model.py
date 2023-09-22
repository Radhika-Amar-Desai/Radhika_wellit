import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

# Load the CSV file into a Pandas DataFrame
# Replace 'your_file.csv' with the path to your CSV file
data = pd.read_csv('FinalData.csv')

# Prompt the user for the village name
user_village_name = input("Enter the village name: ")

# Filter the DataFrame based on the user-provided village name
filtered_data = data[data['VILLAGE'] == user_village_name]

# Check if any rows match the village name
if filtered_data.empty:
    print(f"No data found for village '{user_village_name}'.")
else:
    # Initialize the LabelEncoder
    label_encoder = LabelEncoder()

    # Apply label encoding to the 'FORMATION' and 'River Basin' columns
    filtered_data['FORMATION'] = label_encoder.fit_transform(filtered_data['FORMATION'])
    filtered_data['River Basin'] = label_encoder.fit_transform(filtered_data['River Basin'])
    
    # Select features and target variable
    X = filtered_data[['ELEVATION', 'Normal (1901-70)', 'Average rainfall (2012-21) (mm)',
                       'Rainfall (2021) (mm)', 'Departure (%) in 2021 from normal rainfall',
                       'Departure (%) in 2021 from Average rainfall', 'River Basin', 'FORMATION']]
    
    y_may_flu = filtered_data['MAY_flu']
    y_aug_flu = filtered_data['AUG_flu']
    y_nov_flu = filtered_data['NOV_flu']
    y_jan_flu = filtered_data['JAN_flu']

    depth = filtered_data['DEPTH']

    y_may_bgl = filtered_data['MAY_bgl']
    y_aug_bgl = filtered_data['AUG_bgl']
    y_nov_bgl = filtered_data['NOV_bgl']
    y_jan_bgl = filtered_data['JAN_bgl']    

    # Create a linear regression model
    model = LinearRegression()

    # Fit the model to the data
    model.fit(X, y_may_flu)
    model.fit(X, y_aug_flu)
    model.fit(X, y_nov_flu)
    model.fit(X, y_jan_flu)

    # Make predictions
    predictions_may_flu = model.predict(X)
    predictions_aug_flu = model.predict(X)
    predictions_nov_flu = model.predict(X)
    predictions_jan_flu = model.predict(X)

    avg_flu = ( predictions_may_flu + predictions_aug_flu + predictions_nov_flu + predictions_jan_flu ) / 4

    if ( avg_flu >= 0 ):
        print ( "Well can be constructed." )
        print ( "The fluctuation in Pre-Monsoon period (May) is " , y_may_flu , " The water will be found " , y_may_bgl , " meters below the ground water ( roughly ).")
        print ( "The fluctuation during Monsoon period (August) is " , y_aug_flu , " The water will be found " , y_aug_bgl , " meters below the ground water ( roughly ).")
        print ( "The fluctuation in Post-Monsoon period (November) is ", y_nov_flu , " The water will be found " , y_nov_bgl , " meters below the ground water ( roughly ).")
        print ( "The fluctuation in Irrigation period (January) is ", y_jan_flu , " The water will be found " , y_jan_bgl , " meters below the ground water ( roughly ).")
        print ( "Depth of the well should be ", depth )
    else:
        print ( "Well can't be constructed." )
