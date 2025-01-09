import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
from scipy.stats import zscore
from colorama import Fore, Style

# --- Introduction ---
print(Fore.GREEN + "# Exploratory Data Analysis of Air Quality and Water Pollution Data" + Style.RESET_ALL)
print("## Introduction")
print("This analysis explores a dataset containing information about air quality and water pollution levels. The goal is to understand the distributions of these variables, identify potential outliers, examine correlations, and connect these findings to potential implications for international trade. The dataset used is 'air_quality_data.csv'.")  # Replace with your dataset info

# --- Load Dataset ---
try:
    df = pd.read_csv('air_quality_data.csv')  # Replace with your dataset path
except FileNotFoundError:
    print(Fore.RED + "Error: air_quality_data.csv not found. Please ensure the file is in the correct directory." + Style.RESET_ALL)
    exit()

# --- Data Cleaning and Preparation ---
print(Fore.YELLOW + "## Methodology: Data Cleaning and Preparation" + Style.RESET_ALL)

# Clean Column Names
df.columns = df.columns.str.replace('"', '').str.strip()

# --- Data Type Checks ---
print(Fore.YELLOW + "### Ensuring Correct Data Types" + Style.RESET_ALL)
df['AirQuality'] = pd.to_numeric(df['AirQuality'], errors='coerce')
df['WaterPollution'] = pd.to_numeric(df['WaterPollution'], errors='coerce')

# --- Missing Data Visualization ---
print("### Missing Data Visualization")
msno.matrix(df)
plt.title('Missing Data Visualization')
plt.savefig('missing_data_visualization.png')
# plt.show()

# Handle Missing Values (Forward Fill)
print(Fore.GREEN + "Missing values were handled using forward fill." + Style.RESET_ALL)
df.fillna(method='ffill', inplace=True)

# --- Remove Duplicates ---
print("### Duplicate Removal")
print(Fore.GREEN + f"Number of duplicate rows before removal: {df.duplicated().sum()}" + Style.RESET_ALL)
df.drop_duplicates(inplace=True)
print(Fore.GREEN + f"Number of duplicate rows after removal: {df.duplicated().sum()}" + Style.RESET_ALL)

# --- Outlier Detection (Z-scores) ---
print("### Outlier Detection")
df['z_score_air_quality'] = zscore(df['AirQuality'])
df_cleaned = df[df['z_score_air_quality'].abs() <= 3].copy()
print(Fore.GREEN + "Outliers with Z-scores greater than 3 were removed." + Style.RESET_ALL)

# --- Exploratory Data Analysis (EDA) ---
print(Fore.YELLOW + "## Methodology: Exploratory Data Analysis" + Style.RESET_ALL)

# Descriptive Statistics
print("### Descriptive Statistics")
print("#### Numerical Variables:")
print(df_cleaned.describe())

# Check for categorical columns before trying to describe them
categorical_cols = df_cleaned.select_dtypes(include=['object', 'category']).columns
if not categorical_cols.empty:
    print("#### Categorical Variables:")
    for col in categorical_cols:
        print(f"Value counts for {col}:\n{df_cleaned[col].value_counts()}\n")
else:
    print(Fore.GREEN + "No categorical columns detected in the dataset." + Style.RESET_ALL)

# --- Visualizations ---
print("### Visualizations")

def create_annotated_histogram(data, column_name, color, filename):
    plt.figure(figsize=(12, 6))
    sns.histplot(data, kde=True, color=color, label=f'{column_name} Distribution')
    mean_val = data.mean()
    std_val = data.std()
    plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {mean_val:.2f}')
    plt.axvline(mean_val + std_val, color='green', linestyle='dashed', linewidth=1, label=f'+1 Std Dev')
    plt.axvline(mean_val - std_val, color='green', linestyle='dashed', linewidth=1, label=f'-1 Std Dev')
    plt.title(f'Distribution of {column_name} with Mean and Std Dev')
    plt.xlabel(column_name, fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.savefig(filename, dpi=300)
    print(Fore.BLUE + f"\nColor Explanation ({filename}):" + Style.RESET_ALL)
    print(f"- {color.capitalize()}: Represents the distribution of {column_name} values.")
    print("- Red dashed line: Indicates the mean.")
    print("- Green dashed lines: Indicate one standard deviation above and below the mean.")

def create_annotated_boxplot(data, column_name, color, filename):
    plt.figure(figsize=(8, 6))
    sns.boxplot(y=data, color=color, showmeans=True, meanprops={"marker":"o", "markerfacecolor":"white", "markeredgecolor":"black", "markersize":"10"})
    median_val = data.median()
    plt.axhline(median_val, color='red', linestyle='dashed', linewidth=1, label=f'Median: {median_val:.2f}')
    plt.title(f'Boxplot of {column_name} with Median and Mean')
    plt.ylabel(column_name, fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.savefig(filename, dpi=300)
    print(Fore.BLUE + f"\nColor Explanation ({filename}):" + Style.RESET_ALL)
    print(f"- {color.capitalize()}: Represents the distribution of {column_name} values in the boxplot.")
    print("- Red dashed line: Indicates the median.")
    print("- White circle with black border: Indicates the mean.")

# Create histograms and boxplots
create_annotated_histogram(df_cleaned['AirQuality'], 'Air Quality', 'skyblue', 'air_quality_distribution.png')
create_annotated_histogram(df_cleaned['WaterPollution'], 'Water Pollution', 'salmon', 'water_pollution_distribution.png')
create_annotated_boxplot(df_cleaned['AirQuality'], 'Air Quality', 'lightgreen', 'air_quality_boxplot.png')
create_annotated_boxplot(df_cleaned['WaterPollution'], 'Water Pollution', 'lightcoral', 'water_pollution_boxplot.png')

# --- Air Quality by Country Barplot ---
print("### Air Quality by Country Barplot (Fixed)")
# Aggregating data by country for cleaner barplot
df_country = df.groupby('Country').agg({'AirQuality': 'mean', 'WaterPollution': 'mean'}).reset_index()
top_countries = df_country.sort_values('AirQuality', ascending=False).head(10)

plt.figure(figsize=(14, 8))
sns.barplot(x='Country', y='AirQuality', data=top_countries, palette='Blues_d')
plt.xticks(rotation=90, fontsize=10)
plt.yticks(fontsize=12)
plt.title('Top 10 Countries by Average Air Quality', fontsize=14)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Average Air Quality', fontsize=12)
plt.tight_layout()
plt.savefig('air_quality_by_country.png', dpi=300)

# --- Scatter Plot ---
print("### Scatter Plot")
plt.figure(figsize=(8, 6))
sns.scatterplot(x='AirQuality', y='WaterPollution', data=df_cleaned, color='purple')
plt.title('Scatter Plot of Air Quality vs. Water Pollution')
plt.savefig('scatter_plot.png')
# plt.show()

# --- Correlation Heatmap ---
print("### Correlation Heatmap")
numeric_columns = df_cleaned.select_dtypes(include=[np.number])  # Corrected line
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_columns.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png')
# plt.show()

# --- Findings ---
print(Fore.YELLOW + "## Findings" + Style.RESET_ALL)
print("Based on the EDA, we observed the following:")

mean_aq = df_cleaned['AirQuality'].mean()
std_aq = df_cleaned['AirQuality'].std()
mean_wp = df_cleaned['WaterPollution'].mean()
std_wp = df_cleaned['WaterPollution'].std()
median_aq_box = df_cleaned['AirQuality'].median()
median_wp_box = df_cleaned['WaterPollution'].median()

print(f"- Air Quality: The distribution is centered around a mean of {mean_aq:.2f} with a standard deviation of {std_aq:.2f}. The median is {median_aq_box:.2f}.")
print(f"- Water Pollution: The distribution has a mean of {mean_wp:.2f} and a standard deviation of {std_wp:.2f}. The median is {median_wp_box:.2f}.")
correlation = numeric_columns.corr().loc['AirQuality', 'WaterPollution']
print(f"- The scatter plot and correlation heatmap suggest a correlation of {correlation:.2f} between Air Quality and Water Pollution.")

# --- Conclusion and International Trade Connection ---
print(Fore.YELLOW + "## Conclusion and International Trade Connection" + Style.RESET_ALL)
print("This analysis provided insights into the distributions of air quality and water pollution. The observed correlation could have implications for international trade. For example:")
print("- Countries with higher environmental standards might face higher production costs, impacting their competitiveness in certain sectors.")
print("- Conversely, countries with lower environmental standards might attract industries seeking lower costs but could face trade barriers due to environmental concerns.")
print("Further research could explore the relationship between environmental regulations, trade flows, and economic development.")

# Save cleaned data
df_cleaned.to_csv('cleaned_air_quality_data.csv', index=False)
