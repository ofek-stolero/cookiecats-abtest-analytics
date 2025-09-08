import kagglehub
import pandas as pd

def load_cookie_cats():
    # Download latest version of dataset (cached in ~/.kagglehub/)
    path = kagglehub.dataset_download("yufengsui/mobile-games-ab-testing")
    print("Dataset path:", path)

    # Load CSV
    df = pd.read_csv(f"{path}/cookie_cats.csv")
    return df
