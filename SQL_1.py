from google.cloud import bigquery
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\100689998\Documents\python-scripts\Interview-codes\horizontal-ray-245215-61f00bf119a8.json"

client = bigquery.Client()

dataset_ref = client.dataset('openaq', project='bigquery-public-data')

dataset = client.get_dataset(dataset_ref)

tables = list(client.list_tables(dataset))

num_tables = len(tables)

# print(num_tables)

# for table in tables:
#     print(table.table_id)


table_ref = dataset_ref.table('global_air_quality')

table = client.get_table(table_ref)
# Preview the first five lines of the "global_air_quality" table
#print(client.list_rows(table, max_results=5).to_dataframe())

#print(table.schema)

#print(client.list_rows(table).to_dataframe())

# query = """
#         SELECT city
#         FROM `bigquery-public-data.openaq.global_air_quality`
#         WHERE country = 'US'
#         """

# client = bigquery.Client()

# #Set up the query
# query_job = client.query(query)

# #API request - run the query, and return a pandas DataFrame
# us_cities = query_job.to_dataframe()

# print(us_cities)

query = """
        SELECT country
        FROM `bigquery-public-data.openaq.global_air_quality`
        WHERE unit = "ppm"
        """

client = bigquery.Client()
query_job = client.query(query)
ppm_unit = query_job.to_dataframe()
print(ppm_unit)