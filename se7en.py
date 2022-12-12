import pandas

from pandas.core.frame import DataFrame
from sklearn.preprocessing import OneHotEncoder


def seventh_task(data: DataFrame):
    dataframe = pandas.DataFrame()
    ohe = OneHotEncoder(sparse=False)

    for column in data.columns:
        if data.dtypes[column] == object:
            dataframe[column] = data[column].copy()
            dataframe_ohe = ohe.fit_transform(dataframe)
            data[column + '01'] = dataframe_ohe[:, 0]
            data[column + '02'] = dataframe_ohe[:, 1]
            data = data.drop(column, axis=1)

    return data
