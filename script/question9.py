import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/ai_cleaned.csv")

# Interest and Regulation
print("Interest and Regulation")
interest_regulation = df.groupby("Tech_Interest")["Should_Governments_Regulate"].apply(lambda x: x.mode()[0] if not x.mode().empty else None)
print("Most common regulation opinion for each tech interest group")
print(interest_regulation)