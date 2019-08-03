import pandas as pd
import numpy as np

KD = pd.read_csv('kidneyChronic.csv', na_values=['?', '\t?'])
numeric_datatype = ['age', 'bp', 'bgr', 'bu', 'sc',
                    'sod', 'pot', 'hemo', 'pcv', 'wbcc', 'rbcc']
nominal_datatype = ['sg', 'al', 'su', 'rbc', 'pc', 'pcc',
                    'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane']
print(KD.head())
print(KD.info())
print(KD.isnull().sum())
for data in numeric_datatype:
    KD[[data]].boxplot(showmeans=True)
print(KD['pcv'].value_counts(dropna=False))
# From the info we could see that for numerical data PCV
# is not correctly recognised as numeric which suggests malformed data
# PCV contains tabbed entry which needs to replaced with actual number
KD['pcv'] = pd.to_numeric(KD['pcv'], errors='coerce')
print(KD['pcv'].value_counts(dropna=False))
for numerical in numeric_datatype:
    print("Filling na with mean value for %s numerical data" % numerical)
    KD[numerical].fillna(np.mean(KD[numerical]), inplace=True)
# Once we have sorted out numerical data we need to fill missing
# entry in nominal data type with most occurring value
# Before filling the missing value check the values
for nominal in nominal_datatype:
    print(KD[nominal].value_counts(dropna=False))

# We see that htn and dm has bad values, we will rectify it manually
KD['htn'] = KD['htn'].replace('\tno', 'no')
KD['htn'] = KD['htn'].replace('\tyes', 'yes')
KD['dm'] = KD['dm'].replace('\tno', 'no')
KD['dm'] = KD['dm'].replace(' yes', 'yes')
for nominal in nominal_datatype:
    mode = KD[nominal].value_counts().index[0]
    print("Filling na with mode value %s for %s nominal data" % (mode, nominal))
    KD[nominal].fillna(mode, inplace=True)

print(KD.info())

# Separating feature variable and target variable
X = KD.drop('class', axis='columns')
Y = KD['class']

# Handling categorical columns in feature variable
X = pd.get_dummies(X, drop_first=True)
print(X.info())

# Handling missing value in target variable
print(Y.value_counts(dropna=False))

# Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.8, random_state=42)
rf = RandomForestClassifier(
    n_estimators=50, min_samples_leaf=0.2, random_state=42)
rf.fit(X_train, y_train)
pred = rf.predict(X_test)
print(classification_report(y_test, pred))
print("Accuracy of the RandomForestClassifier model is : {}".format(accuracy_score(y_test, pred)))

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X=X_train, y=y_train)
print("Feature importance: {}".format(clf.feature_importances_))
print("Accuracy of the DecisionTreeClassifier model is : {}".format(clf.score(X=X_test, y=y_test)))
