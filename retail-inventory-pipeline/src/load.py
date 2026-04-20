import psycopg2
import pandas as pd


def load_to_db(df: pd.DataFrame):
    conn = psycopg2.connect(
        dbname="your_db",
        user="your_user",
        password="your_password",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute(
            "INSERT INTO sales (product_id, quantity, price, sale_date) VALUES (%s, %s, %s, %s)",
            (row['product_id'], row['quantity'], row['price'], row['sale_date'])
        )

    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    df = pd.read_csv("data/sample_sales.csv")
    load_to_db(df)
