import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/ai_cleaned.csv")

# Question 10: Individual Consideration
print("--- Question 10: Individual Consideration ---")
individual_consideration_count = df[df['Should_Be_Considered_Individual'] == 'Yes'].groupby('Education_Level').size()
print("Number of respondents who believe AI should be considered an individual, by education level:\n")
print(individual_consideration_count)