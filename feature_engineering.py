from datavisualization import data_vis
from data_cleaning import data_cleaning


def feat_eng():
    data = data_vis()
    print("final dataframe----------", data)

    data.to_csv("binary_smoke_prediction.csv", index=False)


    return data

feat_eng()
