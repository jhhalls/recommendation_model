# import the modules
import pandas as pd

# load the data
df = pd.read_csv('.../data/original/data.csv', encoding='unicode_escape')


# Basic Information

### info
data.info()

### Describe
data.describe()


# Feature Engineering

## Add Columns

# method-1
###  'total amount'
df['total'] = df['quantity']*df['unitprice']

# method-2
###  monthyear
df.insert(loc=2, column='year_month', value=df['invoicedate'].map(lambda x: 100*x.year + x.month))

### Month of the year - 12 months a year
df.insert(loc=3, column='month', value = df['invoicedate'].map(lambda x: x.month))

### Day of week - 7 days
df.insert(loc=4, column='day', value= df['invoicedate'].map(lambda x: x.dayofweek +1))

### Hour - 24 hours
df.insert(loc=5, column='hour', value= df['invoicedate'].map(lambda x: x.hour))

### Week - 52 weeks a year
df.insert(loc=5, column='week', value= df['invoicedate'].map(lambda x: x.strftime('%W')))

### Date of Month - 31 dates
df.insert(loc=5, column='date_of_month', value = df['invoicedate'].map(lambda x: x.day))

# save the preprocessed csv
df.to_csv('ecommerce_preprocessed.csv')