from data_analysis import data_analysis

def data_cleaning():
    data = data_analysis()
    categ = []
    numer = []

    for col in data.columns:
        if data[col].dtype == object:
            categ.append(col)
        else:
            numer.append(col)

    print("categ-----------", categ)
    print("numer-----------", numer)

    print(data['smoking'].value_counts())
    print(data.dtypes)

    data = data.drop('id', axis=1)

    #removing columns 

    # for col in data.columns:
    #     if 'LDL' in col:
    #         del data[col]
    #     elif 'waist(cm)' in col:
    #         del data[col]
    #     else:
    #         continue
    # print(list(data.columns))
     
    return data
data_cleaning()
