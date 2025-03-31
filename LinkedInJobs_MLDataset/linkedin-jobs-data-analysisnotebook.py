import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv(r"C:\Users\pawar\python_data_science\Project\new-res-proj\res-LinkedInJobs_MLDataset\LinkedInJobs_MLDataset.csv")

# Basic Data Exploration
print("Dataset Info:")
df.info()
print("\nSummary Statistics:")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())

# Data Distribution
num_cols = ['Emp_Cnt', 'Flw_Cnt', 'max_sal', 'med_sal', 'min_sal', 'views']
df[num_cols].hist(figsize=(12, 8), bins=30)
plt.show()

# Categorical Distribution
cat_cols = ['Job_Ttl', 'loc', 'wrk_typ', 'xp_lvl']
for col in cat_cols:
    plt.figure(figsize=(12, 5))
    sns.countplot(y=df[col], order=df[col].value_counts().index[:10])
    plt.title(f"Top 10 {col} by Count")
    plt.show()

# Job Market Trends
print("\nTop Hiring Companies:")
print(df['Co_Nm'].value_counts().head(10))

print("\nMost Popular Job Titles:")
print(df['Job_Ttl'].value_counts().head(10))

print("\nLocation Analysis:")
print(df['loc'].value_counts().head(10))

# Salary Analysis
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['med_sal'])
plt.title("Salary Distribution")
plt.show()

print("\nSalary by Experience Level:")
print(df.groupby('xp_lvl')[['min_sal', 'med_sal', 'max_sal']].mean())

# Application & Engagement Insights
print("\nJob Views Analysis:")
print(df[['Job_Ttl', 'views']].sort_values(by='views', ascending=False).head(10))

print("\nApplication Type Impact:")
print(df.groupby('app_typ')['views'].mean())

print("\nSponsorship Effect:")
print(df.groupby('is_sponsored')['views'].mean())

# Remote Work Analysis
print("\nRemote vs Onsite Salary Comparison:")
print(df.groupby('is_remote')[['min_sal', 'med_sal', 'max_sal']].mean())
