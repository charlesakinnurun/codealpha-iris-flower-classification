# %%
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

# %%
PROJECT_ROOT = Path.cwd().parent
DATA_PATH = PROJECT_ROOT / "data" / "engineered_iris_data.csv"

# %%
df = pd.read_csv(DATA_PATH)
df

# %%
# Define features matrix X and target vector y
X = df.drop("species", axis=1)
y = df["species"]

# %%
# Splitting: 80% Train, 20% Test
# random_state for reproducibility
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

# %%
X_train

# %%
X_test

# %%
y_train

# %%
y_test

# %%
X_train.to_csv("X_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)
y_train.to_csv("y_train.csv", index=False)
y_test.to_csv("y_test.csv", index=False)
print("Splitted data saved successfully.")


