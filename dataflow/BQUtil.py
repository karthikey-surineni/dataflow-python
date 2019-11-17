from apache_beam.io.gcp.internal.clients import bigquery
import os
import json
import re

class BQUtil:
    def __init__(self):
        self.home_dir = "/Users/karthikeysurineni/dataflow-python/"
        self.schema_dir = self.home_dir+"infrastructure/BigQuery/schema/"

    def extract_bq_assets(self,full_bq_table_path):
        bq_asset_map = {}
        bq_asset_map['project_id'] = full_bq_table_path.split(":")[0]
        dataset_table = full_bq_table_path.split(":")[1]
        bq_asset_map['dataset_id'] = dataset_table.split(".")[0]
        bq_asset_map['table_id'] = dataset_table.split(".")[1]
        return bq_asset_map

    def get_table_reference(self,full_bq_table_path):
        bq_asset_map = self.extract_bq_assets(full_bq_table_path)

        table_spec = bigquery.TableReference(
        projectId=bq_asset_map['project_id'],
        datasetId=bq_asset_map['dataset_id'],
        tableId=bq_asset_map['table_id'])

        return table_spec

    def get_table_schema(self,full_bq_table_path):
        bq_asset_map = self.extract_bq_assets(full_bq_table_path)
        dataset_table = bq_asset_map['dataset_id']+"-"+bq_asset_map['table_id']
        print(dataset_table)
        for file in os.listdir(self.schema_dir):
            if dataset_table in file:
                with open(self.schema_dir+file,'r') as rf:
                    all_lines = rf.read()
                    # print(all_lines)
                    schema=json.loads(all_lines)
                    # print(v[0])
                    # print(json.dumps(schema,indent=4))
                    return {'fields':schema}

    def parse_method(self, schema, string_input):
        header_row = "("
        print(string_input)
        # values = re.split("|",re.sub('\r\n', '', re.sub(u'"', '', string_input)))
        values = string_input.split("|")
        header_row = []
        for field in schema['fields']:
            header_row.append(field['name'])
        row = zip(header_row,values)
        # print(dict(row))
        return dict(row)