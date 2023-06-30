import cmind
import os
from pathlib import Path

def preprocess(i):

    env = i['env']
    
    ii={'action':'find',
        'automation':'experiment,a0a2d123ef064bcb'}

    experiment_name=i.get('input',{}).get('experiment_name','')
    if experiment_name!='':
        ii['artifact']=experiment_name

    experiment_tags=i.get('input',{}).get('experiment_tags','')
    if experiment_tags=='':
        experiment_tags=env.get('CM_MLPERF_RESULT_TYPE','')

    if experiment_tags!='':
        ii['tags']=experiment_tags
    else:
        ii['tags']='mlperf-inference'

    # Query CM to get experiment entries with MLPerf results
    r=cmind.access(ii)
    if r['return']>0: return r

    lst = r['list']

    for experiment in lst:
        print ('Processing experiment: {}'.format(experiment.path))

        # Do something with results ...

        for path in Path(experiment.path).rglob("cm-result.json"):

            r = cmind.utils.load_json(path)
            if r['return']>0: return r

            results = r['meta']

            updated = False

            for result in results:
                if experiment_tags == "mlperf-inference":
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

                        updated=True

            if updated:
                r=cmind.utils.save_json(path, results)
                if r['return']>0: return r

    return {'return':0}
