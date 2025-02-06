import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import roc_auc_score, roc_curve, auc, accuracy_score
from sklearn import preprocessing
import pickle


# 1 Data preparation
file_path = '/path/to/a/csvfile'
feature_columns = 'feature1'
label_column = 'label'
df = pd.read_csv(file_path)
# if your label column is not numerical, you need to encode it
le = preprocessing.LabelEncoder()
tiv = TfidfVectorizer()

# 2 Split train set and test set
X_train, X_test, y_train, y_test = train_test_split(df[feature_columns], df[label_column], test_size=0.2, random_state=1)

# 3 Train
vectorizer = tiv.fit(X_train)
with open('dv.pkl', 'wb') as f:
    pickle.dump(vectorizer, f, pickle.HIGHEST_PROTOCOL)
X_train_ti = tiv.transform(X_train)
encoder = le.fit(y_train)
with open('enc.pkl', 'wb') as f:
    pickle.dump(encoder, f, pickle.HIGHEST_PROTOCOL)
y_train_le = le.transform(y_train)
svm_model = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
svm_model.fit(X_train_ti, y_train_le)

# 4 Evaluation
X_test_ti = tiv.transform(X_test)
y_test_le = le.transform(y_test)
y_predict = svm_model.predict(X_test_ti)

accuracy = accuracy_score(y_test_le, y_predict)

print("Accuracy:", accuracy)

encoder.inverse_transform(y_predict)

with open('dv.pkl', 'rb') as f:
    dv_load = pickle.load(f)
with open('enc.pkl', 'rb') as f:
    enc_load = pickle.load(f)