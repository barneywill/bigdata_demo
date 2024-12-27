
# Machine Learning

![Machine Learning](https://github.com/barneywill/bigdata_demo/blob/main/imgs/ml.jpg)

## Process
### Training
Features(Input) + Targets(Desired Output) -> Machine Learning -> Model
### Prediction
Features(Input) + Model -> Predicitions(Output)

## Steps
- Business Understanding: Goal, Measurable
- Data Understanding: Avial data sources, Data quality
- Data Preparation: Clean, Transform, Feature Engineering, Data Sampling
- Modeling: Train and choose the best model
- Evaluation: Offline and Online
- Deployment

## Models
- Regression
- Classification
- Clustering
- Recommendation

## Techniques

### Free Dataset
https://www.kaggle.com/

### Python Library

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

### Jupyter Notebook

```
# install
pip install jupyterlab
pip install notebook

# change the ip
jupyter notebook --generate-config
vim .jupyter/jupyter_notebook_config.py
c.ServerApp.ip = '$your_ip'

# set password
jupyter notebook password
# input your password

# start
jupyter notebook

# open
Open http://$your_ip:8888 in a browser.
or
Use Jupyter plugin in vscode.
```

### Data Exploration

```
# all data
df
# data types
df.dtypes
# number data statistics
df.describe()
# null data
df.isnull().sum()
# unique and count
df['col_name'].unique()
df['col_name'].nunique()
# distribution
df['col_name'].vlaue_counts()
df.groupby(['col_name']).size().reset_index(name='count').sort_values('count', ascending=False).iloc[:10]
# graphic distribution
sns.histplot(df['col_name'], bins=50, color='red')
```

### Data Preparation

```
# Enumeration variables or Categorical variables
df['enu_value1'] = (df.enu_var == 'enu_value1').astype('int')
df['enu_value2'] = (df.enu_var == 'enu_value2').astype('int')

# one-hot encoding
category_columns = ['col1', 'col2', ..., 'coln']
for c in category_columns:
    for v in df[c].value_counts().head(5).index:
        df['%s_%s' % (c, v)] = (df[c] == v).astype('int')

# Regularization
XTX = XTX + np.eye(3) * 0.1
```

### Data Sampling
Split data into training set, valuation set, test set.

```
# 1, split the data into multiple parts

# 1.1
# total shuffle the df
df_shuffle = df.sample(frac=1, random_state=seed)
# split the df by index
df_part1 = df_shuffle.iloc[:1000]
df_part2 = df_shuffle.iloc[1000:]

# 1.2
# shuffle the index
idx = np.arange(len(df))
np.random.seed(seed)
np.random.shuffle(idx)
# split the df by shuffled index
df_part1 = df.iloc[idx[:1000]]
df_part2 = df.iloc[idx[1000:]]

# 1.3
p = .2
msk = np.random.rand(len(df)) < p
df_part1 = df[msk]
df_part2 = df[~msk]

# 1.4
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=104, test_size=0.25, shuffle=True)
or
folds = train_test_split(range(len(df)), test_size=0.2, random_state=1)
df_part1 = df.iloc[folds[0]]
df_part2 = df.iloc[folds[1]]

# 2, only split the data into two parts

# get random 20% from df
df_part1 = df.sample(frac=0.2, random_state=seed)
# get the rest
df_part2 = df[~df.index.isin(df_part1.index)]
```

## Example

| |Linear Regression|Logistic Regression|Decision Tree|XGBoost|
|---|---|---|---|---|
|Single Machine|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/linear_regression_python.py'>linear_regression_python.py</a>| |
|scilit-learn|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/linear_regression_scikit.py'>linear_regression_scikit.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/logistic_regression_scikit.py'>logistic_regression_scikit.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/decision_tree_scikit.py'>decision_tree_scikit.py</a>|
|Spark|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/linear_regression_spark.py'>linear_regression_spark.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/logistic_regression_spark.py'>logistic_regression_spark.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/decision_tree_spark.py'>decision_teer_spark.py</a>|

### Linear Regression

```
# Equation
w0 + Xi1*w1 + Xi2*w2 + Xi3*w3 + ... + Xin*wn = yi
X.dot(w) = y
X.T.dot(X).dot(w) = X.T.dot(y)
w = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
```

#### Evaluation Metrics
- Mean Absolute Error (MAE)
- Mean Square Error (MSE)
- Root Mean Squared Error (RMSE)
- Coefficient of Determination (R-squared)

### Logistic Regression
- Logistic Regression = Linear Regression + sigmoid = [0, 1] = Yes or No

```
sigmoid = lambda x: 1 / (1 + np.exp(-x))
```

#### Evaluation Metrics
- Accuracy
- Precision = tp / (tp + fp)
- Recall = tp / (tp + fn)
- tp: True Positive, tn: True Negative, fp: False Positive, fn: False Negative

### Decision Tree
- Overfitting

### XGBoost
