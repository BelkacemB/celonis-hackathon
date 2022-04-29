from pycelonis import get_celonis
from pycelonis import pql

import os
from dotenv import load_dotenv

celonis = get_celonis(
    url=("https://academic-b-berchiche-esi-dz.eu-2.celonis.cloud/"),
    api_token=("MDlhZjY4YWYtNjNiZC00MTg1LTg4YzUtYTRkZjkzZDE3ZDY1Ondrci9XYjA5Y2RTQXgwZk1mbHlvUkNmSHFTOVJNd0RydS9iZDFnaFB2cHRr"),
    key_type="USER_KEY"
)

model = celonis.datamodels.find("3630075d-34fc-4780-90b6-82f5372a7369")

""" # Function that takes a Celonis data model and uses the PQL query language to find all the data in the model then returns it as a list
def find_data(model):
    query = pql.Query(model)
    query.select("*")
    data = query.execute()
    return data

print(find_data("3630075d-34fc-4780-90b6-82f5372a7369")) """


# Function that takes in a model and returns the table names in the model
def get_tables(model):
    tables = []
    for table in model.tables:
        tables.append(table.name)
    return tables


print(get_tables(model))

# Function that returns each column in a table from a model.tables


def get_columns(model):
    columns = []
    for table in model.tables:
        for column in table.columns:
            columns.append(column['name'])
    return columns

# Function that takes in a table name and column name then returns a PQL query that will return the data in the table with the column name


def get_query(table, column):
    q = pql.PQL()
    q += pql.PQLColumn(f"VARIANT({table})", "Variant")
    q += pql.PQLColumn("CLUSTER_VARIANTS( VARIANT({table}), 2, 2)", "Cluster")


""" q = pql.PQL()
q += pql.PQLColumn("VARIANT(_CEL_P2P_ACTIVITIES_EN_parquet.ACTIVITY_EN)", "Variant")
q += pql.PQLColumn("CLUSTER_VARIANTS( VARIANT(_CEL_P2P_ACTIVITIES_EN_parquet.ACTIVITY_EN), 2, 2)", "Cluster")"""

#df = model.get_data_frame(q)

# df.to_csv("clusterized_test.csv")
