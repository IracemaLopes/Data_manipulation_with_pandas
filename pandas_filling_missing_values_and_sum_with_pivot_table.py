import pandas as pd
sales=pd.read_csv("sales_subset.csv")

# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0))