import pandas as pd
def analyse_sales(file_path="data/sales.csv"):
  """load the sales data  and calculate revenue metrics"""
  df = pd.read_csv(file_path)
  required_columns = {'date','product','category','quantity','price'}


  if not required_columns.issubset(df.columns):
    raise ValueError("data is not correctly formatted. missing required columns.")

  df['date'] = pd.to_datetime(df['date'],errors='coerce')
  df['revenue'] = df['quantity'] * df['price']

  total_revenue = df['revenue'].sum()
  product_revenue = (df.groupby('product')['revenue'].sum().sort_values(ascending=False))

  return df, total_revenue, product_revenue

if __name__ == "__main__":
  df, total_revenue, product_revenue = analyse_sales()
  print(f"Total Revenue: {total_revenue}")
  print("Revenue by Product:")
  print(product_revenue)



   