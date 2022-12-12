from pandas import DataFrame


def ninth_task(data: DataFrame):
    g3_marks = list()

    for value in data['G3'].values:
        if value < 11:
            g3_marks.append(0)
        else:
            g3_marks.append(1)

    data['G3_marks'] = g3_marks

    data = data.drop('G1', axis=1)
    data = data.drop('G2', axis=1)
    data = data.drop('G3', axis=1)

    return data
