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


def get_table_names(model):
    """
    get_table_names gets the names of the tables in a model.

    :param model: datamodel from the celonis api
    :return: list of table names in the model
    """
    return [table.name for table in model.tables]


def get_tables(model):
    # get_tables takes in a datamodel and returns the tables in the model
    return model.tables


def get_columns_for_table(table):
    # get_columns_for_table takes in a datamodeltable and returns a list of columbs for the table
    return table.columns


def get_columns_for_model(model):
    """
    get_columns_for_model gets all columns from a celonis datamodel.

    :param model: datamodel from the celonis api
    :return: dictionary with table names as keys and lists of column names as values
    """
    columns = {}
    for table in model.tables:
        specific_table = [column['name'] for column in table.columns]
        columns[table.name] = specific_table
    return columns


def generate_query(table_name, column_name):
    """
    generate_query generates a query for a specific table and column.

    :param table_name: name of a table in the datamodel
    :param column_name: name of a column in the table
    :return: query for the table and column
    """
    q = pql.PQL()
    q += pql.PQLColumn(f"VARIANT({table_name}.{column_name})", "Variant")
    q += pql.PQLColumn(
        f"CLUSTER_VARIANTS( VARIANT({table_name}.{column_name}), 2, 2)", "Cluster")
    return q


def get_queries(model):
    """
    get_queries gets all possible queries for a celonis datamodel.

    :param model: datamodel from the celonis api
    :return: list of queries
    """
    queries = []
    for table in get_tables(model):
        queries.extend(generate_query(
            table.name, column['name']) for column in get_columns_for_table(table))

    return queries


def get_data(model):
    """
    get_data gets all data from a celonis datamodel and saves them as a csv.

    :param model: datamodel from the celonis api
    :return: none
    """
    data = []
    for query in get_queries(model):
        model.get_data_frame(query).to_csv(f"{query}.csv")


q = pql.PQL()
#q += pql.PQL(f"TABLE {get_tables(model)[0]}")
#q += pql.PQL(f"SELECT * from {get_tables(model)[0]};")


q += pql.PQLColumn(
    f"VARIANT({get_table_names(model)[0]}.{get_columns_for_table(get_tables(model)[0])[2]['name']})", "Variant")
q += pql.PQLColumn(
    f"CLUSTER_VARIANTS( VARIANT({get_table_names(model)[0]}.{get_columns_for_table(get_tables(model)[0])[2]['name']}), 2, 2)", "Cluster")

df = model.get_data_frame(q)
print(df)
df.to_csv("clusterized_test.csv")
