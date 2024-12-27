import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score, roc_curve, auc, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import export_text


# 1 Data preparation
file_path = '/path/to/a/csvfile'
feature_columns = ['feature1', 'feature2', 'feature3', 'featuren']
target_column = 'target'
df = pd.read_csv(file_path)
dv = DictVectorizer()
#df = dv.fit_transform(df[feature_columns].to_dict(orient='records'))

# 2 Split train set and test set
folds = train_test_split(range(len(df)), test_size=0.2, random_state=1)
X_train = df[feature_columns].fillna(0).iloc[folds[0]]
y_train = df[target_column].iloc[folds[0]].values
X_test = df[feature_columns].fillna(0).iloc[folds[1]]
y_test = df[target_column].iloc[folds[1]].values

# 3 Train
X_train = dv.fit_transform(X_train.to_dict(orient='records'))
dt_model = DecisionTreeClassifier(max_depth=3).fit(X_train, y_train)

# Visualize the decision tree
print(export_text(dt_model, feature_names=dv.get_feature_names_out()))

# 4 Evaluation
X_test = dv.transform(X_test.to_dict(orient='records'))
y_predict = dt_model.predict(X_test)
y_predict_proba = dt_model.predict_proba(X_test)

accuracy = accuracy_score(y_test, y_predict)
roc_auc_score = roc_auc_score(y_test, y_predict)
fpr, tpr, _ = roc_curve(y_test, y_predict)
roc_auc_curve = auc(fpr, tpr)

print("Accuracy:", accuracy)
print("ROC AUC Score:", roc_auc_score)
print("AUC from roc_curve:", roc_auc_curve)