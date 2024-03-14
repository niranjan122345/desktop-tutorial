#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing  import OneHotEncoder,StandardScaler
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from joblib import dump, load
from sklearn.metrics import r2_score

def evaluvation_pipeline(x_test_path,y_test_path,model):

    #Read data
    X=pd.read_csv(x_test_path)
    y_true=pd.read_csv(y_test_path)
    
    #seperate numerical and categorical columns
    numerical_cols=X.select_dtypes(exclude='object')
    categorical_cols=X.select_dtypes(include='object')
    
    # categorical -- encoding
    encoder_model=load('models/encoder/one_hot_encoder.pkl')
    col=encoder_model.get_feature_names_out()
    transform=encoder_model.transform(categorical_cols).toarray()
    categorical_encode_data=pd.DataFrame(transform,columns=col)

    # numerical-- Scalling
    model_scaling=load('models/scaling/standard_scaler.pkl')
    scaled_data=model_scaling.transform(numerical_cols)
    numerical_scaled_data=pd.DataFrame(scaled_data,columns=numerical_cols.columns)

    # concat numerical and categorical data
    Features=pd.concat([numerical_scaled_data,categorical_encode_data],axis=1)

    # model testing
    lr=load(model)
    y_pred=pd.DataFrame(lr.predict(Features))
    test_score=r2_score(y_true, y_pred)*100
    
    return y_pred,test_score

