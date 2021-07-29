# Import pandas using the alias pd
import pandas as pd
df=pd.read_csv("homelessness.csv")

# Filter for rows where region is Mountain
mountain_reg = df[df["region"]=="Mountain"]

# See the result
print(mountain_reg)