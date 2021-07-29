# Import pandas using the alias pd
import pandas as pd
df=pd.read_csv("homelessness.csv")
# Filter for rows where family_members is less than 1000
# and region is Pacific
fam_lt_1k_pac = df[(df["family_members"]<1000)& (df["region"]=="Pacific")]

# See the result
print(fam_lt_1k_pac)