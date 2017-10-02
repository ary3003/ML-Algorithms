import pickle
import numpy as np
import matplotlib.pyplot as plt
import sys
from feature_format import featureFormat, targetFeatureSplit
from sklearn.preprocessing import MinMaxScaler

sys.path.append("../tools/")


def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    # plot each cluster with a different color--add more colors for
    # drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]

    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    # if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()


# load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

# there's an outlier--remove it!
data_dict.pop("TOTAL", 0)

# the following block finds out the maximum stock and minimum stock
stocks = []
for key, value in data_dict.iteritems():
    if value['exercised_stock_options'] != 'NaN':
        stocks.append(value['exercised_stock_options'])
print max(stocks), min(stocks)

# Stock code block ends

# the following block finds out the maximum and minimum salary
salary = []
for key_, value_ in data_dict.iteritems():
    if value_['salary'] != 'NaN':
        salary.append(value_["salary"])
print max(salary), min(salary)

# salary code block ends


# the input features we want to use
# can be any key in the person-level dictionary (salary, director_fees, etc.)
# you can add how many more features you like just remember to update the for loop below
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"
poi = "poi"
features_list = [poi, feature_1, feature_2, feature_3]

# go and take a look over the featureFormat.py file to understand these methods
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


# this code assumes 3 features
# if you added more features above just remember to increase the unpacking variabes accordingly
# (as it's currently written, the line below assumes 3 features)
for f1, f2, _ in finance_features:
    plt.scatter( f1, f2, _ )
plt.show()

# The following block of code assumes feature scaling
# Each element of numpy array is going to be different training point
# Each element within that training point is ging to be a feature
# The features to be scaled should not be such that one of them cancels out the
# effect of other
# for example, from_messages and salary features can not be scaled
# since from_messages orders in the magnitude of hundreds
# and salary orders in the magnitude of thousands

salary_scale = np.array([477.,200000.,1111258.])
exercised_stock = np.array([3285.,1000000.,34348384.])

scaler = MinMaxScaler()

# The number scaled will contain the same information
# they will just be transformed to numbers between 0 and 1


salary_scale = scaler.fit_transform(salary_scale)
exercised_stock = scaler.fit_transform(exercised_stock)

print salary_scale, exercised_stock


# cluster here; creating predictions of the cluster labels

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2).fit(finance_features)

pred = kmeans.labels_






# rename the "name" parameter when you change the number of features
# so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters_3.png", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"