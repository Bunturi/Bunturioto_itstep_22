import json

# Open the JSON file for reading
with open("movies.json", "r", encoding="utf-8") as read_json:
    python_data = json.load(read_json)