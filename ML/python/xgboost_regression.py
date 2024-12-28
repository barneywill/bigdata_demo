import xgboost as xgb
import pandas as pd
from numpy import absolute

from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split, cross_val_score, RepeatedKFold
from sklearn.metrics import mean_absolute_error, roc_auc_score, roc_curve, auc, accuracy_score

# 1 Data preparation
file_path = '/path/to/a/csvfile'
feature_columns = ['feature1', 'feature2', 'feature3', 'featuren']
label_column = 'label'
df = pd.read_csv(file_path)
dv = DictVectorizer()

# 2 Split train set and test set
folds = train_test_split(range(len(df)), test_size=0.2, random_state=1)
X_train = df[feature_columns].fillna(0).iloc[folds[0]]
y_train = df[label_column].iloc[folds[0]].values
X_test = df[feature_columns].fillna(0).iloc[folds[1]]
y_test = df[label_column].iloc[folds[1]].values

# 3 Train
X_train = dv.fit_transform(X_train.to_dict(orient='records'))
xgb_params = {
    'eta': 0.3,
    'max_depth': 6,
    'min_child_weight': 1,
    'objective': 'binary:logistic',
    'eval_metric': 'mae',
    'nthread': 4,
    'seed': 1,
    'verbosity': 1,
    'n_estimators': 1000
}

# 3.1
model = xgb.XGBRegressor(**xgb_params)
# not necessary
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
scores = cross_val_score(model, X_train, y_train, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)
scores = absolute(scores)
print('Mean MAE: %.3f (%.3f)' % (scores.mean(), scores.std()) )

model.fit(X_train, y_train)

# 4.1
X_test = dv.transform(X_test.to_dict(orient='records'))
y_predict = model.predict(X_test)



# 3.2
d_train = xgb.DMatrix(X_train, label=y_train, feature_names=dv.get_feature_names())
d_test = xgb.DMatrix(X_test, feature_names=dv.get_feature_names())
d_model = xgb.train(xgb_params, d_train, num_boost_round=10, evals=[(d_train, 'train'), (d_test, 'test')])

# 4.2
y_predict = d_model.predict(d_test)

# 4 Evaluation
roc_auc_score = roc_auc_score(y_test, y_predict)
