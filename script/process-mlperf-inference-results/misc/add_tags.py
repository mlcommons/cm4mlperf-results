import cmind

def process():

    r = cmind.access({'action':'find',
                      'automation':'experiment'})

    if r['return']>0: return r

    lst = r['list']

    for e in lst:
        meta = e.meta
        tags = meta.get('tags',[])

        for t in ['mlperf-inference', 'mlperf-tiny', 'mlperf-training']:
            if t in tags:
                if 'mlperf' not in tags:
                    tags.insert(0, 'mlperf')

                    print (tags)
                    
                    meta['tags']=tags

                    e.update(meta, replace = True)

                    break


    return {'return':0}


if __name__ == "__main__":
   r = process()
   if r['return']>0: cmind.error(r)

