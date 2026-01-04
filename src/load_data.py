# %% [markdown]
# Data Loading

# %%
import pandas as pd
def load_data():
    # Load the iris dataset from a CSV file
    df = pd.read_csv("data/iris_raw.csv")
    return df

# %%
data = load_data()
print(data.head())
