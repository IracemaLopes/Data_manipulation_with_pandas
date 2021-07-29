# Import pandas using the alias pd
import pandas as pd

df=pd.read_csv("homelessness.csv")

# Sort homelessness by individual
homelessness_ind = df.sort_values("individuals")

# Print the top few rows
print(homelessness_ind.head())