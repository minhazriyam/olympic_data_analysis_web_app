import pandas as pd

def preprocess(df,region_df):


    df = df[df['Season'] == 'Summer']

    df = df.merge(region_df, on='NOC', how='left')

    df.drop_duplicates(inplace=True)

    medal_df = pd.get_dummies(df['Medal'])
    df = pd.concat([df, medal_df], axis=1)

    return df