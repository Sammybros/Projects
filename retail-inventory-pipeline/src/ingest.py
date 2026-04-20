import pandas as pd


def ingest_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df


if __name__ == "__main__":
    df = ingest_data("data/sample_sales.csv")
    print(df.head())
