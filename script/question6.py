import pandas as pd

# Import the cleaned data
df = pd.read_csv("datasets/ai_cleaned.csv")

# Working Comfort and Consciousness Belief
print("Working Comfort and Consciousness Belief")
yes_conscious_df = df[df["Can_AI_Become_Conscious"] == "Yes"]
most_common_comfort = yes_conscious_df["Working_Comfort"].mode()[0]

print(f"Among those who believe AI can become conscious, the most common 'Working_Comfort' response is: {most_common_comfort}")
