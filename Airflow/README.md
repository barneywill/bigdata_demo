# Install

```
AIRFLOW_VERSION=2.10.4

# Extract the version of Python you have installed. If you're currently using a Python version that is not supported by Airflow, you may want to set this manually.
# See above for supported versions.
PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example this would install 2.10.4 with python 3.8: https://raw.githubusercontent.com/apache/airflow/constraints-2.10.4/constraints-3.8.txt

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

# Run
```
# put your py files under this directory
mkdir -p ~/airflow/dags

export AIRFLOW_HOME=~/airflow
airflow standalone
```

if you don't want the default examples, modify $AIRFLOW_HOME/airflow.cfg
```
# Whether to load the DAG examples that ship with Airflow. It's good to
# get started, but you probably want to set this to ``False`` in a production
# environment
#
# Variable: AIRFLOW__CORE__LOAD_EXAMPLES
#
load_examples = false
```

if you forget your password
```
airflow users delete -u admin
airflow users create --username admin --password admin --role Admin --firstname admin --lastname admin --email admin@admin.com
```

# Open
http://127.0.0.1:8080


![dag](https://github.com/barneywill/bigdata_demo/blob/main/imgs/dag.jpg)

Official: https://airflow.apache.org/docs/apache-airflow/stable/start.html