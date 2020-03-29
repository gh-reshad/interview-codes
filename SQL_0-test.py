from google.cloud import bigquery
import os

#Set credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\100689998\Documents\python-scripts\Interview-codes\horizontal-ray-245215-61f00bf119a8.json"


client = bigquery.Client()

dataset_ref = client.dataset('chicago_crime', project='bigquery-public-data')

#API
dataset = client.get_dataset(dataset_ref)

tables = list(client.list_tables(dataset))
# count = 0

# for table in tables:
    
#     print(table.table_id)
#     count += 1

# print(count)

num_tables = len(tables)
#print(num_tables)

table_ref = dataset_ref.table('crime')

table = client.get_table(table_ref)

#print(table.schema)
print(client.list_rows(table, max_results=5).to_dataframe())