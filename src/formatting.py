# import the module
import pandas as pd

# load the data
df = pd.read_csv('data.csv', encoding='unicode_escape')

# dataframe of rows with atleast one missing values
null = pd.DataFramedata([data.isnull().any(axis=1)])

# save the null dataframe
null.to_csv('../data/missing_values.csv')

## check for null values
df.isnull().sum().sort_values(ascending=False)

## drop the rows with missing values
df = df.dropna()

# formatting
### convert columns to lowercase
data.columns = map(str.lower, data.columns)

### change te invoice date format from str to timestamp
data['invoicedate'] = pd.to_datetime(data.invoicedate, format = '%m/%d/%Y %H:%M')

### change the columns from float to integer
df['customerid'].astype(int)

### change description of products to lowercase
data['description'] = data.description.str.lower()

### rearrange columns for easy reference
df = df[['invoiceno', 'invoicedate', 'stockcode', 'description', 'quantity',
         'unitprice', 'total', 'customerid', 'country']]

