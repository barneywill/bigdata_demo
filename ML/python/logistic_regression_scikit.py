import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer

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
lr_model = LogisticRegression().fit(X_train, y_train)

r_sq = lr_model.score(X_train, y_train)
print('coefficient of determination:', r_sq)
print('intercept:', lr_model.intercept_)
print('slope:', lr_model.coef_)

# 4 Evaluation
X_test = df_test[feature_columns].fillna(0).values
# hard prediction
y_predict = lr_model.predict(X_test)
# probability prediction
y_predict_proba = lr_model.predict_proba(X_test)
any_result = (y_predict_proba >= 0.6)

y_test = df_test[target_column].values
accuracy = (y_test == y_predict).mean()
print(f"Accuracy: {accuracy:.4f}")
