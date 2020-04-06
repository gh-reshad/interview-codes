from google.cloud import bigquery
from google.cloud import storage
import os

def implicit():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)


#Path to the google credentials file.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\100689998\Documents\python-scripts\Interview-codes\horizontal-ray-245215-61f00bf119a8.json"
#creating a client object
client = bigquery.Client()

#construct a refrence to the 'hacker news' dataset
dataset_ref = client.dataset("hacker_news", project="bigquery-public-data")

#API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

#List all the tables in the 'hacker news' dataset
tables = list(client.list_tables(dataset))

#Print the name of all the tables in the dataset
for table in tables:
    print(table.table_id)


#cinstruct a refrence to the 'full' table
table_ref = dataset_ref.table('full')

#API request - fetch the table
table = client.get_table(table_ref)

#print(table.schema)

#Preview the first five lines of the 'full' table
print(client.list_rows(table, max_results=5).to_dataframe())

#Preview the first five enteries in the 'by' columnn of the 'full' table
print(client.list_rows(table, selected_fields=table.schema[:1], max_results=5).to_dataframe())



