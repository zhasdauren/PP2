import json

f = open('sample-data.json')

data = json.load(f)
print(data['totalCount'])

# x = json.loads(data)
# print(x['totalCount'])