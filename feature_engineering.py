from datavisualization import data_vis
from data_cleaning import data_cleaning


def feat_eng():
    data = data_vis()
    print("final dataframe----------", data)
    data.replace({'not smoking': 0, 'smoking': 1}, inplace=True)
    data = data.drop('age_group', axis=1)

    x = data.drop('smoking', axis=1)
    y = data['smoking']
    oversample = SMOTE()
    #undersample = RandomUnderSampler()
    X, Y = oversample.fit_resample(x, y)
    data = pd.concat([X, pd.Series(Y, name='smoking')], axis=1)

    print("after samplng---------", data['smoking'].value_counts())

    print("before duplicate values: ",  data.duplicated().sum())
    #print("drop duplcates-----------", data.drop_duplicates(inplace=True))

    print("final duplicate values: ",  data.isnull().sum())
    data.to_csv("binary_smoke_prediction.csv", index=False)


    return data

feat_eng()
