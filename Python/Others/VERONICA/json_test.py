import json
from datetime import datetime, timedelta

with open('var.json', 'r') as file:
  data = json.load(file)
  data["today"] = data["tomorrow"].copy()
  data["tomorrow"]["date"] = (datetime.now()+timedelta(1)).date().isoformat()

with open('var.json', 'w') as file:
  json.dump(data, file, indent=2)
