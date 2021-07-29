# Import pandas using the alias pd
import pandas as pd
df=pd.read_csv("homelessness.csv")

# Sort homelessness by region, then descending family members
homelessness_reg_fam = df.sort_values(["region","family_members"], ascending=[True,False])

# Print the top few rows
print(homelessness_reg_fam.head())