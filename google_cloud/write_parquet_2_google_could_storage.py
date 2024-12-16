import pandas as pd
import os

#pip install pyarrow
import pyarrow as pa
import pyarrow.parquet as pq

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
    
table_name = 'yellow_tripdata'

#write parquet table with partitions
def write_2_storage():
    data = get_df()
    table = pa.Table.from_pandas(data)
    gcs = pa.fs.GcsFileSystem()
    pq.write_to_dataset(table, 
                        root_path=f'{bucket_name}/{table_name}', 
                        partition_cols = ['tpep_pickup_date'],
                        filesystem = gcs)

if __name__ == '__main__':
    write_2_storage()