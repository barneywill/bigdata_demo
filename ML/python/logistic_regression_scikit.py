import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, roc_curve, auc, accuracy_score
import pickle

# 1 Data preparation
file_path = '/path/to/a/csvfile'
feature_columns = ['feature1', 'feature2', 'feature3', 'featuren']
label_column = 'label'
df = pd.read_csv(file_path)
dv = DictVectorizer()
#df = dv.fit_transform(df[feature_columns].to_dict(orient='records'))

# 2 Split train set and test set
folds = train_test_split(range(len(df)), test_size=0.2, random_state=1)
X_train = df[feature_columns].fillna(0).iloc[folds[0]]
y_train = df[label_column].iloc[folds[0]].values
X_test = df[feature_columns].fillna(0).iloc[folds[1]]
y_test = df[label_column].iloc[folds[1]].values

# 3 Train
vectorizer = dv.fit(X_train.to_dict(orient='records'))
with open('dv.pkl', 'wb') as f:
    pickle.dump(vectorizer, f, pickle.HIGHEST_PROTOCOL)
X_train = dv.transform(X_train.to_dict(orient='records'))
lr_model = LogisticRegression().fit(X_train, y_train)

r_sq = lr_model.score(X_train, y_train)
print('coefficient of determination:', r_sq)
print('intercept:', lr_model.intercept_)
print('slope:', lr_model.coef_)

# 4 Evaluation
X_test = dv.transform(X_test.to_dict(orient='records'))
# hard prediction
y_predict = lr_model.predict(X_test)
# probability prediction
y_predict_proba = lr_model.predict_proba(X_test)
any_result = (y_predict_proba >= 0.6)

accuracy = (y_test == y_predict).mean()
print(f"Accuracy: {accuracy:.4f}")

accuracy = accuracy_score(y_test, y_predict)
roc_auc_score = roc_auc_score(y_test, y_predict)
fpr, tpr, _ = roc_curve(y_test, y_predict)
roc_auc_curve = auc(fpr, tpr)

print("Accuracy:", accuracy)
print("ROC AUC Score:", roc_auc_score)
print("AUC from roc_curve:", roc_auc_curve)

with open('dv.pkl', 'rb') as f:
    dv_load = pickle.load(f)