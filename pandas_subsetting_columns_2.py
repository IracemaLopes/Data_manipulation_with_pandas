# Import pandas using the alias pd
import pandas as pd
df=pd.read_csv("homelessness.csv")

# Select the state and family_members columns
state_fam = df[["state","family_members"]]

# Print the head of the result
print(state_fam.head())