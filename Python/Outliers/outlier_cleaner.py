#!/usr/bin/python

import math

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    # residual error is given as the absolute value of error squared
    errors = (net_worths - predictions)**2

    # cleaning the data according to the net_worth and errors
    cleaned_data = zip(ages, net_worths, errors)

    cleaned_data = sorted(cleaned_data, key=lambda x: x[2], reverse=True)
    limit = int(len(net_worths) * 0.1)

    return (cleaned_data[limit:])

