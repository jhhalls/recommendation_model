"""
@author : jhhalls
"""


# import the libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori, association_rules

# read the dataset with correct encoding

df = pd.read_csv('data.csv', encoding='ISO-8859-1')

# have a peak into the dataframe

df.head()

#  check the basic format of the dataframe

df.shape                               #shape
df.size                                #size
df.columns                             #see the columns
df.describe()                          # describe the data
df.info()                              # basic information


#### Preprocess the data

#  features to lowercase
df.columns = map(str.lower, df.columns)                    

# remove the whitespaces from the description
df['description'] = df['description'].str.strip()

# drop the rows with missing invoice number
df.dropna(axis=0, subset = ['invoiceno'], inplace=True)    

# change the format of invoice number from integer to string
df['invoiceno']  = df['invoiceno'].astype('str')           

# drop the rowd with C in their invoice number   (cancelled orders)
df = df[-df['invoiceno'].str.contains('C')]                


# make basket with frequency for any item in each purchase in France
#  similar filtraion can be used for other countries or any other parameter

basket = (df[df['country'] == 'France']                              # select the country = France
         .groupby(['invoiceno', 'description'])['quantity']          # group the selected data by invoice number and description of the product
         .sum().unstack().reset_index().fillna(0)                    # sum the quantity of each description, reset index  and fill missing values with 0
         .set_index('invoiceno'))                                    #set index as invoice number

# check the basket
basket


# define a function to encode the frequency

def encode_units(x):
    if x<=0:                       #encode values <=0 as 0
        return 0
    if x>=1:                       # encode values >=1 as 1
        return 1

    
##encode the basket    
baskets_sets  = basket.applymap(encode_units)         

# drop the postage column
baskets_sets.drop('POSTAGE',axis=1, inplace = True)    

# check the basket set dataframe
baskets_sets                                           

# any two items brought together with with a  supprt of atleast 7%  
frequent_itemsets = apriori(baskets_sets, min_support=0.07, use_colnames=True)        

# generating rules with corresponding support, confidence and lift
rules = association_rules(frequent_itemsets, metric='lift',min_threshold=1)     

# check the rules
rules.head()


# filter the rules with large lift(6) and high confidence (0.8)

rules[ (rules['lift'] >= 6) &
       (rules['confidence'] >= 0.8) ]


# make insights using statistical knowledge
# At this point, you may want to look at how much opportunity there is to use the popularity of one product to drive sales of another



#### lets check rules for the same for Germany

# make the basket
basket2 = (df[df['Country'] =="Germany"]
          .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))

# encode the frequency
basket_sets2 = basket2.applymap(encode_units)        

# drop the postage column
basket_sets2.drop('POSTAGE', inplace=True, axis=1)

# any two items brought together with with a  support of atleast 5%  
frequent_itemsets2 = apriori(basket_sets2, min_support=0.05, use_colnames=True)

# generate the rules
rules2 = association_rules(frequent_itemsets2, metric="lift", min_threshold=1)

# filter the rules with moderate lift (4) and moderate confidence(0.5)
rules2[ (rules2['lift'] >= 4) &
        (rules2['confidence'] >= 0.5)]




