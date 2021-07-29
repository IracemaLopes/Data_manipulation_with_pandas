# Import pandas using the alias pd
import pandas as pd

df=pd.read_csv("homelessness.csv")
# Sort homelessness by descending family members
homelessness_fam = df.sort_values("family_members", ascending=False)

# Print the top few rows
print(homelessness_fam.head())