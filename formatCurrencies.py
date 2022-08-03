import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('data/data.csv')
# Get only the REF_DATE, Type of currency, and the value of the currency
data = data[['REF_DATE', 'Type of currency', 'VALUE']]
# Rename the columns
data.columns = ['Date', 'Currency', 'Value']
# Convert the date to a datetime object
data['Date'] = pd.to_datetime(data['Date'])
# Remove entries of value where it is Nan
data = data[data['Value'].notnull()]
# Split the data into frames, one for each currency     
data_gb = data.groupby('Currency')
# Put each frame into a csv
for name, group in data_gb:
    group.to_csv(f'data/{name}.csv')

