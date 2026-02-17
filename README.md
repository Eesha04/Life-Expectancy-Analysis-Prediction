# Analyzing Global Trends in Life Expectancy

## Project Overview
[cite_start]This project investigates the intricate relationship between a nation's socio-economic factors and its **Life Expectancy**[cite: 47, 53]. [cite_start]By analyzing 15 years of data from 243 countries aggregated by the **World Health Organization (WHO)**, this study utilizes advanced data science techniques and interactive visualizations to uncover patterns that inform healthcare and socio-economic policies[cite: 55, 67, 68].

---

## Core Objectives
* [cite_start]**Correlation Analysis:** Delve deep into the relationship between GDP, education, and health indicators[cite: 53, 54].
* [cite_start]**Data Integrity:** Identify and handle erroneous data points (e.g., impossible mortality or BMI values)[cite: 158, 173].
* [cite_start]**Predictive Modeling:** Build a robust Lasso regression model to predict life expectancy based on socio-economic drivers[cite: 847, 849].
* [cite_start]**Interactive Exploration:** Provide nuanced insights through 3D interactive graphs and geographic choropleth maps[cite: 1149, 1316].

---

## Technical Stack
* [cite_start]**Language:** Python [cite: 57, 58]
* [cite_start]**Libraries:** `Pandas`, `NumPy`, `Scikit-learn`, `Matplotlib`, `Seaborn`, `Plotly`, `Folium` [cite: 57-64, 1156, 1316]
* [cite_start]**Methodologies:** Lasso Regression, K-Means Clustering, Winsorization, and Iterative Imputation [cite: 62, 372, 815, 849, 901]

---

## Data Pipeline & Preprocessing

### 1. Data Cleaning & Imputation
[cite_start]The project manages a high volume of missing data using sophisticated modeling rather than simple deletion[cite: 183, 381].
* [cite_start]**Standardization:** Cleaned column names by removing whitespace and converting to lowercase for error-resistant analysis [cite: 84-87].
* [cite_start]**Iterative Imputer:** Used `IterativeImputer` to estimate missing features by modeling them as a function of other features, resulting in a dataset with **0.0% null values**[cite: 372, 381, 384].

> <img width="405" height="323" alt="image" src="https://github.com/user-attachments/assets/2fb208c8-1774-4a99-a175-bca45d96878a" />

> [cite_start]*This visualization shows that the distribution remained consistent even after data cleaning/dropping rows[cite: 362, 364].*

### 2. Outlier Management
[cite_start]To prevent extreme values (outliers) from skewing results, we implemented **Winsorization**[cite: 815].
* [cite_start]**Technique:** Extreme values are transformed to be less extreme rather than being removed, maintaining the integrity of the dataset while reducing influence on statistical analyses[cite: 816, 817].

---

## Key Insights & Modeling

### Statistical Correlation
[cite_start]The analysis identified the top four factors most highly correlated with life expectancy[cite: 1001]:
1.  [cite_start]**Schooling** (Positive Correlation) [cite: 1001]
2.  [cite_start]**Income Composition of Resources** (Positive Correlation) [cite: 1001]
3.  [cite_start]**HIV/AIDS Prevalence** (Negative Correlation) [cite: 1001]
4.  [cite_start]**Adult Mortality** (Negative Correlation) [cite: 1001]

> <img width="640" height="368" alt="image" src="https://github.com/user-attachments/assets/9f46799a-fd09-4462-aa84-61502e7438a9" />


### Machine Learning Performance
[cite_start]We utilized a Lasso Regression model to perform simultaneous feature selection and prediction[cite: 849, 851].
* [cite_start]**Mean Squared Error (MSE):** 12.92 [cite: 888]
* [cite_start]**R-squared ($R^2$):** 0.836 [cite: 888]
* [cite_start]**Result:** The model explains approximately **83.6% of the variance** in global life expectancy[cite: 890].

---

## Advanced Visualizations

### 1. Interactive 3D Exploration
[cite_start]By incorporating multiple attributes into a 3D interactive graph, we visualized the synergy between economic prosperity, education, and health[cite: 1149, 1151].
* [cite_start]**Axes:** GDP, Schooling, and Life Expectancy categorized by Developed/Developing status[cite: 1168, 1181].

### 2. K-Means Clustering
[cite_start]Grouped countries based on measles and HIV/AIDS prevalence to identify similar health risk patterns[cite: 892, 936].
* [cite_start]**Outcome:** Enabled data-driven decision-making for targeting specific healthcare interventions[cite: 937].

> <img width="613" height="326" alt="image" src="https://github.com/user-attachments/assets/2c31cee5-aae0-48b3-adf3-301de3bd11d5" />


### 3. Geographic Choropleth Map
[cite_start]Created an interactive map using the `Folium` library to visualize geographic variations in life expectancy[cite: 1316, 1320].

---

## Conclusion
[cite_start]The findings highlight a compelling disparity: developed nations, with advanced healthcare and stable economies, exhibit significantly higher life expectancy than developing nations[cite: 1075, 1076]. [cite_start]This project demonstrates that while GDP is a strong indicator, the combination of **education (schooling)** and **economic stability** are the primary drivers for a healthier global society[cite: 1153, 1637].

---

## How to Run
1. Clone this repository.
2. Open the notebook in **Google Colab**.
3. [cite_start]Upload the required CSV datasets when prompted by the `files.upload()` cell[cite: 73].
