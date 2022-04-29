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

# Function that returns a column for a table


def get_columns_for_table(table):
    columns = []
    for column in table.columns:
        columns.append(column['name'])
    return columns

# Function that returns each column in a datamodel as a dictionary
def get_columns_for_model(model):
    columns = {}
    for table in model.tables:
        specific_table = []
        for column in table.columns:
            specific_table.append(column['name'])
        columns[table.name] = specific_table
    return columns


# Function that takes in a table name and column name then returns a PQL query that will return the data in the table with the column name
def get_query(table, column):
    q = pql.PQL()
    q += pql.PQLColumn(f"VARIANT({table}.{column})", "Variant")
    q += pql.PQLColumn(
        "CLUSTER_VARIANTS( VARIANT({table}.{column}), 2, 2)", "Cluster")
    return q


""" print((get_tables(model)))
print((get_columns(model))) 
print(get_query("_CEL_P2P_ACTIVITIES_EN_parquet", "_CASE_KEY"))"""

# Function that takes in a model then returns get_query for each get_tables of the model


def get_queries(model):
    queries = []
    for table in get_tables(model):
        for column in get_columns(model):
            queries.append(get_query(table, column))
    return queries

# Function that executes model.get_data_frame on each query outputed by get_queries


def get_data(model):
    data = []
    for query in get_queries(model):
        model.get_data_frame(query).to_csv(f"{query}.csv")


# get_data(model)

""" q = pql.PQL()
q += pql.PQLColumn("VARIANT(_CEL_P2P_ACTIVITIES_EN_parquet.ACTIVITY_EN)", "Variant")
q += pql.PQLColumn("CLUSTER_VARIANTS( VARIANT(_CEL_P2P_ACTIVITIES_EN_parquet.ACTIVITY_EN), 2, 2)", "Cluster")"""

#df = model.get_data_frame(q)

# df.to_csv("clusterized_test.csv")
