import sys
import json

def fill_values(data, values):
    if isinstance(data, dict):
        if "id" in data and "value" in data:
            if data["id"] in values:
                data["value"] = values[data["id"]]

        for item in data.values():
            fill_values(item, values)

    elif isinstance(data, list):
        for item in data:
            fill_values(item, values)

values_path = sys.argv[1]
tests_path = sys.argv[2] 
report_path = sys.argv[3]

with open(values_path, "r", encoding="utf-8") as file:
    values_data = json.load(file)

with open(tests_path, "r", encoding="utf-8") as file:
    tests_data = json.load(file)

values = {}

for item in values_data["values"]:
    values[item["id"]] = item["value"]

fill_values(tests_data, values)

with open(report_path, "w", encoding="utf-8") as file:
    json.dump(
        tests_data,
        file,
        ensure_ascii=False,
        indent=4
    )