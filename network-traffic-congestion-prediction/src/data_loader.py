import pandas as pd

def load_data(path):
    """Load dataset from the specified path."""
    try:
        df = pd.read_csv(path)
        print(f"Data shape: {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
