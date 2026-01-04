# %% [markdown]
# Exploratory Data Analysis

# %%
from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

PROJECT_ROOT = Path.cwd().parent
DATA_PATH = PROJECT_ROOT / "data" / "encoded_iris_data.csv"

df = pd.read_csv(DATA_PATH)

# %%
df

# %%
# Visualizing Class Distribution (Ensuring no Class Imbalance)
plt.figure(figsize=(6,4))
sns.countplot(x='species', data=df)
plt.title("Class Distribution (0: Setosa, 1: Versicolor, 2: Virginica)")
plt.show()

# %%
# Pairplot: Visualizing relationships and separability between features
sns.pairplot(df, hue='species', markers=["o", "s", "D"])
plt.suptitle("Pairplot of Iris Features", y=1.02)
plt.show()

# %%
# Correlation Heatmap: Identify Mulicollinearity
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(),annot=True,cmap="coolwarm",fmt=".2f")
plt.show()


