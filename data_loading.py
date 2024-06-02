import pandas as pd

def data_load():

    df = pd.read_csv("train.csv")

    return df

data_load()