#!/usr/bin/env python
# coding: utf-8

# In[159]:


# ignore warnings
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split
from env import host, user, password


# In[160]:


def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    It takes in a string name of a database as an argument.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# In[161]:


def new_telco_data():
    '''
    This function reads the telco data from the Codeup db into a df.
    '''
    sql_query = """
                select * from customers
                join contract_types using (contract_type_id)
                join internet_service_types using (internet_service_type_id)
                join payment_types using (payment_type_id)
                """
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    
    return df


# In[164]:


def clean_prep_telco(raw_telco):
    pruned_telco = raw_telco.drop(columns = ['customer_id', 'payment_type_id', 'internet_service_type_id', 'contract_type_id', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing'])
    # For our purposes, Mailed Check/Electronic Check and Automatic Bank Transfer/Automatic Credit Card payments
    # are close enough that we will group them together for further analysis
    for i in range(len(pruned_telco)):
        if pruned_telco.contract_type[i] == 'One year':
            pruned_telco.contract_type[i] = 'contract'
        elif pruned_telco.contract_type[i] == 'Two year':
            pruned_telco.contract_type[i] = 'contract'
        elif pruned_telco.contract_type[i] == 'Month-to-month':
            pruned_telco.contract_type[i] = 'no_contract'
        else:
            print("Cmon man, what are we even doing here.")
    
        if pruned_telco.payment_type[i] == 'Bank transfer (automatic)':
            pruned_telco.payment_type[i] = "auto_payment"
        elif pruned_telco.payment_type[i] == 'Credit card (automatic)':
            pruned_telco.payment_type[i] = "auto_payment"
        elif pruned_telco.payment_type[i] == 'Electronic check':
            pruned_telco.payment_type[i] = "manual_payment"
        elif pruned_telco.payment_type[i] == 'Mailed check':
            pruned_telco.payment_type[i] = "manual_payment"
        else:
            print("There is a glitch in the matrix.")
        
        if pruned_telco.partner[i] == 'No':
            pruned_telco.partner[i] = 0
        elif pruned_telco.partner[i] == 'Yes':
            pruned_telco.partner[i] = 1
        else:
            print("Cmon man, what are we even doing here.")  
        
        if pruned_telco.internet_service_type[i] == 'Fiber optic':
            pruned_telco.internet_service_type[i] = "Fiber"
            
    
    # Setup dummy variables
    dummy_telco = pd.get_dummies(pruned_telco[['gender', 'dependents', 'phone_service', 'contract_type', 'internet_service_type', 'payment_type']], dummy_na=False, drop_first=True)
    
    # Merge dummy variables, drop variables that are no redundant
    wrangled_telco = pd.concat([pruned_telco, dummy_telco], axis=1)
    wrangled_telco = wrangled_telco.drop(columns=['gender', 'dependents', 'phone_service', 'contract_type', 'internet_service_type', 'payment_type'])
    
    # Split into train, validate, test
    train_validate, test = train_test_split(wrangled_telco, test_size=0.2, 
                                            random_state=123, 
                                            stratify=wrangled_telco['churn'])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=123,
                                       stratify=train_validate['churn'])
    
    return wrangled_telco, train, validate, test
    


# In[ ]:




