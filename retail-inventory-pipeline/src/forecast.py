import pandas as pd
from sklearn.linear_model import LinearRegression


def forecast_demand(df: pd.DataFrame):
    df['day'] = df['sale_date'].dt.dayofyear
    X = df[['day']]
    y = df['quantity']

    model = LinearRegression()
    model.fit(X, y)

    future_days = pd.DataFrame({'day': range(df['day'].max()+1, df['day'].max()+31)})
    predictions = model.predict(future_days)

    return predictions


if __name__ == "__main__":
    df = pd.read_csv("data/sample_sales.csv")
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    preds = forecast_demand(df)
    print(preds[:10])
