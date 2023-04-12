import cmind
import os

def preprocess(i):

    experiment_tags=i.get('input',{}).get('experiment_tags','')
    experiment_name=i.get('input',{}).get('experiment_name','')

    ii={'action':'find',
        'automation':'experiment,a0a2d123ef064bcb'}

    if experiment_name!='':
        ii['artifact']=experiment_name

    if experiment_tags!='':
        ii['tags']=experiment_tags
    else:
        ii['tags']='mlperf-inference'

    # Query CM to get experiment entries with MLPerf results
    r=cmind.access(ii)
    if r['return']>0: return r

    lst = r['list']

    for experiment in lst:
        print (experiment.path)

        # Do something with results ...

    return {'return':0}
