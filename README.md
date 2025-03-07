# House Sales Map Data Analysis

## Project Description
This project aims to analyze house sales data, identify the variables affecting house prices, and present results through various visualizations. The dataset was analyzed using Python.

## Methods Used & Learnings
- **Data Loading and Inspection**: The CSV file was loaded using Pandas and basic data exploration was performed.
- **Correlation Analysis**: Relationships among numerical variables were examined, and the top 10 features with the highest correlation to "SalePrice" were identified.
- **Data Visualization**:
  - Correlation matrix visualized using Seaborn.
  - Average sale prices by ZIP code displayed using a bar chart.
  - The most expensive houses were plotted on a map using Folium.

## Analyses & Findings
1. **Correlation Analysis:**
   - The top 10 variables most correlated with "SalePrice" were identified.
   - A heatmap was used to visualize the correlation structure.
![Figure_2](https://github.com/user-attachments/assets/4e1ac2eb-68f7-42dc-9372-c6ccf1cfbe05)

2. **Average Sale Prices by ZIP Code:**
   - The top 20 ZIP codes with the highest prices were visualized using a bar chart.
![indir (1)](https://github.com/user-attachments/assets/66c23697-ac1d-4680-a020-e8ed3f31fa0e)

3. **Geographic Distribution of the Most Expensive Houses:**
   - The top 10 most expensive houses were marked on a map using Folium.
   - The map was saved as `most_expensive_houses_map.html`.

## Technologies Used
- **Python** (pandas, numpy, seaborn, matplotlib, folium)
- **Jupyter Notebook or Google Colab** (for executing the code and performing analysis)

## Files
- `house_sales.csv`: The dataset used.
- `most_expensive_houses_map.html`: The map visualization of the most expensive houses.
- `house_sales_analysis.ipynb`: The Python code used for analysis.

## How to Use?
1. Clone the project to your local machine.
2. Install the required Python libraries:
   ```sh
   pip install pandas numpy seaborn matplotlib folium
   ```
3. Run the `house_sales_analysis.ipynb` file using Jupyter Notebook or Google Colab.

This project is useful for data scientists and real estate analysts interested in analyzing house prices and visualizing them on a map.

![Ekran görüntüsü 2025-03-07 150714](https://github.com/user-attachments/assets/3ef4bd3d-fb2a-4115-a205-16dadacabc68)


