# Import pandas using the alias pd
import pandas as pd
df=pd.read_csv("homelessness.csv")

# Filter for rows where individuals is greater than 10000
ind_gt_10k = df[df["individuals"]>10000]

# See the result
print(ind_gt_10k)