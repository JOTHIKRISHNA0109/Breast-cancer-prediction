import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
link="C:\\Users\\asus\\Breast Cancer Prediction\\data.csv"
data = pd.read_csv(link)
data.drop(data.columns[[-1, 0]], axis=1, inplace=True)
diagnosis_all = list(data.shape)[0]
diag_map = {'M':1, 'B':0}
data['diagnosis'] = data['diagnosis'].map(diag_map)
features_mean= list(data.columns[1:11])
X = data.loc[:,features_mean]
Y = data.loc[:,'diagnosis']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)