import pandas as pd
sales=pd.read_csv('sales_subset.csv')

# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Get proportion of sales at each store
sales_propn_by_type = sales_by_type / sum(sales_by_type)
print(sales_propn_by_type)