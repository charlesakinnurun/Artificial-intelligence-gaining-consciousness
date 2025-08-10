import pandas as pd

# Load the datasets
df = pd.read_csv("datasets/ai_cleaned.csv")

# Tech Interest vs Knowledge
print("Tech Interest vs Knowledge")
tech_interest_knowledge = pd.crosstab(df["Tech_Interest"],df["AI_Knowledge_Level"],normalize="index").round(2)
print("Relationship between Tech Interest and AI Knowledge Level (row percentages):\n")
print(tech_interest_knowledge.head())
