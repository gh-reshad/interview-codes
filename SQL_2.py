from google.cloud import bigquery
import os 


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\100689998\Documents\python-scripts\Interview-codes\horizontal-ray-245215-61f00bf119a8.json"
client = bigquery.Client()

dataset_ref = client.dataset('hacker_news', project='bigquery-public-data')

dataset = client.get_dataset(dataset_ref)

tables = list(client.list_tables(dataset))

# for table in tables:
#     print(table.table_id)

table_ref = dataset_ref.table('comments')

table = client.get_table(table_ref)

print(client.list_rows(table, max_results=5).to_dataframe())

# query = """
#         SELECT author, COUNT(1) AS NumPosts
#         FROM `bigquery-public-data.hacker_news.comments`
#         GROUP BY author
#         HAVING COUNT(1) > 10000
#         """

# Set up the query (cancel the query if it would use too much of 
# your quota, with the limit set to 1 GB)
# safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
# query_job = client.query(query, job_config=safe_config)

# profilic_commenters = query_job.to_dataframe()

# print(profilic_commenters.head())

query = """
        SELECT deleted, COUNT(1) AS NumDeleted
        FROM `bigquery-public-data.hacker_news.comments`
        GROUP BY deleted
        HAVING deleted = True
        """

safe_config = bigquery.QueryJobConfig(maximum_bytes_build = 10**10)
query_job = client.query(query, job_config=safe_config)

deleted_comments = query_job.to_dataframe()

print(deleted_comments.head())
