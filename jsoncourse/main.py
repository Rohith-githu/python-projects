import json

with open('app.json') as f:
  data = json.load(f)

print(data['email'])