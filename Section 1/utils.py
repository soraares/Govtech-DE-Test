import sys
import pandas as pd

def munge_data(filename = 'dataset.csv'):
    df = pd.read_csv(filename)

    df = df[(pd.notna(df['name'])) | ~ (df['name'] == '')]
    df['last_name'] = df['name']
    df.rename(columns = {'name': 'first_name'}, inplace = True)
    df['first_name'] = df['first_name'].apply(lambda x: x.split(' ')[0])
    df['last_name'] = df['last_name'].apply(lambda x: x.split(' ')[1])
    df = df[['first_name', 'last_name', 'price']]

    df['price'] = df['price'].apply(str)
    df['price'] = df['price'].apply(lambda x: x.lstrip('0'))
    df['price'] = df['price'].apply(float)
    df['above_100'] = df['price'].apply(lambda x: x > 100)

    df.to_csv(f'new_{filename}', index = False)