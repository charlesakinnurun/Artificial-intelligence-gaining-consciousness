import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/ai_cleaned.csv")

# Knowledge and Consciousness
print("Knowledge and Consciousness")
expert_df = df[df["AI_Knowledge_Level"] == "I am an  expert"]
expert_yes_conscious_count = (expert_df["Can_AI_Become_Conscious"] == "Yes").sum()
expert_total = len(expert_df)
expert_conscious_percentage = (expert_yes_conscious_count / expert_total) * 100
print(f"Percentage of experts who believe AI can become conscious:{expert_conscious_percentage:.2f}")