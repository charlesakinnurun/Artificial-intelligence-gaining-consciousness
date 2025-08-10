import pandas as pd
import io

# Load the datasets
df = pd.read_csv("datasets/ai.csv")

# Print the shape before removing duplicates
print(f"Shape before removing duplicates: {df.shape}")

# Remove duplicate rows
df_cleaned = df.drop_duplicates()

# Print the shape after removing duplicates
print(f"Shape after removing the dupicates: {df_cleaned.shape}")

# Get the list of object type columns to check unique values again
object_cols = df_cleaned.select_dtypes(include="object").columns.to_list()

# Print unique values for each object column to confirm they are clean
for col in object_cols:
    print(f"Unique values in '{col}': {df_cleaned[col].unique()}")

# Save the cleaned dataset
df_cleaned.to_csv("datasets/ai_cleaned.csv")
print("Saved Successfully")