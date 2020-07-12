# import the module
import pandas as pd

# load the data
df = pd.read_csv('data.csv', encoding= 'ISO-8859-1')

# map columns to lowercase
df.columns = map(str.lower, df.columns)

# check the countries
countries = list(df['country'].unique())

# 
def countries_csv():
    
    for i, country in enumerate(countries_list):
    #print(i, country)
        
    #Select data for the year
        data = df[df.country == country]
    
    # Write the new DataFrame to a csv file
        filename = str(country) + '.csv'
        print(filename)
        data.to_csv(filename)
