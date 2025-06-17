import numpy as np 
import pandas as pd 

'''
Import the data into Python environment as a Pandas DataFrame.
Check for missing values, if any and drop the corresponding rows.
Find the district that gets the highest annual rainfall.
Display the top 5 states that get the highest annual rainfall.
Drop the columns 'Jan-Feb', 'Mar-May', 'Jun-Sep', 'Oct-Dec'.
Display the state-wise mean rainfall for all the months using a pivot table.
Display the count of districts in each state.
For each state, display the district that gets the highest rainfall in May. Also display the recorded rainfall.
'''

rainfall_df = pd.read_csv('/Users/kaipatel/Documents/GitHub/Python-for-Data-Science-Course/rainfall1627650742214.csv')
print(rainfall_df)
rainfall_df.dropna(inplace=True)

max_annual_rainfall = rainfall_df['ANNUAL'].max()
print(max_annual_rainfall)
district_with_max_rainfall = rainfall_df.loc[rainfall_df['ANNUAL'] == max_annual_rainfall, 'DISTRICT'].values[0]
print(district_with_max_rainfall)

top_5_states = rainfall_df.groupby('STATE_UT_NAME')['ANNUAL'].sum().nlargest(5)
print(top_5_states)

drop_columns = rainfall_df.drop(columns=['Jan-Feb', 'Mar-May', 'Jun-Sep', 'Oct-Dec'])
print(drop_columns)

state_wise_mean_rainfall = rainfall_df.pivot_table(
    values=['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
    index='STATE_UT_NAME',
    aggfunc='mean'
)
print(state_wise_mean_rainfall)

district_count_per_state = rainfall_df['STATE_UT_NAME'].value_counts()
print(district_count_per_state)

highest_may_rainfall = rainfall_df.loc[rainfall_df['MAY'].idxmax(), ['STATE_UT_NAME', 'DISTRICT', 'MAY']]
print(highest_may_rainfall)