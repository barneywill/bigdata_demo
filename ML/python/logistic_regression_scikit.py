import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split

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
