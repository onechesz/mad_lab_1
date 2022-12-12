import pandas

from se7en import seventh_task
from ei8ht import eighth_task
from n9ne import ninth_task
from t10n import tenth_task

data = pandas.read_csv('math_students.csv', delimiter=',')
seventh_data = seventh_task(data)
eighth_data = eighth_task(seventh_data)
ninth_data = ninth_task(seventh_data)
tenth_data = tenth_task(ninth_data)

print(tenth_data)

eighth_data.to_csv('eighth_data.csv')
tenth_data.to_csv('tenth_data.csv')
