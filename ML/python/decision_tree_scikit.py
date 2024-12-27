import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score


# 1 Data preparation
file_path = '/path/to/a/csvfile'
feature_columns = ['feature1', 'feature2', 'feature3', 'featuren']
target_column = 'target'
df = pd.read_csv(file_path)
dv = DictVectorizer()
df = dv.fit_transform(df[feature_columns].to_dict(orient='records'))

# 2 Split train set and test set
df_train = df.sample(frac=0.8, random_state=1)
df_test = df[~df.index.isin(df_train.index)]

# 3 Train
y_train = df_train[target_column].values
X_train = df_train[feature_columns].fillna(0).values
dt_model = DecisionTreeClassifier().fit(X_train, y_train)

# 4 Evaluation
X_test = df_test[feature_columns].fillna(0).values
y_predict = dt_model.predict(X_test)
y_predict_proba = dt_model.predict_proba(X_test)

y_test = df_test[target_column].values
roc_auc_score = roc_auc_score(y_test, y_predict)
