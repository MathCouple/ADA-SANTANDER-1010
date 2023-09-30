import os
import requests
import json
from datetime import datetime, timedelta

from dotenv import load_dotenv


load_dotenv()

dias_a_subtrair = 5
data_atual = datetime.now()

nova_data = data_atual - timedelta(days=dias_a_subtrair)
date_from = nova_data.strftime('%Y-%m-%d')
date_to = data_atual

KEYWORD = 'covid+medicina'
SORT_BY = 'popularity'
api_key = os.getenv('NEWS_API_ORG')
url = ('https://newsapi.org/v2/everything?'
       f'q={KEYWORD}&'
       f'from={date_from}&'
       f'to={date_to}&'
       f'sortBy={SORT_BY}&'
       f'apiKey={api_key}'
)


response = requests.get(url)
data_json = response.json()

print(json.dumps(data_json, indent=4))
