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


def high_middle_low(df, day):
    high = len(df[(df["Ship Mode"] == "First Class") & (df["Day"] == day)]) +\
           len(df[(df["Ship Mode"] == "Same Day") & (df["Day"] == day)])
    middle = len(df[(df["Ship Mode"] == "Second Class") & (df["Day"] == day)])
    low = len(df[(df["Ship Mode"] == "Standard Class") & (df["Day"] == day)])
    return pd.DataFrame({'high': [high], 'middle': [middle], 'low': [low]})

def combined_df(dest1, day, loads, dest1a):
    df1 = high_middle_low(dest1, day)
    df1['sent_units'] = loads[dest1a][day -1]
    return df1

def remainder(df):
    from pandasql import sqldf
    # Use pandasql to join the two dataframes
    query = '''
    SELECT
        df.high,
        df.middle,
        df.low,
        df.sent_units,
        CASE
            WHEN df.high > df.sent_units THEN df.high - df.sent_units
            WHEN df.high + df.middle > df.sent_units THEN  df.high + df.middle - df.sent_units
            ELSE df.high + df.middle + df.low - df.sent_units
        END AS remainder
    FROM
        df
    '''
    df_result = sqldf(query)

    #create a new column indicating the remainder is high, middle or low 
    df_result['remainder_type'] = np.where(df.high > df.sent_units, 'high',
                                      np.where(df.high + df.middle > df.sent_units, 'middle',
                                               np.where(df.high + df.middle + df.low - df.sent_units > 0, 'low', 'other')))

    return df_result


def new_remainder_type(df):
    new_df = pd.DataFrame()
    new_df['new_high'] = df.loc[df['remainder_type'] == 'high', 'remainder']
    new_df['new_middle'] = df.loc[df['remainder_type'] == 'middle', 'remainder']
    new_df['new_low'] = df.loc[df['remainder_type'] == 'low', 'remainder']
    new_df['middleqqq'] = df['middle']
    new_df['lowqqq'] = df['low']
    new_df = new_df.fillna(0)
    return new_df




def create_new_df(df1, df2):
    from pandasql import sqldf
    pysqldf = lambda q: sqldf(q, globals())
    
    query = """
    SELECT 
        CASE
            WHEN df1.new_high > 0 THEN df1.new_high + df2.high
            ELSE df2.high
        END AS high,
        CASE
            WHEN df1.new_high > 0 THEN df1.middleqqq + df2.middle
            WHEN df1.new_middle > 0 THEN df1.new_middle + df2.middle
            ELSE df2.middle
        END AS middle,
        CASE
            WHEN df1.new_high > 0 THEN df1.lowqqq + df2.low
            WHEN df1.new_middle > 0 THEN df1.lowqqq + df2.low
            WHEN df1.new_low > 0 THEN df1.new_low + df2.low
            ELSE df2.low
        END AS low
    FROM 
        df1
    JOIN 
        df2
    """
    df3 = pysqldf(query)
    return df3








