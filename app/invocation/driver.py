import requests
import os
import json

# api_key = os.environ.get('LICHESS_OAUTH_TOKEN')
# payload = {}
#
# # Make GET request to Lichess API
# resp = requests.request(
#     "GET",
#     url='https://lichess.org/api/games/user/NHorde',
#     data=payload,
#     params={
#         'pgnInJson': True,
#         'max': 2,
#         'evals': False,
#         'moves': True,
#         'opening': True
#     }
# )
#
# resp_json = []
# ndjson = resp.content.decode().split('\n')
#
# for json_obj in ndjson:
#     if json_obj:
#         resp_json.append(json_obj)
# #
# # for i in resp_json:
# #     if "1. " in i:
# #         print(i)
#
# print(resp.content)



import requests, json

headers = {
    "accept":"application/x-ndjson"
}

url = "https://www.lichess.org/api/games/user/nhorde"

r = requests.get(url,
                 params={"max":1, "perfType":"rapid","analysed":"false", "clocks":"false", "evals":"false", "opening":"true"},
                 headers=headers)
r_text = r.content.decode("utf-8")

games = [json.loads(s) for s in r_text.split("\n")[:-1]]

print(json.dumps(games, indent=3))