import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/ai_cleaned.csv")

print("Age and Threat Perception")

threat_groups = df.groupby("Threat_Assessment")["Age"].mean().round(2)
print("Average age of AI threat assessment")
print(threat_groups.head())