# %% [markdown]
# Data Encoding

# %%
from sklearn.preprocessing import LabelEncoder
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path.cwd().parent
DATA_PATH = PROJECT_ROOT / "data" / "preprocessed_iris_data.csv"

df = pd.read_csv(DATA_PATH)
df


# %%
# Handling Categorical Target: Encodiing "Species" to Numerical Labels
# Iris-setosa -> 0, Iris-versicolor -> 1, Iris-virginica -> 2
le = LabelEncoder()
df["species"] = le.fit_transform(df["species"])
class_names = le.classes_

# %%
df

# %%
# Project root (one level above notebooks)
PROJECT_ROOT = Path.cwd().parent
DATA_DIR = PROJECT_ROOT / "data"

# Create data directory if it doesn't exist
DATA_DIR.mkdir(exist_ok=True)

# Save file
output_path = DATA_DIR / "encoded_iris_data.csv"
df.to_csv(output_path, index=False)

print('Encoded data saved successfully!')


