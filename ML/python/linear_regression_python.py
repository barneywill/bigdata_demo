import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1 Data preparation
file_path = '/path/to/a/csvfile'
feature_columns = ['feature1', 'feature2', 'feature3', 'featuren']
label_column = 'target'
df = pd.read_csv(file_path)
categorical_columns = ['cat1', 'cat2', 'catn']
for c in categorical_columns:
    for v in df[c].value_counts().head(5).index:
        new_feature_column = '%s=%s' % (c, v)
        df[new_feature_column] = (df[c] == v).astype('int')
        feature_columns.append(new_feature_column)

# 2 Split train set and test set
df_train = df.sample(frac=0.8, random_state=1)
df_test = df[~df.index.isin(df_train.index)]

# 3 Train
y_train = df_train[label_column].values
# fill zeros
X_train = np.column_stack((np.ones(len(df_train)), df_train[feature_columns].fillna(0).values))
# regularization
w = np.linalg.inv(X_train.T.dot(X_train) + np.eye(X_train.shape[1]) * 0.001).dot(X_train.T).dot(y_train)

# 4 Evaluation
X_test = np.column_stack(np.ones(len(df_test)), df_test[feature_columns].fillna(0).values)
y_predict = X_test.dot(w)
y_test = df_test[label_column].values
# by visualization
sns.histplot(y_predict, bins=50, color='red')
sns.histplot(y_test, bins=50, color='blue')
# by numbers
mae = (y_predict - y_test).mean()
se = (y_predict - y_test) ** 2
mse = se.mean()
rmse = np.sqrt(mse)
print(f'MAE: {mae}, MSE: {mse}, RMSE: {rmse}')