import pandas as pd
temperatures = pd.read_csv("temperatures.csv")

print('Get 23rd row, 2nd column (index 22, 1)')
print(temperatures.iloc[23:2])

print('Use slicing to get the first 5 rows')
print(temperatures.iloc[:6])

print('Use slicing to get columns 3 to 4')
print(temperatures.iloc[:,2:4])

print('Use slicing in both directions at once')
print(temperatures.iloc[0:6,2:5])