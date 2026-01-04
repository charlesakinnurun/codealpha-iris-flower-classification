# %% [markdown]
# Data Preprocessing

# %%
import sys
from pathlib import Path

project_root = Path.cwd().parent
sys.path.append(str("src"))

# %%
import pandas as pd
import load_data as ld
def preprocess_data():
    df = ld.load_data()
    return df

# %%
df = preprocess_data()
df.head()

# %%
# Data Information
print(df.info())

# %%
# Shape of the Data
print("Shape of the data:", df.shape)

# %%
# Check for duplicated rows
df_duplicated = df.duplicated().sum()
print("Number of duplicated rows:", df_duplicated)

# %%
# Check for missing values
if df.isnull().sum().any():
    print("Missing values detected. Performing imputation...")
    df = df.fillna(df.median())

# %%
df

# %%
# Dropping the "Id" as it unique identifier and adds no predictive value (avoid overfitting)
if 'Id' in df.columns:
    df = df.drop(columns=['Id'])

# %%
df

# %%
# Rename columns for consistency
df.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)

# %%
df

# %%
'''import sys
from pathlib import Path

project_root = Path.cwd().parent
sys.path.append(str("data"))'''

# %%
from pathlib import Path

# Project root (one level above notebooks)
PROJECT_ROOT = Path.cwd().parent
DATA_DIR = PROJECT_ROOT / "data"

# Create data directory if it doesn't exist
DATA_DIR.mkdir(exist_ok=True)

# Save file
output_path = DATA_DIR / "preprocessed_iris_data.csv"
df.to_csv(output_path, index=False)

print('Prepprocessed data saved successfully!')


# %%
#preprocessed_df = df

# %%
#preprocessed_df

# %%
def preprocess_data():
    df
    return df

# %%
data = preprocess_data()
print(data.head())


