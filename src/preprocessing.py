import pandas as pd


def load_data(path):
    df = pd.read_csv(path, encoding='latin-1')
    return df


def clean_data(df):

    df.drop_duplicates(inplace=True)

    df.columns = df.columns.str.strip()

    df['Order Date'] = pd.to_datetime(
        df['Order Date'],
        dayfirst=True
    )

    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.strftime('%b')

    return df