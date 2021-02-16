# -*- coding: utf-8 -*-
"""BCG1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OFClK_KUnaLTfnWG1tKLfQZHdW0gwHNK
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk

from google.colab import drive
drive.mount('/content/drive')

"""# LOAD DATA

"""

data1=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/V INTERN/BCG/ml_case_training_data.csv')
data1

data2=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/V INTERN/BCG/ml_case_training_hist_data.csv')
data2

data2a=data2.groupby(['price_date']).count()
data2a

data3=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/V INTERN/BCG/ml_case_training_output.csv')
data3

"""# MERGE DATA"""

data=pd.merge(data1, data3, how='left')
data

"""# CHECK FOR MISSING VALUE"""

data.info()

"""# CONVERT DATE OBJECT TO DATE TIME"""

data['date_activ']=pd.to_datetime(data['date_activ'])
data['date_end']=pd.to_datetime(data['date_end'])
data['date_first_activ']=pd.to_datetime(data['date_first_activ'])
data['date_modif_prod']=pd.to_datetime(data['date_modif_prod'])
data['date_renewal']=pd.to_datetime(data['date_renewal'])

"""# DROP COLUMNS WITH LITTLE TO NOTHING 'NAN' VALUES"""

data=data.drop(columns=['campaign_disc_ele', 'activity_new'])
data

"""# drop duplicate values"""

data=data.drop(columns=['forecast_base_bill_ele'])

data.info()

"""# GROUP SECOND DATA BY 'ID'"""

data2['id'].value_counts()

"""# DATA DISTRIBUTION & OUTLIERS

"""

data.describe()

"""# TO CHECK FOR OUTLIERS

"""

data.boxplot(column=['cons_12m', 'cons_gas_12m', 'cons_last_month'])

data.boxplot(column=['forecast_base_bill_year'])

data.boxplot(column=['forecast_bill_12m'])

data.boxplot(column=['forecast_cons'])

data.hist()

"""# most of these features have many outliers

# Check for correlations
"""

data.corr()

data2.corr()

