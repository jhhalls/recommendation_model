# import the libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import warnings
import missingno as msno 
import pandas_profiling
from sklearn.preprocessing import LabelEncoder
import gc
import datetime
%matplotlib inline
color = sns.color_palette()
# current version of seaborn generates a bunch of warnings that we'll ignore
warnings.filterwarnings('ignore')
sns.set_style('whitegrid')


# import the data with correct encoding
data = pd.read_csv('data.csv', encoding='unicode_escape')


# columns to lowercase
data.columns = map(str.lower, data.columns)

# change format of invoice date to timestamp
data['invoicedate'] = pd.to_datetime(data.invoicedate, format = '%m/%d/%Y %H:%M')

# change format of description to lowercase
data['description'] = data.description.str.lower()

# change format of customerid to integer
df['customerid'].astype('int64')


# rows with missing values
data[data.isnull().any(axis=1)].head()

# number of missing values in each column
data.isnull().sum().sort_values(ascending=False)

# drop the missing values
df = data.dropna()

# remove rows with negative quantity
df[df.quantity<0].drop()


# rearrange columns for easy reference
df = df[['invoiceno', 'invoicedate', 'stockcode', 'description', 'quantity',
         'unitprice', 'total', 'customerid', 'country']]