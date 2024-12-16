import pandas as pd
import os

#pip install pandas_gbq
import pandas_gbq as gbq

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/to/your/credentials.json'

bucket_name = 'test-bucket-1'
file_name = 'yellow_tripdata_2019-01.csv'

#read csv
def get_df() -> pd.DataFrame:
    data = pd.read_csv(f"gs://{bucket_name}/{file_name}")
    data.tpep_pickup_datetime = pd.to_datetime(data.tpep_pickup_datetime)
    data.tpep_dropoff_datetime = pd.to_datetime(data.tpep_dropoff_datetime)
    data['tpep_pickup_date'] = data['tpep_pickup_datetime'].dt.date
    data.columns = (data.columns
                    .str.replace(' ', '_')
                    .str.lower())
    return data

project_id = 'my_project_id'
table_id = 'ny_taxi.yellow_tripdata'

#write to a bigquery table
def write_2_bigquery():
    data = get_df()
    gbq.to_gbq(data, table_id, project_id=project_id)

if __name__ == '__main__':
    write_2_bigquery()