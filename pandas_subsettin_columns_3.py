# Import pandas using the alias pd
import pandas as pd
df=pd.read_csv("homelessness.csv")

# Select only the individuals and state columns, in that order
ind_state = df[["individuals","state"]]

# Print the head of the result
print(ind_state.head())