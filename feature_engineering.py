from datavisualization import data_vis
from data_cleaning import data_cleaning


def feat_eng():
    data = data_vis()
    print("final dataframe----------", data)
    data.replace({'not smoking': 0, 'smoking': 1}, inplace=True)
    data = data.drop('age_group', axis=1)
    data.to_csv("binary_smoke_prediction.csv", index=False)


    return data

feat_eng()
