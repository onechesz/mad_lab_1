import pandas
from pandas.core.frame import DataFrame
from sklearn.preprocessing import normalize


def eighth_task(data: DataFrame):
    df_normalized = normalize(data, axis=0)

    return pandas.DataFrame(df_normalized, columns=data.columns)
