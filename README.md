## Introduction
The dataset contains 247 entries related to public opinions on Artificial Intelligence (AI) gaining consciousness. The data appears to be from a survey, with columns capturing demographic information and a range of opinions on AI.
### Data Cleaning
```python
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
```
### Analysis
1. **Education and Opinion:** How does the distribution of opinions on AI consciousness (Can_AI_Become_Conscious) differ across various Education_Level groups?
2. **Age and Threat Perception:** What is the average Age of respondents who classify AI as a 'Serious threat' compared to those who see it as a 'Low threat' or 'No threat at all'?
3. **Tech Interest vs. Knowledge:** Is there a strong correlation between a respondent's self-reported Tech_Interest and their AI_Knowledge_Level?
4. **Rights and Gender:** What is the percentage breakdown of respondents who believe AI should have rights (Should_It_Have_Rights), separated by Gender?
5. **Regulation and Education:** What proportion of people with a 'PhD' degree believe governments should 'Yes, definitely' regulate AI?
6. **Working Comfort and Consciousness Belief:** Among those who believe AI can become conscious (Can_AI_Become_Conscious is 'Yes'), what is the most frequent response for Working_Comfort?
7. **Sufferability and Threat Perception:** How does the Threat_Assessment of AI differ for those who believe AI can suffer (Can_It_Suffer is 'Yes') versus those who do not (Can_It_Suffer is 'No')?
8. **Knowledge and Consciousness:** What percentage of respondents with an AI_Knowledge_Level of 'I am an expert' believe that AI can become conscious (Can_AI_Become_Conscious)?
9. **Interest and Regulation:** What are the most common Should_Governments_Regulate responses for each category of Tech_Interest?
10. **Individual Consideration:** How many respondents, categorized by Education_Level, believe that an AI should be considered an individual (Should_Be_Considered_Individual is 'Yes')?
#### How does the distribution of opinions on AI consciousness (Can_AI_Become_Conscious) differ across various Education_Level groups?
```python
import pandas as pd
# Load the cleaned data

df = pd.read_csv("datasets/ai_cleaned.csv")

print("Education and Opinion")

education_opinion = df.groupby("Education_Level")["Can_AI_Become_Conscious"].value_counts(normalize=True).unstack(fill_value=0).round(2)
print("Distribution of Opinions of AI consciousness by Education level")
print(education_opinion)
```
#### What is the average Age of respondents who classify AI as a 'Serious threat' compared to those who see it as a 'Low threat' or 'No threat at all'?
```python
import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/ai_cleaned.csv")

print("Age and Threat Perception")

threat_groups = df.groupby("Threat_Assessment")["Age"].mean().round(2)
print("Average age of AI threat assessment")
print(threat_groups.head())
```
#### Is there a strong correlation between a respondent's self-reported Tech_Interest and their AI_Knowledge_Level?
```python
import pandas as pd

# Load the datasets
df = pd.read_csv("datasets/ai_cleaned.csv")

# Tech Interest vs Knowledge
print("Tech Interest vs Knowledge")
tech_interest_knowledge = pd.crosstab(df["Tech_Interest"],df["AI_Knowledge_Level"],normalize="index").round(2)
print("Relationship between Tech Interest and AI Knowledge Level (row percentages):\n")
print(tech_interest_knowledge.head())
```
#### What is the percentage breakdown of respondents who believe AI should have rights (Should_It_Have_Rights), separated by Gender?
```python
import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/ai_cleaned.csv")

print("Rights and Gender")

rights_gender = pd.crosstab(df["Gender"],df["Should_It_Have_Rights"],normalize="index").round(2)
print("'Percentage of responses of AI having rights, by gender")
print(rights_gender)
```
#### What proportion of people with a 'PhD' degree believe governments should 'Yes, definitely' regulate AI?
```python
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
```
#### Among those who believe AI can become conscious (Can_AI_Become_Conscious is 'Yes'), what is the most frequent response for Working_Comfort?
```python
import pandas as pd

# Import the cleaned data
df = pd.read_csv("datasets/ai_cleaned.csv")

# Working Comfort and Consciousness Belief
print("Working Comfort and Consciousness Belief")
yes_conscious_df = df[df["Can_AI_Become_Conscious"] == "Yes"]
most_common_comfort = yes_conscious_df["Working_Comfort"].mode()[0]

print(f"Among those who believe AI can become conscious, the most common 'Working_Comfort' response is: {most_common_comfort}")
```
#### How does the Threat_Assessment of AI differ for those who believe AI can suffer (Can_It_Suffer is 'Yes') versus those who do not (Can_It_Suffer is 'No')?
```python
import pandas as pd

# Load the dataset
df = pd.read_csv("datasets/ai_cleaned.csv")

# Sufferability and Threat Perception
print("Sufferability and Threat Perception")
suffer_threat = df.groupby("Can_It_Suffer")["Threat_Assessment"].value_counts(normalize=True).unstack(fill_value=0).round(2)
print("Threat assessment distribution by belief in AIs ability to suffer")
print(suffer_threat)
```
#### What percentage of respondents with an AI_Knowledge_Level of 'I am an expert' believe that AI can become conscious (Can_AI_Become_Conscious)?
```python
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
```
#### What are the most common Should_Governments_Regulate responses for each category of Tech_Interest?
```python
import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/ai_cleaned.csv")

# Interest and Regulation
print("Interest and Regulation")
interest_regulation = df.groupby("Tech_Interest")["Should_Governments_Regulate"].apply(lambda x: x.mode()[0] if not x.mode().empty else None)
print("Most common regulation opinion for each tech interest group")
print(interest_regulation)
```
#### How many respondents, categorized by Education_Level, believe that an AI should be considered an individual (Should_Be_Considered_Individual is 'Yes')?
```python
import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/ai_cleaned.csv")

# Question 10: Individual Consideration
print("--- Question 10: Individual Consideration ---")
individual_consideration_count = df[df['Should_Be_Considered_Individual'] == 'Yes'].groupby('Education_Level').size()
print("Number of respondents who believe AI should be considered an individual, by education level:\n")
print(individual_consideration_count)
```
