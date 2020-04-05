from google.cloud import bigquery
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\100689998\Documents\python-scripts\Interview-codes\horizontal-ray-245215-61f00bf119a8.json"


client = bigquery.Client()

dataset_ref = client.dataset('chicago_taxi_trips', project='bigquery-public-data')

dataset = client.get_dataset(dataset_ref)

# tables = list(client.list_tables(dataset_ref))

# for table in tables:
#     print(table.table_id)

table_ref = dataset_ref.table('taxi_trips')

table = client.get_table(table_ref)

print(client.list_rows(table, max_results=5).to_dataframe())

