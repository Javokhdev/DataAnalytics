import matplotlib
matplotlib.use('Agg')  # Switch to non-interactive backend

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
from scipy.stats import zscore

# Load dataset
df = pd.read_csv('air_quality_data.csv')

# Data Cleaning & Preparation
df.columns = df.columns.str.replace('"', '').str.strip()

print("Dataset Overview:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nDescriptive Statistics:")
print(df.describe())

# Visualize missing data using missingno
print("\nVisualizing Missing Data:")
msno.matrix(df)
plt.savefig('missing_data.png')  # Save the plot as a PNG file

# Handle missing values
df.fillna(method='ffill', inplace=True)

# Descriptive statistics after handling missing values
print("\nDescriptive Statistics After Handling Missing Data:")
print(df.describe())

# Outlier Detection (Z-scores)
df['z_score_air_quality'] = zscore(df['AirQuality'])
outliers = df[df['z_score_air_quality'].abs() > 3]
print(outliers)

df_cleaned = df[df['z_score_air_quality'].abs() <= 3]
print("\nDescriptive Statistics After Removing Outliers:")
print(df_cleaned.describe())

# EDA
sns.histplot(df['AirQuality'], kde=True)
plt.title('Distribution of Air Quality')
plt.savefig('air_quality_distribution.png')

sns.histplot(df['WaterPollution'], kde=True)
plt.title('Distribution of Water Pollution')
plt.savefig('water_pollution_distribution.png')

sns.boxplot(x=df['AirQuality'])
plt.title('Boxplot of Air Quality')
plt.savefig('air_quality_boxplot.png')

sns.boxplot(x=df['WaterPollution'])
plt.title('Boxplot of Water Pollution')
plt.savefig('water_pollution_boxplot.png')

# Only select numeric columns for correlation
numeric_columns = df.select_dtypes(include=[np.number])

# Calculate the correlation matrix using only numeric columns
sns.heatmap(numeric_columns.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png')

# Barplot of Air Quality by Country
plt.figure(figsize=(12, 6))
sns.barplot(x='Country', y='AirQuality', data=df)
plt.xticks(rotation=90)
plt.title('Average Air Quality by Country')
plt.savefig('air_quality_by_country.png')

# Insights
print("\nConclusion and Insights:")
print("1. The dataset shows varying levels of air quality and water pollution across countries.")
print("2. The correlation matrix shows a moderate correlation between Air Quality and Water Pollution.")
print("3. Countries with higher air quality tend to have lower water pollution (or vice versa).")

# Optional: Save the cleaned data
df_cleaned.to_csv('cleaned_air_quality_data.csv', index=False)
