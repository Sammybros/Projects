import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    df['total_value'] = df['quantity'] * df['price']
    return df


if __name__ == "__main__":
    df = pd.read_csv("data/sample_sales.csv")
    df = transform_data(df)
    print(df.head())
