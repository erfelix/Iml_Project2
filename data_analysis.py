import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

print(df.head(5))

# Calculate the sum over each column
nan_sum = df.isna().sum()

# Reset the index to convert the resulting Series to a DataFrame
nan_sum_df = nan_sum.reset_index()

# Rename the columns for better readability
nan_sum_df.columns = ['Countries', 'MissingValuesCount']

# Create the bar plot using Seaborn
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
sns.barplot(data=nan_sum_df, x='Countries', y='MissingValuesCount')
plt.title('Number of missing values for each Country')
plt.xlabel('Countries')
plt.ylabel('MissingValuesCount')
plt.show()