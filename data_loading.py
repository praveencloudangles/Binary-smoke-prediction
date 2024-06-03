import pandas as pd

def data_load():

    df = pd.read_csv("train_dataset.csv")

    return df

data_load()
