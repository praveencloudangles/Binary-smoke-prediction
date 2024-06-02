from data_loading import data_load

def data_analysis():
    data = data_load()

    print(data)

    print("null values: ", data.isnull().sum())
    print("duplicate values: ",  data.duplicated().sum())
    print("shape of dataframe: ", data.shape)
    print("target variable count: ", data['smoking'].value_counts())
    print("describe: ", data.describe())

    return data

data_analysis()