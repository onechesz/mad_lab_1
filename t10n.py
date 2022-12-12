from pandas import DataFrame


def tenth_task(data: DataFrame):
    return data['G3_marks'].value_counts()
