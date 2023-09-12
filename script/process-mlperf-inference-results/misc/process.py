from pathlib import Path
import sys
import json
import os

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

result_type = os.environ.get('CM_MLPERF_RESULT_TYPE', 'inference')

for path in Path('experiment').rglob("cm-result.json"):

    if 'mlperf-inference' not in str(path):
        continue

    if '-all-' not in str(path) and '-v3.1-' not in str(path):
        continue

    print (path)

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

    if result_type == "inference":
        for result in final_result:
            if result.get('has_power', False):
                result_power = result.get('Result_Power', '')

                scenario = result.get('Scenario', '').lower()

                if scenario == 'offline':
                    infs_per_second = result.get('Result')
                    if not infs_per_second or not result_power:
                        continue
                    inference_per_joule = infs_per_second / result_power

                if scenario in ['singlestream', 'multistream']:
                    latency_per_inference = result.get('Result')
                    result_power_units = result.get('Result_Power_Units')
                    if not latency_per_inference or not result_power or not result_power_units:
                        continue
                    if result_power_units == "millijoules":
                        inference_per_joule = 1000 / result_power if scenario == 'singlestream' else 8000/result_power
                    else:
                        continue
                else:
                    continue

                result['Inference_per_Joule'] = inference_per_joule

    if result_type == "tiny":
        pass

    with open(path, "w") as outfile:
        print(json.dumps(final_result, indent=2), file=outfile)



