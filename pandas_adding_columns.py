# Import pandas using the alias pd
import pandas as pd
df=pd.read_csv("homelessness.csv")

# Add total col as sum of individuals and family_members
df["total"]=df["individuals"] + df["family_members"]

# Add p_individuals col as proportion of individuals
df["p_individuals"]=df["individuals"]/df["total"]

# See the result
print(df)