from pycelonis import get_celonis
from pycelonis import pql

import os
from dotenv import load_dotenv

celonis = get_celonis(
    url=os.getenv("URL"),
    api_token=os.getenv("API_TOKEN")
)

model = celonis.datamodels.find("3630075d-34fc-4780-90b6-82f5372a7369")

q = pql.PQL()
q += pql.PQLColumn("VARIANT(_CEL_P2P_ACTIVITIES_EN_parquet.ACTIVITY_EN)", "Variant")
q += pql.PQLColumn("CLUSTER_VARIANTS( VARIANT(_CEL_P2P_ACTIVITIES_EN_parquet.ACTIVITY_EN), 2, 2)", "Cluster")

df = model.get_data_frame(q)

df.to_csv("clusterized.csv")

