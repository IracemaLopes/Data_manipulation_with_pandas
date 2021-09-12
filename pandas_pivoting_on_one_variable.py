import pandas as pd
import numpy as np
sales=pd.read_csv("sales_subset.csv")

print('Pivot for mean weekly_sales for each store type')
mean_sales_by_type = sales.pivot_table(values="weekly_sales", index="type")

print('print mean_sales_by_type')
print(mean_sales_by_type)

print('Pivot for mean and median weekly_sales for each store type')
mean_med_sales_by_type = sales.pivot_table(values="weekly_sales", index="type", aggfunc=[np.mean,np.median])

print('Print mean_med_sales_by_type')
print(mean_med_sales_by_type)

print('Pivot for mean weekly_sales by store type and holiday')
mean_sales_by_type_holiday = sales.pivot_table(values="weekly_sales", index="type", columns="is_holiday")

print('Print mean_sales_by_type_holiday')
print(mean_sales_by_type_holiday)