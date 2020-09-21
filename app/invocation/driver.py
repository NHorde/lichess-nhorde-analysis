import requests
import os


api_key = os.environ.get('LICHESS_OAUTH_TOKEN')
payload = {}

# Make GET request to Lichess API
resp = requests.request(
    "GET",
    url='https://lichess.org/game/export/4KxbUGJv',
    data=payload,
    params={
        'pgnInJson': True,
        'evals': False,
        'clocks': False
    }
)

resp_json = []
ndjson = resp.content.decode().split('\n')

for json_obj in ndjson:
    if json_obj:
        resp_json.append(json_obj)

print(resp_json[-1])
