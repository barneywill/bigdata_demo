import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction import DictVectorizer

# 1 Data preparation
file_path = '/path/to/a/csvfile'
feature_columns = ['feature1', 'feature2', 'feature3', 'featuren']
target_column = 'target'
df = pd.read_csv(file_path)
# category columns
dv = DictVectorizer()
#category_columns = ['col1', 'col2', 'coln']
#dv.fit(df[category_columns].to_dict(orient='records'))
#dv.get_feature_names()
#dv.tranform(df[category_columns].to_dict(orient='records'))
df = dv.fit_transform(df[feature_columns].to_dict(orient='records'))

# 2 Split train set and test set
df_train = df.sample(frac=0.8, random_state=1)
df_test = df[~df.index.isin(df_train.index)]

# 3 Train
y_train = df_train[target_column].values
# fill zeros
X_train = df_train[feature_columns].fillna(0).values
lr_model = LinearRegression().fit(X_train, y_train)

# Obtain the coefficient of determination by calling the model with the score() function, then print the coefficient:
r_sq = lr_model.score(X_train, y_train)
print('coefficient of determination:', r_sq)
print('intercept:', lr_model.intercept_)
print('slope:', lr_model.coef_) 

# 4 Evaluation
X_test = df_test[feature_columns].fillna(0).values
y_predict = lr_model.predict(X_test)
y_test = df_test[target_column].values
# by visualization
sns.histplot(y_predict, bins=50, color='red')
sns.histplot(y_test, bins=50, color='blue')
# by numbers
mae = (y_predict - y_test).mean()
se = (y_predict - y_test) ** 2
mse = se.mean()
rmse = np.sqrt(mse)
print(f'MAE: {mae}, MSE: {mse}, RMSE: {rmse}')