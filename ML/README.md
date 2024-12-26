
# Machine Learning

## Process
### Training
Features(Input) + Targets(Desired Output) -> Machine Learning -> Model
### Prediction
Features(Input) + Model -> Predicitions(Output)

## Steps
- Business Understanding: Goal, Measurable
- Data Understanding: Avial data sources, Data quality
- Data Preparation: Clean, Transform, Features
- Modeling: Choose the best model
- Evaluation: Offline and Online, Accuracy, Precision, Recall
- Deployment

## Type
- Regression
- Classification
- Clustering
- Recommendation

## Jupyter Notebook

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
```

## Data Exploration

```
# all data
df
# number data
df.describe()
# null data
df.isnull().sum()
# unique and count
df['col_name'].unique()
df['col_name'].nunique()
# distribution
df.groupby(['col_name']).size().reset_index(name='count').sort_values('count', ascending=False).iloc[:10]
# graphic distribution
sns.histplot(df['col_name'], bins=50)
```

## Example: Taxi Tip Forecast


