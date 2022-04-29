from pycelonis import get_celonis
import os
from dotenv import load_dotenv

celonis = get_celonis(
    url=os.getenv("URL"),
    api_token=os.getenv("API_TOKEN")
)