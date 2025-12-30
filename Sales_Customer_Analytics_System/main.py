import pandas as pd

customers = pd.read_csv('customers.csv')
products = pd.read_csv('products.csv')
sales = pd.read_csv('sales.csv')

print(customers)
print(products)
print(sales)

print(customers.head())
print(customers.info())

print(products.describe())

print(sales.shape)
# Handle Missing Values
customers['age'].fillna(customers['age'].mean(),inplace=True)

print(customers)

print(sales.head())

sales['order_date'] = pd.to_datetime(sales['order_date'])
sales['month'] = sales['order_date'].dt.month
sales['year'] = sales['order_date'].dt.year
print(sales)

df = sales.merge(customers, on="customer_id", how="inner") \
          .merge(products, on="product_id", how="inner")




df['total_price'] = df['quantity'] * df['price']
print(df.head())

total_revenue = df['total_price'].sum()

print("Total Revenue : " , total_revenue)

revenue_by_product = df.groupby('product_name')['total_price'].sum()
print(revenue_by_product)
revenue_by_category = df.groupby('category')['total_price'].sum()
print(revenue_by_category)
revenue_by_city = df.groupby('city')['total_price'].sum()
print(revenue_by_city)
high_value_orders= df[df['total_price'] > 20000]
print(high_value_orders)

top_order = df.sort_values('total_price',ascending=False)
print(top_order)

monthly_sales = df.groupby('month')['total_price'].sum()
print(monthly_sales)

df.to_csv("final_sales_report.csv",index=False)
revenue_by_product.to_csv("revenue_by_product.csv")
revenue_by_city.to_csv("revenue_by_city.csv")

monthly_sales.plot(kind="bar", title="Monthly Sales")
