import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('Training.csv')
ill = list(data['prognosis'].unique())


def make_desition(prognosis):
    return ill.index(prognosis)


data['desition'] = data['prognosis'].apply(make_desition)
data.drop('prognosis', axis=1, inplace=True)
X = data.drop('desition', axis=1)
y = data['desition']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
clf = RandomForestClassifier(max_depth=50, random_state=10, max_features=100, n_estimators=10)
