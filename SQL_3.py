from google.cloud import bigquery
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\100689998\Documents\python-scripts\Interview-codes\horizontal-ray-245215-61f00bf119a8.json"

client = bigquery.Client()

dataset_ref = client.dataset('world_bank_intl_education', project='bigquery-public-data')

dataset = client.get_dataset(dataset_ref)

table_ref = dataset_ref.table('international_education')

table = client.get_table(table_ref)

#print(client.list_rows(table, max_results=5).to_dataframe())

# query = """ 
#         SELECT country_name, AVG(value) as avg_ed_spending_pct
#         FROM `bigquery-public-data.world_bank_intl_education.international_education`
#         WHERE indicator_code = 'SE.XPD.TOTL.GD.ZS' and year >= 2010 and year <= 2017
#         GROUP BY country_name
#         ORDER BY avg_ed_spending_pct DESC
#         """


query = """
        SELECT indicator_name, indicator_code , COUNT(1) AS num_rows
        FROM `bigquery-public-data.world_bank_intl_education.international_education`
        WHERE  year = 2016
        GROUP BY indicator_name, indicator_code
        HAVING num_rows >= 175
        ORDER BY num_rows DESC
        """


safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
query_job = client.query(query, job_config=safe_config)

country_result = query_job.to_dataframe()

print(country_result.head())


