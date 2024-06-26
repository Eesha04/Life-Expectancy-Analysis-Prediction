# -*- coding: utf-8 -*-
"""Copy of final.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OEZio4bJytjKPZQJfwFsWCyhwAZB2M-x

Understanding and exploring our datasets
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from scipy.stats.mstats import winsorize
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
import os
# %matplotlib inline

import pandas as pd
from google.colab import files
import matplotlib.pyplot as plt
uploaded=files.upload()
import io
df1 = pd.read_csv(io.BytesIO(uploaded['dataset1.csv']))

import pandas as pd
from google.colab import files
import matplotlib.pyplot as plt
uploaded=files.upload()
import io
df2 = pd.read_csv(io.BytesIO(uploaded['dataset2.csv']))

import pandas as pd
from google.colab import files
import matplotlib.pyplot as plt
uploaded=files.upload()
import io
df3 = pd.read_csv(io.BytesIO(uploaded['dataset3.csv']))

df4=pd.merge(df1,df2)
df4.head()

df=pd.merge(df4,df3)
df.head()
df.drop(df.columns[0], axis=1, inplace=True)
df.head()

df.shape

orig_cols = list(df.columns)
new_cols = []
for col in orig_cols:
    new_cols.append(col.strip().replace('  ', ' ').replace(' ', '_').lower())
df.columns = new_cols

df.rename(columns={'thinness_1-19_years':'thinness_10-19_years'}, inplace=True)

original_df=df
original_df

plt.figure(figsize=(15,10))
for i, col in enumerate(['adult_mortality', 'infant_deaths', 'bmi', 'under-five_deaths', 'gdp', 'population'], start=1):
    plt.subplot(2, 3, i)
    df.boxplot(col)

import numpy as np
mort_5_percentile = np.percentile(df.adult_mortality.dropna(), 5)
df.adult_mortality = df.apply(lambda x: np.nan if x.adult_mortality < mort_5_percentile else x.adult_mortality, axis=1)
df.infant_deaths = df.infant_deaths.replace(0, np.nan)
df.bmi = df.apply(lambda x: np.nan if (x.bmi < 10 or x.bmi > 50) else x.bmi, axis=1)
df['under-five_deaths'] = df['under-five_deaths'].replace(0, np.nan)

def nulls_breakdown(df=df):
    df_cols = list(df.columns)
    cols_total_count = len(list(df.columns))
    cols_count = 0
    for loc, col in enumerate(df_cols):
        null_count = df[col].isnull().sum()
        total_count = df[col].isnull().count()
        percent_null = round(null_count/total_count*100, 2)
        if null_count > 0:
            cols_count += 1
            print('[iloc = {}] {} has {} null values: {}% null'.format(loc, col, null_count, percent_null))
    cols_percent_null = round(cols_count/cols_total_count*100, 2)
    print('Out of {} total columns, {} contain null values; {}% columns contain null values.'.format(cols_total_count, cols_count, cols_percent_null))

nulls_breakdown()

df.drop('bmi', axis=1, inplace=True)

cols=[var for var in df.columns if df[var].isnull().mean()<0.05 and df[var].isnull().mean()>0]
cols

(len(df[cols].dropna())/len(df))*100

df.dropna(subset=cols,inplace=True)
df.shape

fig = plt.figure()
ax = fig.add_subplot(111)

# original data
original_df['life_expectancy'].plot.density(color='red')

# data after cca
df['life_expectancy'].plot.density(color='green')

fig = plt.figure()
ax = fig.add_subplot(111)

# original data
original_df['adult_mortality'].plot.density(color='red')

# data after cca
df['adult_mortality'].plot.density(color='green')

fig = plt.figure()
ax = fig.add_subplot(111)

# original data
original_df['polio'].plot.density(color='red')

# data after cca
df['polio'].plot.density(color='green')

fig = plt.figure()
ax = fig.add_subplot(111)

# original data
original_df['diphtheria'].plot.density(color='red')

# data after cca
df['diphtheria'].plot.density(color='green')

fig = plt.figure()
ax = fig.add_subplot(111)

# original data
original_df['thinness_10-19_years'].plot.density(color='red')

# data after cca
df['thinness_10-19_years'].plot.density(color='green')

fig = plt.figure()
ax = fig.add_subplot(111)

# original data
original_df['thinness_5-9_years'].plot.density(color='red')

# data after cca
df['thinness_5-9_years'].plot.density(color='green')

from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import pandas as pd
import numpy as np

cols_drop=['country','status']
temp_df=df.drop(cols_drop,axis=1)
cols_df=df[cols_drop]
# Create an instance of IterativeImputer
imputer = IterativeImputer(random_state=0)

# Fit and transform the imputer on your data
X_imputed = imputer.fit_transform(temp_df)

# The result is a NumPy array with imputed values
# Convert it back to a DataFrame if needed
df_imputed = pd.DataFrame(X_imputed, columns=temp_df.columns)
# new_df=pd.merge(cols_df,df_imputed,on='Year')
new_df = cols_df.merge(df_imputed, left_index=True, right_index=True)
df=new_df

nulls_breakdown(new_df)

"""Handling outliers"""

cont_vars = list(df.columns)[3:]
def outliers_visual(data):
    plt.figure(figsize=(15, 40))
    i = 0
    for col in cont_vars:
        i += 1
        plt.subplot(9, 4, i)
        plt.boxplot(data[col])
        plt.title('{} boxplot'.format(col))
        i += 1
        plt.subplot(9, 4, i)
        plt.hist(data[col])
        plt.title('{} histogram'.format(col))
    plt.show()
outliers_visual(df)

def outlier_count(col, data=df):
    print(15*'-' + col + 15*'-')
    q75, q25 = np.percentile(data[col], [75, 25])
    iqr = q75 - q25
    min_val = q25 - (iqr*1.5)
    max_val = q75 + (iqr*1.5)
    outlier_count = len(np.where((data[col] > max_val) | (data[col] < min_val))[0])
    outlier_percent = round(outlier_count/len(data[col])*100, 2)
    print('Number of outliers: {}'.format(outlier_count))
    print('Percent of data that is outlier: {}%'.format(outlier_percent))

for col in cont_vars:
    outlier_count(col)

def test_wins(col, lower_limit=0, upper_limit=0, show_plot=True):
    wins_data = winsorize(df[col], limits=(lower_limit, upper_limit))
    wins_dict[col] = wins_data
    if show_plot == True:
        plt.figure(figsize=(15,5))
        plt.subplot(121)
        plt.boxplot(df[col])
        plt.title('original {}'.format(col))
        plt.subplot(122)
        plt.boxplot(wins_data)
        plt.title('wins=({},{}) {}'.format(lower_limit, upper_limit, col))
        plt.show()

wins_dict = {}
test_wins(cont_vars[0], lower_limit=.01, show_plot=True)
test_wins(cont_vars[1], upper_limit=.04, show_plot=False)
test_wins(cont_vars[2], upper_limit=.05, show_plot=False)
test_wins(cont_vars[3], upper_limit=.0025, show_plot=False)
test_wins(cont_vars[4], upper_limit=.135, show_plot=False)
test_wins(cont_vars[5], lower_limit=.1, show_plot=False)
test_wins(cont_vars[6], upper_limit=.19, show_plot=False)
test_wins(cont_vars[7], upper_limit=.05, show_plot=False)
test_wins(cont_vars[8], lower_limit=.1, show_plot=False)
test_wins(cont_vars[9], upper_limit=.02, show_plot=False)
test_wins(cont_vars[10], lower_limit=.105, show_plot=False)
test_wins(cont_vars[11], upper_limit=.185, show_plot=False)
test_wins(cont_vars[12], upper_limit=.105, show_plot=False)
test_wins(cont_vars[13], upper_limit=.07, show_plot=False)
test_wins(cont_vars[14], upper_limit=.035, show_plot=False)
test_wins(cont_vars[15], upper_limit=.035, show_plot=False)
test_wins(cont_vars[16], lower_limit=.05, show_plot=False)
test_wins(cont_vars[17], lower_limit=.025, upper_limit=.005, show_plot=False)

print(cont_vars)
print(col)
plt.figure(figsize=(15,5))
for i, col in enumerate(cont_vars, 1):
    plt.subplot(21, 2, i)
    plt.boxplot(wins_dict[col])
plt.tight_layout()
plt.show()

wins_df = df.iloc[:, 0:3]
for col in cont_vars:
    wins_df[col] = wins_dict[col]

wins_df.describe()
nulls_breakdown(wins_df)

"""Filters"""

mask = np.triu(wins_df[cont_vars].corr())
plt.figure(figsize=(15,6))
sns.heatmap(wins_df[cont_vars].corr(), annot=True, fmt='.2g', vmin=-1, vmax=1, center=0, cmap='coolwarm', mask=mask)
plt.ylim(18, 0)
plt.title('Correlation Matrix Heatmap')
plt.show()

df_filtered = wins_df[wins_df['year'] == 2015]
df_filtered

correlation_matrix=wins_df[cont_vars].corr()
correlation_with_life = correlation_matrix['life_expectancy'].abs().sort_values(ascending=False)

# Exclude 'lifeexpectancy' itself from the list
correlation_with_life = correlation_with_life.drop('life_expectancy')

# Get the top four correlated columns
top_correlations = correlation_with_life.head(4)

# Extract the column names
top_correlation_columns = top_correlations.index.tolist()

print("Top four correlated columns with 'life_expectancy':")
print(top_correlation_columns)

colsel = top_correlation_columns + ['year'] + ['life_expectancy']
new_df = df_filtered[colsel]
new_df

for column in top_correlation_columns:
    q1 = np.percentile(new_df[column], 25)
    q3 = np.percentile(new_df[column], 75)
    iqr = q3 - q1
    print(f"q1 for {column}: {q1}")
    print(f"q3 for {column}: {q3}")

q1=np.percentile(new_df['life_expectancy'],25)
q3=np.percentile(new_df['life_expectancy'],75)
print(q1)
print(q3)

df.columns

"""filtering countries with high life expectancy"""

# Assuming df is your pandas DataFrame containing the dataset

# Filter out countries based on correlations
filtered_countries_high = wins_df[
    ((wins_df['adult_mortality'] < 75.5) |
    (wins_df['hiv/aids'] < 0.1) |
    (wins_df['income_composition_of_resources'] > 0.7945) |
    (wins_df['schooling'] > 14.85)) &
    (wins_df['life_expectancy'] > 76.95)
     & (wins_df['year'] == 2015)
]

# Output the filtered countries
print(filtered_countries_high.sort_values('life_expectancy'))

wins_df
nulls_breakdown(wins_df)

"""filtering countries with low life expectancy"""

# Filter out countries based on correlations
filtered_countries_low = wins_df[
    ((wins_df['adult_mortality'] > 213.0) |
    (wins_df['hiv/aids'] > 0.4) |
    (wins_df['income_composition_of_resources'] < 0.575) |
    (wins_df['schooling'] < 11.1)) &
    (wins_df['life_expectancy'] < 65.75)
     & (wins_df['year'] == 2015)
]

# Output the filtered countries
print(filtered_countries_low.sort_values('life_expectancy'))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error, r2_score


cols=wins_df.columns.tolist()
cols.remove('life_expectancy')
cols.remove('country')
cols.remove('status')
cols.remove('year')
# Select independent variables (X) and the target variable (y)
X = wins_df[cols]  # Include your independent variables
y = wins_df['life_expectancy']  # Your target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the Lasso regression model
alpha = 0.01  # Adjust the regularization strength (alpha) as needed
model = Lasso(alpha=alpha)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Print the coefficients of the selected features
feature_names = X.columns
coefficients = model.coef_

"""interactive plots"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load your dataset, assuming it's stored in a CSV file
# Replace 'your_dataset.csv' with the actual file path


# Define the features for clustering
features = ['measles', 'hiv/aids']

# Group the data by country and calculate the average prevalence over 15 years
average_data = wins_df.groupby('country')[features].mean()

# Create a K-Means model with the desired number of clusters
n_clusters = 3  # You can adjust the number of clusters
kmeans = KMeans(3, random_state=0)
cluster_labels = kmeans.fit_predict(average_data)

# Plot the clustered data
plt.figure(figsize=(12, 6))
for i in range(n_clusters):
    plt.scatter(
        average_data[cluster_labels == i]['measles'],
        average_data[cluster_labels == i]['hiv/aids'],
        label=f'Cluster {i + 1}',
    )

# Set labels and legend
plt.xlabel('Average Measles Prevalence')
plt.ylabel('Average HIV/AIDS Prevalence')
plt.title('Clustering of Average Prevalence of HIV/AIDS and Measles (15-Year Average) by Country')
plt.legend()

# Show the plot
plt.show()



!pip install plotly
import plotly.express as px

# Interactive Scatter Plot
scatter_plot = px.scatter(df, x='gdp', y='life_expectancy', color='country', hover_data=['year'])
scatter_plot.update_traces(marker=dict(size=12, opacity=0.8))
scatter_plot.update_layout(title='Interactive Scatter Plot: GDP vs Life Expectancy',
                          xaxis_title='GDP',
                          yaxis_title='Life Expectancy')

scatter_plot.show()

# Interactive Histogram
histogram = px.histogram(df, x='life_expectancy', color='country', marginal='rug')
histogram.update_layout(title='Interactive Histogram: Life Expectancy',
                        xaxis_title='Life Expectancy',
                        yaxis_title='Count')

histogram.show()

# boxplot for Status and life expectancy
sns.boxplot(x='Status', y='Life expectancy', data=df)
plt.show()

# boxplot for Status and Schooling
import seaborn as sns

plt.figure(figsize=(8, 6))
sns.boxplot(x='Status', y='Schooling', data=df1)
plt.xlabel('Status')
plt.ylabel('Schooling')
plt.title('Schooling Years by Status')
plt.show()

# interactive 3D graph for the 3 parameters
import plotly.express as px

# Sample data (replace this with your actual dataset)
countries = df['country']
status = df['status']
life_expectancy = df['life_expectancy']
schooling = df['schooling']

# Create a DataFrame
import pandas as pd
data = pd.DataFrame({'Country': countries, 'Status': status, 'Life Expectancy': life_expectancy, 'Schooling': schooling})

# Create an interactive 3D scatter plot using Plotly
fig = px.scatter_3d(data, x='Status', y='Life Expectancy', z='Schooling', color='Status',
                    labels={'x': 'Status', 'y': 'Life Expectancy', 'z': 'Schooling'},
                    title='Interactive 3D Graph: Status, Life Expectancy, and Schooling',
                    text='Country')  # 'text' parameter for hover information

# Customize hover text
fig.update_traces(textposition='top center')

# Show the interactive plot
fig.show()

"""cluster and predictions

General insights gathered from data visualization

---

developed countries with high schooling have greater life expectancy

---
"""

# boxplot for Status and life expectancy
sns.boxplot(x='Status', y='Life expectancy', data=df)
plt.show()

inp_country=input("Enter Country : ")

# Filter the DataFrame to get data for the user input country
country_df = wins_df[wins_df['country'] == inp_country]
country_df
attributes = [col for col in country_df.columns if col != 'life_expectancy']
attributes.remove('country')
attributes.remove('status')
# Set up the number of rows and columns for subplots
num_rows = len(attributes)
num_cols = 1  # You can change this if you want a different number of columns

# Create a new figure
fig, axes = plt.subplots(num_rows, num_cols, figsize=(8, 4*num_rows))

# Ensure axes is a 2D array
if num_rows == 1:
    axes = [axes]

# Loop through the attributes and create plots
for i, attribute in enumerate(attributes):
    ax = axes[i]

    # Scatter plot of the current attribute vs. LifeExpectancy
    ax.plot(country_df[attribute], country_df['life_expectancy'], marker='o', linestyle='-', color='b')

    ax.set_xlabel(attribute)
    ax.set_ylabel('Life Expectancy')
    ax.set_title(f'{attribute} vs. Life Expectancy')

# Adjust spacing between subplots
plt.tight_layout()

# Show the plots
plt.show()

!pip install seaborn matplotlib

import seaborn as sns
import matplotlib.pyplot as plt

# Create a violin plot using seaborn
sns.set(style="whitegrid")  # Set the style of the plot
plt.figure(figsize=(8, 6))  # Set the size of the plot

# Create the violin plot
sns.violinplot(y=df['life_expectancy'], color="skyblue")

# Add labels and title
plt.ylabel("Life Expectancy")
plt.title("Violin Plot of Life Expectancies")

# Display the plot
plt.show()

import plotly.express as px

# Sample data (replace this with your actual dataset)
countries = wins_df['country']
GDP = wins_df['gdp']
life_expectancy = wins_df['life_expectancy']
schooling = wins_df['schooling']
status = wins_df['status']

# Create a DataFrame
import pandas as pd
data = pd.DataFrame({'Country': countries, 'GDP': GDP, 'Life Expectancy': life_expectancy, 'Schooling': schooling, 'Status': status})

# Create an interactive 3D scatter plot using Plotly
fig = px.scatter_3d(data, x='GDP', y='Life Expectancy', z='Schooling', color='Status',
                    labels={'x': 'GDP', 'y': 'Life Expectancy', 'z': 'Schooling'},
                    title='Interactive 3D Graph: Life Expectancy based on status, schooling, and GDP')

# Customize hover text
fig.update_traces(textposition='top center')

# Show the interactive plot
fig.show()

# Find the index of the row with the highest life expectancy value
max_life_expectancy_index = filtered_countries_high['life_expectancy'].idxmax()
# Extract the row with the highest life expectancy value into a new DataFrame
highest_life_expectancy_df = filtered_countries_high.loc[max_life_expectancy_index:max_life_expectancy_index]
highest_life_expectancy_df

# Find the index of the row with the highest life expectancy value
min_life_expectancy_index = filtered_countries_low['life_expectancy'].idxmin()
# Extract the row with the highest life expectancy value into a new DataFrame
lowest_life_expectancy_df = filtered_countries_low.loc[min_life_expectancy_index:min_life_expectancy_index]
lowest_life_expectancy_df

c1=str(highest_life_expectancy_df['country'])
print(c1)
c2=str(lowest_life_expectancy_df['country'])
print(c2)

# Filter data for country_df1
country_df1 = wins_df[wins_df['country'] == 'Albania']

# Filter data for country_df2
country_df2 = wins_df[wins_df['country'] == 'Seychelles']

attributes = [col for col in country_df1.columns if col not in ['life_expectancy', 'country', 'status']]
print(attributes)
# Set up the number of rows and columns for subplots
num_rows = len(attributes)
num_cols = 1  # You can change this if you want a different number of columns






for attribute in attributes:
    plt.figure(figsize=(8, 5))

    plt.scatter(country_df1[attribute], country_df1['life_expectancy'], label='Albania', alpha=0.5)
    plt.scatter(country_df2[attribute], country_df2['life_expectancy'], label='Seychelles', alpha=0.5)

    plt.xlabel(attribute)
    plt.ylabel('Life Expectancy')
    plt.title(f'Scatter Plot: {attribute} vs. Life Expectancy')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Sort the DataFrame by 'Life_Expectancy' in descending order and get the top 5 rows
top_5_life_expectancy_df = filtered_countries_high.sort_values(by='life_expectancy', ascending=False).head(5)



# Sort the DataFrame by 'Life_Expectancy' in descending order and get the top 5 rows
top_5_low_life_expectancy_df = filtered_countries_low.sort_values(by='life_expectancy', ascending=True).head(5)



list1= top_5_life_expectancy_df['country'].tolist()

list2= top_5_low_life_expectancy_df['country'].tolist()

# Filter data for country_df1
country_df1 = wins_df[wins_df['country'].isin(list1)]

# Filter data for country_df2
country_df2 = wins_df[wins_df['country'].isin(list2)]

attributes = [col for col in country_df1.columns if col not in ['life_expectancy', 'country', 'status']]

# Set up the number of rows and columns for subplots
num_rows = len(attributes)
num_cols = 1  # You can change this if you want a different number of columns




# Loop through the attributes and create plots
# for i, attribute in enumerate(attributes):
#     plt.scatter(country_df1[attribute], country_df1['life_expectancy'], label='Albania', alpha=0.5)
#     plt.scatter(country_df2[attribute], country_df2['life_expectancy'], label='Seychelles', alpha=0.5)

#     plt.xlabel(attribute)
#     plt.ylabel('Life Expectancy')
#     plt.title(f'Scatter Plot: {attribute} vs. Life Expectancy')
#     plt.legend()

for attribute in attributes:
    plt.figure(figsize=(8, 5))

    plt.scatter(country_df1[attribute], country_df1['life_expectancy'], label='Albania', alpha=0.5)
    plt.scatter(country_df2[attribute], country_df2['life_expectancy'], label='Seychelles', alpha=0.5)

    plt.xlabel(attribute)
    plt.ylabel('Life Expectancy')
    plt.title(f'Scatter Plot: {attribute} vs. Life Expectancy')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Add a legend to distinguish between the two countries


# # Adjust spacing between subplots
# plt.tight_layout()

# # Show the plots
# plt.show()