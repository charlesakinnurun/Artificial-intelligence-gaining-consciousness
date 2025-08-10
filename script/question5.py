import pandas as pd

# Import the cleaned data
df = pd.read_csv("datasets/ai_cleaned.csv")

# Regulation and Education
print("Regulation and Education")
phd_df = df[df["Education_Level"] == "PhD"]
phd_regulate_count = (phd_df["Should_Governments_Regulate"] == "Yes,definitely").sum()
phd_total = len(phd_df)
phd_regulate_percentage = (phd_regulate_count / phd_total) * 100
print(f"Percentage of PhD holders who believe governments should definitely regulate AI: {phd_regulate_percentage:.2f}")