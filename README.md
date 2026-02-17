# Analyzing Global Trends in Life Expectancy

## Project Overview
This project investigates the intricate relationship between a nation's socio-economic factors and its **Life Expectancy**. By analyzing 15 years of data from 243 countries aggregated by the **World Health Organization (WHO)**, this study utilizes advanced data science techniques and interactive visualizations to uncover patterns that inform healthcare and socio-economic policies.

---

## Core Objectives
* **Correlation Analysis:** Delve deep into the relationship between GDP, education, and health indicators.
* **Data Integrity:** Identify and handle erroneous data points (e.g., impossible mortality or BMI values).
* **Predictive Modeling:** Build a robust Lasso regression model to predict life expectancy based on socio-economic drivers.
* **Interactive Exploration:** Provide nuanced insights through 3D interactive graphs and geographic choropleth maps.

---

## Technical Stack
* **Language:** Python 
* **Libraries:** `Pandas`, `NumPy`, `Scikit-learn`, `Matplotlib`, `Seaborn`, `Plotly`, `Folium` 
* **Methodologies:** Lasso Regression, K-Means Clustering, Winsorization, and Iterative Imputation 

---

## Data Pipeline & Preprocessing

### 1. Data Cleaning & Imputation
The project manages a high volume of missing data using sophisticated modeling rather than simple deletion.
* **Standardization:** Cleaned column names by removing whitespace and converting to lowercase for error-resistant analysis.
* **Iterative Imputer:** Used `IterativeImputer` to estimate missing features by modeling them as a function of other features, resulting in a dataset with **0.0% null values**.

> <img width="405" height="323" alt="image" src="https://github.com/user-attachments/assets/2fb208c8-1774-4a99-a175-bca45d96878a" />

> *This visualization shows that the distribution remained consistent even after data cleaning/dropping rows.*

### 2. Outlier Management
To prevent extreme values (outliers) from skewing results, we implemented **Winsorization**.
* **Technique:** Extreme values are transformed to be less extreme rather than being removed, maintaining the integrity of the dataset while reducing influence on statistical analyses.

---

## Key Insights & Modeling

### Statistical Correlation
The analysis identified the top four factors most highly correlated with life expectancy:
1.  **Schooling** (Positive Correlation) 
2.  **Income Composition of Resources** (Positive Correlation) 
3.  **HIV/AIDS Prevalence** (Negative Correlation) 
4.  **Adult Mortality** (Negative Correlation) 

> <img width="640" height="368" alt="image" src="https://github.com/user-attachments/assets/9f46799a-fd09-4462-aa84-61502e7438a9" />


### Machine Learning Performance
We utilized a Lasso Regression model to perform simultaneous feature selection and prediction.
* **Mean Squared Error (MSE):** 12.92 
* **R-squared ($R^2$):** 0.836 
* **Result:** The model explains approximately **83.6% of the variance** in global life expectancy.

---

## Advanced Visualizations

### 1. Interactive 3D Exploration
By incorporating multiple attributes into a 3D interactive graph, we visualized the synergy between economic prosperity, education, and health.
* **Axes:** GDP, Schooling, and Life Expectancy categorized by Developed/Developing status.

### 2. K-Means Clustering
Grouped countries based on measles and HIV/AIDS prevalence to identify similar health risk patterns.
* **Outcome:** Enabled data-driven decision-making for targeting specific healthcare interventions.

> <img width="613" height="326" alt="image" src="https://github.com/user-attachments/assets/2c31cee5-aae0-48b3-adf3-301de3bd11d5" />


### 3. Geographic Choropleth Map
Created an interactive map using the `Folium` library to visualize geographic variations in life expectancy.

---

## Conclusion
The findings highlight a compelling disparity: developed nations, with advanced healthcare and stable economies, exhibit significantly higher life expectancy than developing nations. This project demonstrates that while GDP is a strong indicator, the combination of **education (schooling)** and **economic stability** are the primary drivers for a healthier global society.

---

## How to Run
1. Clone this repository.
2. Open the notebook in **Google Colab**.
3. Upload the required CSV datasets when prompted by the `files.upload()` cell.
