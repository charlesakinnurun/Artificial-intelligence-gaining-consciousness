import pandas as pd
# Load the cleaned data

df = pd.read_csv("datasets/ai_cleaned.csv")

print("Education and Opinion")

education_opinion = df.groupby("Education_Level")["Can_AI_Become_Conscious"].value_counts(normalize=True).unstack(fill_value=0).round(2)
print("Distribution of Opinions of AI consciousness by Education level")
print(education_opinion)