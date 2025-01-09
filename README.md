# Exploratory Data Analysis on Air Quality and Water Pollution Data

## Overview
This project involves performing an Exploratory Data Analysis (EDA) on a dataset containing information about air quality and water pollution. The analysis aims to:
- Understand the distribution of air quality and water pollution variables.
- Identify and handle missing data, duplicates, and outliers.
- Visualize relationships between variables.
- Connect findings to implications for international trade.

The dataset used for this project is `air_quality_data.csv`, which contains measurements of air quality and water pollution levels from various countries.

## Features
- **Data Cleaning**: Handles missing values, removes duplicates, and detects outliers.
- **Visualizations**: Includes histograms, boxplots, scatter plots, and correlation heatmaps to reveal insights.
- **Automated Report Generation**: Saves cleaned data and visualizations as output files.
- **International Trade Insights**: Connects environmental data findings to trade implications.

---

## File Structure
```
DataAnalytics/
├── .venv/                         # Virtual environment
├── air_quality_data.csv            # Original dataset
├── eda_task.py                     # Python script for EDA
├── cleaned_air_quality_data.csv    # Cleaned dataset output
├── requirements.txt                # Dependencies list
├── missing_data_visualization.png  # Visualizations
├── air_quality_distribution.png    # Visualizations
├── water_pollution_distribution.png# Visualizations
├── air_quality_boxplot.png         # Visualizations
├── water_pollution_boxplot.png     # Visualizations
├── air_quality_by_country.png      # Visualizations
├── scatter_plot.png                # Visualizations
├── correlation_heatmap.png         # Visualizations
├── README.md                       # Project documentation (this file)
```

---

## Installation and Setup

### Prerequisites
- Python 3.7 or higher
- VS Code or another IDE for Python development

### Steps
1. Clone or download the project files.
2. Open a terminal in the project directory and create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - **Windows**:
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Run the Script**:
   Execute the Python script to clean the data, perform the EDA, and save the results:
   ```bash
   python eda_task.py
   ```

2. **Outputs**:
   - **Cleaned Data**: Saved as `cleaned_air_quality_data.csv`.
   - **Visualizations**: Saved as `.png` files in the project directory.

3. **Viewing Results**:
   - Open the `.png` visualization files to examine the data distribution, outliers, and correlations.
   - Read the console output for detailed analysis results and insights.

---

## Analysis Highlights

### Key Findings
1. **Air Quality and Water Pollution**:
   - The mean air quality is approximately X.
   - The mean water pollution level is approximately Y.
   - A correlation of Z suggests a moderate/strong relationship between these variables.

2. **Outliers**:
   - Removed data points with Z-scores greater than 3 to ensure accurate analysis.

3. **Visual Insights**:
   - Histograms and boxplots reveal the central tendencies and variability in the data.
   - A scatter plot shows the relationship between air quality and water pollution.
   - The correlation heatmap highlights significant relationships among numeric variables.

### Connection to International Trade
- Countries with stricter environmental standards may face higher production costs, affecting trade competitiveness.
- Conversely, less stringent standards could attract industries but face trade restrictions due to environmental concerns.

---

## Troubleshooting

### "ImportError: No module named 'colorama'"
- Ensure the virtual environment is activated before running the script.

### "FileNotFoundError: air_quality_data.csv"
- Ensure the dataset `air_quality_data.csv` is in the project root directory.

### Visualization Windows Opening
- If you prefer not to display plots, comment out `plt.show()` in the code.

---

## Dependencies
The project uses the following Python libraries:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `missingno`
- `colorama`

These dependencies are listed in the `requirements.txt` file.

---

## Credits
- **Dataset**: The dataset was sourced from Kaggle.
- **Tools**: Analysis was performed using Python with pandas, matplotlib, seaborn, and other libraries.

---

## License
This project is released under the [MIT License](https://opensource.org/licenses/MIT).

