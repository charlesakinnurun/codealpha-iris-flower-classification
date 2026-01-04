# %%
import pandas as pd
from pathlib import Path

# %%
PROJECT_ROOT = Path.cwd().parent
DATA_PATH = PROJECT_ROOT / "data" / "encoded_iris_data.csv"

# %%
df = pd.read_csv(DATA_PATH)
df

# %%
# Engineering "Ratios" - often flower species are defined by the proportion of petals/sepals
# Creating a Petal Aspect Ratio and Sepal Aspect Ratio
df["petalratio"] = df["petallengthcm"] / df["petalwidthcm"]
df["sepalratio"] = df["sepallengthcm"] / df["sepalwidthcm"]
print("\n--- Feature Engineering Complete (Added Ratios) ---")

# %%
df

# %%
# Project root (one level above notebooks)
PROJECT_ROOT = Path.cwd().parent
DATA_DIR = PROJECT_ROOT / "data"

# Create data directory if it doesn't exist
DATA_DIR.mkdir(exist_ok=True)

# Save file
output_path = DATA_DIR / "engineered_iris_data.csv"
df.to_csv(output_path, index=False)

print('Feature engineered data saved successfully!')


