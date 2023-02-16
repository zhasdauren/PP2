import json

f = open('sample-data.json')

data = json.load(f)
print(data['imdata'][0]['l1PhysIf']['attributes']['autoNeg'])

# x = json.loads(data)
# print(x['totalCount'])