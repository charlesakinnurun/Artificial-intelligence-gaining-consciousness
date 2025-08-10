import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/ai_cleaned.csv")

print("Rights and Gender")

rights_gender = pd.crosstab(df["Gender"],df["Should_It_Have_Rights"],normalize="index").round(2)
print("'Percentage of responses of AI having rights, by gender")
print(rights_gender)