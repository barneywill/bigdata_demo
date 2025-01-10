# Airflow

Apache Airflow™ is an open-source platform for developing, scheduling, and monitoring batch-oriented workflows. 

| |Index|
|---|---|
|1|[Install](#install)|
|2|[Run](#run)|
|3|[Open](#open)|
|4|[Roles(webserver, scheduler, worker)](#role)|
|5|[Concepts](#concept)|
|6|[Commands](#command)|

![Airflow Architecture](https://github.com/barneywill/bigdata_demo/blob/main/imgs/airflow_architecture.jpg)

## <a id='install'></a>1 Install

```
AIRFLOW_VERSION=2.10.4

# Extract the version of Python you have installed. If you're currently using a Python version that is not supported by Airflow, you may want to set this manually.
# See above for supported versions.
PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example this would install 2.10.4 with python 3.8: https://raw.githubusercontent.com/apache/airflow/constraints-2.10.4/constraints-3.8.txt

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

## <a id='run'></a>2 Run
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

## <a id='open'></a>3 Open
http://127.0.0.1:8080

![dag](https://github.com/barneywill/bigdata_demo/blob/main/imgs/dag.jpg)

Official: https://airflow.apache.org/docs/apache-airflow/stable/start.html


## <a id='role'></a>4 Roles(webserver, scheduler, worker)

### 4.1 webserver

### 4.2 scheduler
The Airflow scheduler monitors all tasks and all DAGs, and triggers the task instances whose dependencies have been met. Behind the scenes, it spins up a subprocess, which monitors and stays in sync with a folder for all DAG objects it may contain, and periodically (every minute or so) collects DAG parsing results and inspects active tasks to see whether they can be triggered.

### 4.3 worker
- SequentialExecutor: Airflow uses a sqlite database, which you should outgrow fairly quickly since no parallelization is possible using this database backend. It works in conjunction with the SequentialExecutor which will only run task instances sequentially.
- LocalExecutor: tasks will be executed as subprocesses;
- CeleryExecutor: one of the ways you can scale out the number of workers. For this to work, you need to setup a Celery backend (RabbitMQ, Redis, …) and change your airflow.cfg to point the executor parameter to CeleryExecutor and provide the related Celery settings.
- KubernetesExecutor

## <a id='concept'></a>5 Concept

### 5.1 DAG
In Airflow, a DAG – or a Directed Acyclic Graph – is a collection of all the tasks you want to run, organized in a way that reflects their relationships and dependencies.

### 5.2 Operator
An operator describes a single task in a workflow. Operators are usually (but not always) atomic, meaning they can stand on their own and don’t need to share resources with any other operators. The DAG will make sure that operators run in the correct certain order; other than those dependencies, operators generally run independently. In fact, they may run on two completely different machines.

### 5.3 Task
Once an operator is instantiated, it is referred to as a “task”. The instantiation defines specific values when calling the abstract operator, and the parameterized task becomes a node in a DAG.

### 5.4 DAG Run
A DAG Run is an object representing an instantiation of the DAG in time.

### 5.5 Task Instance
A task instance represents a specific run of a task and is characterized as the combination of a dag, a task, and a point in time. Task instances also have an indicative state, which could be “running”, “success”, “failed”, “skipped”, “up for retry”, etc.

## 6 <a id='command'></a>Commands
```
# test your code without syntax error
python ~/airflow/dags/$dag.py

# print the list of active DAGs
airflow list_dags

# prints the list of tasks the dag_id
airflow list_tasks $dag_id

# prints the hierarchy of tasks in the DAG
airflow list_tasks $dag_id --tree

# test your task instance
airflow test $dag_id $task_id 2025-01-01

# run your task instance
airflow run $dag_id $task_id 2025-01-01

# get the status of task
airflow task_state $dag_id $task_id 2025-01-01

# trigger a dag run
airflow trigger_dag $dag_id 2025-01-01

# get the status of dag
airflow dag_state $dag 2025-01-01

# run a backfill over 2 days
airflow backfill $dag_id -s 2025-01-01 -e 2025-01-02
```
