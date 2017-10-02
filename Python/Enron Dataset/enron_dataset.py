# This example shows working with a large dataset
# The classic Enron Dataset

# !/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).
    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }
    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:
    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print enron_data
names = [] # Initializing empty list to store all names
poi_flag = 0
pay_flag = 0

# iterating over the dict to get all 'keys' (names)
for values in enron_data.iterkeys():
    names.append(values)
    if enron_data[values]["poi"] == 1:
        poi_flag += 1
        if enron_data[values]['total_payments'] == 'NaN':
            pay_flag += 1


# printing the number of names in the dataset
print len(names)
print names
print enron_data['SKILLING JEFFREY K']['total_payments']
print enron_data['LAY KENNETH L']['total_payments']
print enron_data['FASTOW ANDREW S']['total_payments']
print poi_flag
print pay_flag




