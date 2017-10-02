#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop("TOTAL", 0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")



# Finding the first largest value
max_salary_1 = 1000000
max_bonus = 5000000
max_salary_1_key = []
for data_element in data_dict:
# print data_element[0]['salary']
    if data_dict[data_element]['salary'] != 'NaN' and data_dict[data_element]['salary'] > max_salary_1 and data_dict[data_element]['bonus'] >=5000000:

        max_salary_1 = data_dict[data_element]['salary']
        max_salary_1_key.append(data_element)

print max_salary_1_key
print max_salary_1
print(data_dict[max_salary_1_key])

matplotlib.pyplot.show()

