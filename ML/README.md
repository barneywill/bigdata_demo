
# Machine Learning

| |Index|
|---|---|
|1|[Process](#process)|
|2|[Steps](#step)|
|3|[Models](#model)|
|4|[Concepts](#concept)|
|5|[Techniques](#tech)|
|6|[Examples](#example)|

## <a id='process'></a>1 Process
### Training
Features(Input) + Targets(Desired Output) -> Machine Learning -> Model
### Prediction
Features(Input) + Model -> Predicitions(Output)

## <a id='step'></a>2 Steps
- Business Understanding: Goal, Measurable
  - Identify the business problem, understand how we can solve it
  - Will Mechine Learning help?
  - If not, propose an alternative solution
  - Define the goal which has to be measurable
- Data Understanding: Avial data sources, Data quality
  - Analyze available data sources, decide if we need to get more data
  - Is it reliable?
  - Is the dataset large enough?
  - Do we need to get more data?
  - It may influence the goal
- Data Preparation: Clean, Transform, Feature Engineering, Data Sampling
  - Transform the data so it can be put into a ML algorithm
  - Clean the data
  - Build the pipelines
  - Convert into tabular form
- Modeling: Train and choose the best model
  - Training the models: the actual Machine Learning happens here
  - Try different models: Logistic regression, Decision tree, Neural network
  - Go back: Add new features, Fix data issues
  - Select the best one
- Evaluation: Offline and Online
  - Measure how well the model solves the business problem
  - Is the model good enough?
  - Have we reached the goal?
  - Do our metrics improve?
  - Was the goal achievable?
  - Did we solve/measure the right thing?
- Deployment
  - Deploy the model to production
  - Roll the model to all users
  - Proper monitoring
  - Ensuring the quality and maintainability

## <a id='model'></a>3 Models
- Regression: Linear Regression, Decision Tree Regression, XGBoost Regression
  - Regression algorithms are used to predict the continuous values such as price, salary, age, etc.
- Classification: Logistic Regression, Decision Tree Classifier, XGBoost Classifier, SVM
  - Classification algorithms are used to predict/Classify the discrete values such as Male or Female, True or False, Spam or Not Spam, etc.
  - Binomial vs Multinomial
- Clustering: K-Means, DBSCAN
- Recommendation: Collaborative Filtering(User & Item based)
  - Recommendation algorithms are used to find different top-N items for each individual user.

## <a id='concept'></a>4 Concepts
- X, y
- train, test
- feature, label
- model, fit, transform, metrics
- pipeline, transformers, estimators

## <a id='tech'></a>5 Techniques

### 5.1 Free Dataset
- https://www.kaggle.com/
- from sklearn.datasets import load_diabetes

### 5.2 Python Library

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

### 5.3 Jupyter Notebook

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

### 5.4 Data Exploration

```
# all data
df
# data types
df.dtypes
# number data statistics
df.describe()
df.describe(include='all')
# null data
df.isnull().sum()
df.isna().sum()
# unique and count
df['col_name'].unique()
df['col_name'].nunique()
df.nunique()
# distribution
df['col_name'].value_counts()
df.groupby(['col_name']).size().reset_index(name='count').sort_values('count', ascending=False).iloc[:10]
# graphic distribution
sns.histplot(df['col_name'], bins=50, color='red')
```

### 5.5 Data Preparation
Models can only work with numbers.
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

### 5.6 Data Sampling
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

### 5.7 Feature importance analysis
- Difference
  - Global - Group
- Ratio
  - Group / Global

```
from IPython.display import display

global = df.col.mean()
categorical_cols = ['col1', 'col2', 'col2']
for c in categorical_cols:
    print(c)
    df_group = df.groupby(c).col.agg(['mean', 'count'])
    df_group['diff'] = group - global
    df_group['ratio'] = group / global
    display(df_group)
    print()
```

#### Mutual information (Categorical)
The mutual information(MI) of two random variables is a measure of mutual dependence between the two variables.

```
from sklearn.metrics import mutual_info_score

mutual_info_score(df.col1, df.col2)

def mutual_info_score_by_column(col):
  return mutual_info_score(col, df.col1)
df[categorical_cols].apply(mutual_info_score_by_column).sort_values(ascending=False)
```

#### Correlation (Numerical)
Correlation coefficient is a measure of linear correlation between two sets of data.

```
df[numerical].corrwith(df.col1)
```

### 5.8 Cross validation

```
from sklearn.model_selection import KFold
from tqdm.auto import tqdm
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
scores = []
for train_idx, val_idx in tqdm(kfold.split(df), total=5):
    df_train = df.iloc[train_idx]
    df_val = df.iloc[val_idx]
    model = train(df_train, y_train)
    y_pred = model.predict(df_val)
    auc = roc_auc_score(y_val, y_pred)
    scores.append(auc)

np.mean(scores), np.std(scores)
```

## <a id='example'></a>6 Examples

| |Linear Regression|Logistic Regression|Decision Tree|XGBoost|
|---|---|---|---|---|
|Single Machine|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/linear_regression_python.py'>linear_regression_python.py</a>| |
|scikit-learn|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/linear_regression_scikit.py'>linear_regression_scikit.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/logistic_regression_scikit.py'>logistic_regression_scikit.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/decision_tree_regression_scikit.py'>decision_tree_regression_scikit.py</a><br><a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/decision_tree_classification_scikit.py'>decision_tree_classification_scikit.py</a>
|XGBoost| | | |<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/xgboost_regression.py'>xgboost_regression.py</a><br><a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/xgboost_classification.py'>xgboost_classification.py</a>|
|Spark|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/linear_regression_spark.py'>linear_regression_spark.py</a><br><a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/scala/LinearRegressionSpark.scala'>LinearRegressionSpark.scala</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/logistic_regression_spark.py'>logistic_regression_spark.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/decision_tree_regression_spark.py'>decision_teer_regression_spark.py</a><br><a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/decision_tree_classification_spark.py'>decision_teer_classification_spark.py</a><br><a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/scala/DecisionTreeClassificationSpark.scala'>DecisionTreeClassificationSpark.scala</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/xgboost_regression_spark.py'>xgboost_regression_spark.py</a><br><a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/xgboost_classification_spark.py'>xgboost_classification_spark.py</a><br><a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/scala/XGBoostRegressionSpark.scala'>XGBoostRegressionSpark.scala</a>|
|Bigquery|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/bigquery/linear_regression_bigquery.sql'>linear_regression_bigquery.sql</a>|

### 6.1 Linear Regression

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

### 6.2 Logistic Regression
- Logistic Regression = Linear Regression + sigmoid = [0, 1] = Yes or No

```
sigmoid = lambda x: 1 / (1 + np.exp(-x))
```

#### Evaluation Metrics
Confusion table
- Accuracy
  - vs Dummy model
- Precision = tp / (tp + fp)
- Recall = tp / (tp + fn)
  - tp: True Positive, tn: True Negative, fp: False Positive, fn: False Negative

```
confusion_matrix / confusion_matrix.sum()
```

### 6.3 Decision Tree
- max_depth
- min_samples_leaf

#### Evaluation Metrics
- ROC: Receiver-operating Characteristic Curve
- AUC: Area Under the roc Curve
  - TPR: True Positive Rate, FPR: False Positive Rate
  - FPR = fp / (tn + fp)
  - TPR = tp / (fn + tp)

```
from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve(y_val, y_pred)
plt.figure(figsize=(5, 5))
plt.plot(fpr, tpr, label='Model')
plt.plot([0, 1], [0, 1], label='Random', linestyle='--')
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.legend()
```

![decision tree](https://github.com/barneywill/bigdata_demo/blob/main/imgs/decision_tree.jpg)

### 6.4 XGBoost
- Tuning
  - eta: learning rate, default=0.3
  - max_depth: default=6
  - min_child_weight: min_samples_leaf in RF, default=1

![xgboost](https://github.com/barneywill/bigdata_demo/blob/main/imgs/xgboost_model.jpg)

## 7 Deploy

### 7.1 Save & Load the model

```
import pickle
model_file = 'lr_model_C=%.bin' % C

f_out = open(model_file, 'wb')
pickle.dump((dv, model), f_out)
f_out.close()

with open(model_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)
```

### 7.2 Flask

```
from flask import Flask
from flask import request
from flask import jsonify

app = Flask('ping')

@app.route('/ping', methods=['POST'])
def ping():
    json = request.get_json()
    result = {'a':1, 'b':2}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
```

```
pip install flask
python ping.py

pip install gunicorn
gunicorn --bind=0.0.0.0:9000 ping:app
```

```
import requests
url = 'http://ping'
json = '{"a":1}'
request.post(url, json=json).json()
```

### 7.3 Virtual environment

#### conda

#### pipenv

```
pip install pipenv
pipenv install numpy scikit-learn==0.24.2 flask gunicorn
pipenv shell
which python
echo $PATH
```

#### docker
Dockfile
```
FROM python:3.8.12-slim
RUN pip install pipenv
WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]
RUN pipenv install --system --deploy 
COPY ["app.py", "model.bin", "./"]
EXPOSE 9000
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9000", "ping:app"]
```
docker build -t test-img .
