import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split

# 1 Data preparation
file_path = '/path/to/a/csvfile'
feature_columns = ['feature1', 'feature2', 'feature3', 'featuren']
label_column = 'label'
df = pd.read_csv(file_path)
# category columns
dv = DictVectorizer()
#category_columns = ['col1', 'col2', 'coln']
#dv.fit(df[category_columns].to_dict(orient='records'))
#dv.get_feature_names()
#dv.tranform(df[category_columns].to_dict(orient='records'))
#df = dv.fit_transform(df[feature_columns].to_dict(orient='records'))

# 2 Split train set and test set
folds = train_test_split(range(len(df)), test_size=0.2, random_state=1)
X_train = df[feature_columns].fillna(0).iloc[folds[0]]
y_train = df[label_column].iloc[folds[0]].values
X_test = df[feature_columns].fillna(0).iloc[folds[1]]
y_test = df[label_column].iloc[folds[1]].values

# 3 Train
X_train = dv.fit_transform(X_train.to_dict(orient='records'))
lr_model = LinearRegression().fit(X_train, y_train)

# Obtain the coefficient of determination by calling the model with the score() function, then print the coefficient:
r_sq = lr_model.score(X_train, y_train)
print('coefficient of determination:', r_sq)
print('intercept:', lr_model.intercept_)
print('slope:', lr_model.coef_) 

# 4 Evaluation
X_test = dv.transform(X_test.to_dict(orient='records'))
y_predict = lr_model.predict(X_test)
# by visualization
sns.histplot(y_predict, bins=50, color='red')
sns.histplot(y_test, bins=50, color='blue')
# by numbers
mae = (y_predict - y_test).mean()
se = (y_predict - y_test) ** 2
mse = se.mean()
rmse = np.sqrt(mse)
print(f'MAE: {mae}, MSE: {mse}, RMSE: {rmse}')