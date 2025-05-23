# data_cleaning_cheatsheet.py

import pandas as pd
import numpy as np
import seaborn as sns

# Step 1: Understand Data Structure
data = {
    'Name': ['Alice', 'Bob', 'Charlie', np.nan, 'Eve'],
    'Age': [25, 30, 35, 40, np.nan],
    'Gender': ['F', 'M', 'M', 'M', 'F'],
    'Score': [85, np.nan, 90, 88, 95],
    'Registered': ['2022-01-01', '2022-02-15', '2022-01-20', '2022-03-01', '2022-04-10']
}
df = pd.DataFrame(data)

# Step 2: Explore the Data
print(df.describe())
print(df.info())
print(df.head())

# Step 3: Standardize Data Formats
df['Name'] = df['Name'].str.title()
df['Registered'] = pd.to_datetime(df['Registered'], format='%Y-%m-%d')
df['Gender'] = df['Gender'].str.strip().str.upper()

# Step 4: Remove Duplicates
df = df.drop_duplicates()

# Step 5: Handle Missing Values
df['Name'] = df['Name'].fillna('Unknown')
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Score'] = df['Score'].fillna(df['Score'].mean())

# Step 6: Standardize String Values
df['Gender'] = df['Gender'].replace({'FEMALE': 'F', 'MALE': 'M'})

# Step 7: Filter Out Bad Data
df = df[df['Score'] > 0]  # remove clearly bad data
threshold = len(df) * 0.5
df = df.dropna(axis=1, thresh=threshold)

# Step 8: Remove Outliers
Q1 = df['Score'].quantile(0.25)
Q3 = df['Score'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df = df[(df['Score'] >= lower_bound) & (df['Score'] <= upper_bound)]

# Step 9: Rename Columns
df = df.rename(columns={
    'Name': 'name',
    'Age': 'age',
    'Gender': 'gender',
    'Score': 'score',
    'Registered': 'registration_date'
})

# Step 10: Save Cleaned Data
df.to_csv('cleaned_data.csv', index=False)
