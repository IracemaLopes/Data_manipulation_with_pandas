# Import pandas using the alias pd
import pandas as pd
df=pd.read_csv("homelessness.csv")

# Select the individuals column
individuals = df["individuals"]

# Print the head of the result
print(individuals.head())