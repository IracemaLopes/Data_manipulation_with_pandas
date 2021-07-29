# Import pandas using the alias pd
import pandas as pd
df=pd.read_csv("homelessness.csv")

# Create indiv_per_10k col as homeless individuals per 10k state pop
df["indiv_per_10k"] = 10000 * df["individuals"] / df["state_pop"]

# Subset rows for indiv_per_10k greater than 20
high_homelessness = df[df["indiv_per_10k"]>20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[["state","indiv_per_10k"]]

# See the result
print(result)