import pandas as pd

# Load the dataset
df = pd.read_csv("datasets/ai_cleaned.csv")

# Sufferability and Threat Perception
print("Sufferability and Threat Perception")
suffer_threat = df.groupby("Can_It_Suffer")["Threat_Assessment"].value_counts(normalize=True).unstack(fill_value=0).round(2)
print("Threat assessment distribution by belief in AIs ability to suffer")
print(suffer_threat)