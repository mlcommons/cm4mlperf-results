from pathlib import Path
import sys
import json

def merge_result(processed, res):
    index = res['url']
    if index not in processed:
        processed[index] = res
        return
    for key in res:
        if key == "Result_Units" and res[key] in ["Watts", "millijoules"]:
            val = res[key]
            key = "Result_Power_Units"
        else:
            val = res[key]

        if key not in processed[index]:
            processed[index][key] = val
        
for path in Path('experiment').rglob("cm-result.json"):

    with open(path) as json_data:
        data = json.load(json_data)

    locations = []
    for res in data:
        if res['url'] not in res:
            locations.append(res['url'])

    processed={}
    for res in data:
        merge_result(processed, res)
    final_result = []

    for loc in locations:
        cur_res = {}
        for key in processed[loc]:
            cur_res[key] = processed[loc][key]
        final_result.append(cur_res)

    with open(path, "w") as outfile:
        print(json.dumps(final_result, indent=2), file=outfile)



