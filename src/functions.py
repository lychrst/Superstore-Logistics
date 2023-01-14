import pandas as pd
import statsmodels.api as sm
import numpy as np
super_explore =  pd.read_csv('superstore.csv', encoding = 'unicode_escape')

def Central_to_South(df):
    '''Determines which products need to be shipped from the 
       Central Warehouse to the South Warehouse
    Parameters
    ----------
    df: dataframe 
    The specific dataset(s) being queried.
    
    Returns 
    -------
    Central_to_South: dataset
    The specific orders that need to be shipped from the Central warehouse to the Southern Warehouse.
    '''
    df1 = df[df['Region'] == 'South']
    
    Central_to_South = df1[(df1["Sub-Category"] == 'Paper') | (df1["Sub-Category"] == 'Storage') \
| (df1["Sub-Category"] == 'Tables') | (df1["Sub-Category"] == 'Machines')]
    return Central_to_South

def East_to_South(df):
    '''Determines which products need to be shipped from the 
       East Warehouse to the South Warehouse
    Parameters
    ----------
    df: dataframe 
    The specific dataset(s) being queried.
    
    Returns 
    -------
    East_to_South: dataset
    The specific orders that need to be shipped from the East warehouse to the Southern Warehouse.
    '''
    df1 = df[df['Region'] == 'South']
    
    East_to_South = df1[(df1["Sub-Category"] == 'Phones') | (df1["Sub-Category"] == 'Chairs') \
| (df1["Sub-Category"] == 'Labels') | (df1["Sub-Category"] == 'Supplies')]
    return East_to_South

def West_to_South(df):
    '''Determines which products need to be shipped from the 
       West Warehouse to the South Warehouse
    Parameters
    ----------
    df: dataframe 
    The specific dataset(s) being queried.
    
    Returns 
    -------
    West_to_South: dataset
    The specific orders that need to be shipped from the West warehouse to the Southern Warehouse.
    '''
    df1 = df[df['Region'] == 'South']
    
    West_to_South = df1[(df1["Sub-Category"] == 'Furnishings') | (df1["Sub-Category"] == 'Art') \
| (df1["Sub-Category"] == 'Appliances') | (df1["Sub-Category"] == 'Bookcases') | (df1["Sub-Category"] == 'Fasteners')]
    return West_to_South


def South_to_Central(df):
    '''Determines which products need to be shipped from the 
       South Warehouse to the Central Warehouse
    Parameters
    ----------
    df: dataframe 
    The specific dataset(s) being queried.
    
    Returns 
    -------
    South_to_Central: dataset
    The specific orders that need to be shipped from the Southern warehouse to the Central Warehouse.
    '''
    df1 = df[df['Region'] == 'Central']
    
    South_to_Central = df1[(df1["Sub-Category"] == 'Copiers') | (df1["Sub-Category"] == 'Envelopes') \
| (df1["Sub-Category"] == 'Accessories') | (df1["Sub-Category"] == 'Binders')]
    return South_to_Central


def East_to_Central(df):
    '''Determines which products need to be shipped from the 
       East Warehouse to the Central Warehouse
    Parameters
    ----------
    df: dataframe 
    The specific dataset(s) being queried.
    
    Returns 
    -------
    East_to_Central: dataset
    The specific orders that need to be shipped from the East warehouse to the Central Warehouse.
    '''
    df1 = df[df['Region'] == 'Central']
    
    East_to_Central =  df1[(df1["Sub-Category"] == 'Phones') | (df1["Sub-Category"] == 'Chairs') \
| (df1["Sub-Category"] == 'Labels') | (df1["Sub-Category"] == 'Supplies')]
    return East_to_Central

def West_to_Central(df):
    '''Determines which products need to be shipped from the 
       West Warehouse to the Central Warehouse
    Parameters
    ----------
    df: dataframe 
    The specific dataset(s) being queried.
    
    Returns 
    -------
    West_to_Central: dataset
    The specific orders that need to be shipped from the West warehouse to the Central Warehouse.
    '''
    df1 = df[df['Region'] == 'Central']
    
    West_to_Central = df1[(df1["Sub-Category"] == 'Furnishings') | (df1["Sub-Category"] == 'Art') \
| (df1["Sub-Category"] == 'Appliances') | (df1["Sub-Category"] == 'Bookcases') | (df1["Sub-Category"] == 'Fasteners')]
    return West_to_Central 


def South_to_East(df):
    '''Determines which products need to be shipped from the 
       Southern Warehouse to the Eastern Warehouse
    Parameters
    ----------
    df: dataframe 
    The specific dataset(s) being queried.
    
    Returns 
    -------
    South_to_East: dataset
    The specific orders that need to be shipped from the Southern warehouse to the Eastern Warehouse.
    '''
    df1 = df[df['Region'] == 'East']
    
    South_to_East = df1[(df1["Sub-Category"] == 'Copiers') | (df1["Sub-Category"] == 'Envelopes') \
| (df1["Sub-Category"] == 'Accessories') | (df1["Sub-Category"] == 'Binders')]
    return South_to_East

def Central_to_East(df):
    '''Determines which products need to be shipped from the 
       Central Warehouse to the Eastern Warehouse
    Parameters
    ----------
    df: dataframe 
    The specific dataset(s) being queried.
    
    Returns 
    -------
    Central_to_East: dataset
    The specific orders that need to be shipped from the Central warehouse to the Eastern Warehouse.
    '''
    df1 = df[df['Region'] == 'East']
    
    Central_to_East = df1[(df1["Sub-Category"] == 'Paper') | (df1["Sub-Category"] == 'Storage') \
| (df1["Sub-Category"] == 'Tables') | (df1["Sub-Category"] == 'Machines')]
    return Central_to_East


def West_to_East(df):
    '''Determines which products need to be shipped from the 
       Western Warehouse to the Eastern Warehouse
    Parameters
    ----------
    df: dataframe 
    The specific dataset(s) being queried.
    
    Returns 
    -------
    West_to_Central: dataset
    The specific orders that need to be shipped from the West warehouse to the East Warehouse.
    '''
    df1 = df[df['Region'] == 'East']
    
    West_to_East = df1[(df1["Sub-Category"] == 'Furnishings') | (df1["Sub-Category"] == 'Art') \
| (df1["Sub-Category"] == 'Appliances') | (df1["Sub-Category"] == 'Bookcases') | (df1["Sub-Category"] == 'Fasteners')]
    return West_to_East


def South_to_West(df):
    '''Determines which products need to be shipped from the 
       Southern Warehouse to the Western Warehouse
    Parameters
    ----------
    df: dataframe 
    The specific dataset(s) being queried.
    
    Returns 
    -------
    South_to_West: dataset
    The specific orders that need to be shipped from the Southern warehouse to the Western Warehouse.
    '''
    df1 = df[df['Region'] == 'West']
    
    South_to_West = df1[(df1["Sub-Category"] == 'Copiers') | (df1["Sub-Category"] == 'Envelopes') \
| (df1["Sub-Category"] == 'Accessories') | (df1["Sub-Category"] == 'Binders')]
    return South_to_West

def Central_to_West(df):
    '''Determines which products need to be shipped from the 
       Central Warehouse to the Western Warehouse
    Parameters
    ----------
    df: dataframe 
    The specific dataset(s) being queried.
    
    Returns 
    -------
    Central_to_West: dataset
    The specific orders that need to be shipped from the Central warehouse to the Western Warehouse.
    '''
    df1 = df[df['Region'] == 'West']
    
    Central_to_West = df1[(df1["Sub-Category"] == 'Paper') | (df1["Sub-Category"] == 'Storage') \
| (df1["Sub-Category"] == 'Tables') | (df1["Sub-Category"] == 'Machines')]
    return Central_to_West

def East_to_West(df):
    '''Determines which products need to be shipped from the 
       East Warehouse to the Western Warehouse
    Parameters
    ----------
    df: dataframe 
    The specific dataset(s) being queried.
    
    Returns 
    -------
    East_to_West: dataset
    The specific orders that need to be shipped from the Eastern warehouse to the Western Warehouse.
    '''
    df1 = df[df['Region'] == 'West']
    
    East_to_West =  df1[(df1["Sub-Category"] == 'Phones') | (df1["Sub-Category"] == 'Chairs') \
| (df1["Sub-Category"] == 'Labels') | (df1["Sub-Category"] == 'Supplies')]
    return East_to_West


def random_customer_orders(dataframe, seed, loc, scale, size1, size2, low, high):
    np.random.default_rng(seed)
    rncos = np.random.normal(loc = loc, scale = scale, size = (size1, size2)).tolist()
    rnco = rncos[0]
    rncoi= ([int(a) for a in rnco])
    df = pd.DataFrame()
    start = 0
    for i in range(1, len(rncoi) + 1):
        end = start + rncoi[i - 1]
        df_temp = pd.DataFrame({'Day': [i] * rncoi[i - 1]})
        df = pd.concat([df, df_temp], ignore_index=True)
        df['orders'] = np.random.randint(low, high, size=len(df)) 
        merged_df = pd.merge(df, dataframe, left_on = "orders", right_on= "Row ID")
    return merged_df

