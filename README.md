#  MLPerf™ Inference Results in the MLCommons CM format

This is the repository containing aggregated results of the MLPerf™ Inference benchmark 
in the [MLCommons CM format](https://github.com/mlcommons/ck)
for the [Collective Knowledge Playground](https://x.cKnowledge.org)
being developed by the [MLCommons taskforce on automation and reproducibility](https://cKnowledge.org/mlcommons-taskforce).

It makes it easier to analyze MLPerf inference results, add derived metrics such as performance/Watt and constraints,
and link reproducibility reports as shown in these examples:
* [Power efficiency to compare Qualcomm, Nvidia and Sima.ai devices](https://cKnowledge.org/mlcommons-mlperf-inference-gui-derived-metrics-and-conditions)
* [Reproducibility report for Nvidia Orin](https://access.cknowledge.org/playground/?action=experiments&name=mlperf-inference--v3.0--edge--closed--image-classification--offline&result_uid=3751b230c800434a)

For benchmark code and rules please see the [GitHub repository](https://github.com/mlcommons/inference).

## How to import raw MLPerf results to CK/CM format

Install [MLCommons CM framework](https://github.com/mlcommons/ck/blob/master/docs/installation.md).

Pull CM repository with automation recipes:
```bash
cm pull repo mlcommons@ck
```

Install repositories with raw MLPerf inference benchmark results:
```bash
cm run script "get git repo _repo.https://github.com/mlcommons/inference_results_v2.0" --env.CM_GIT_CHECKOUT=master --extra_cache_tags=mlperf-inference-results,version-2.0
cm run script "get git repo _repo.https://github.com/mlcommons/inference_results_v2.1" --env.CM_GIT_CHECKOUT=master --extra_cache_tags=mlperf-inference-results,version-2.1
cm run script "get git repo _repo.https://github.com/mlcommons/inference_results_v3.0" --env.CM_GIT_CHECKOUT=main --extra_cache_tags=mlperf-inference-results,version-3.0
```

Convert raw MLPerf results into CM experiment entries:
```bash
cm run script "import mlperf inference to-experiment" 
```

Visualize results on your local machine via CK playground GUI:
```bash
cm run script "gui _playground"
```

These results are also available in the [public CK playground](https://x.cKnowledge.org).

## How to update MLPerf results for the CK playground

### Using your own python script

You can use this repository to fix, update and improve experimental results
by calculating and adding derived metrics (performance/watt)
or links to reproducibility reports that will be visible in a CK Playground GUI.

Install [MLCommons CM framework](https://github.com/mlcommons/ck/blob/master/docs/installation.md).

Pull CM repository with automation recipes and with MLPerf results in the CM format:
```bash
cm pull repo mlcommons@ck
cm pull repo mlcommons@cm_inference_results
```

Find CM entries with MLPerf v3.0 experiments from CMD:
```bash
cm find experiment --tags=mlperf-inference,v3.0
```

Find CM entries with MLPerf v3.0 experiments from Python:
```python
import cmind

r = cmind.access({'action':'find',
                  'automation':'experiment,a0a2d123ef064bcb',
                  'tags':'mlperf-inference,v3.0'})

if r['return']>0: cmind.error(r)

lst = r['list']

for experiment in lst:
    print (experiment.path)
```

### Using CM script

We created a [sample CM script](script/process-mlperf-inference-results) in this repository 
that you can use and [extend](script/process-mlperf-inference-results/customize.py) to add derived metrics:

```bash
cm run script "process mlperf-inference results" --experiment_tags=mlperf-inference,v3.0
```

# Contacts

This project is maintained by the [MLCommons taskforce on automation and reproducibility](https://cKnowledge.org/mlcommons-taskforce).
Join our [Discord server](https://discord.gg/JjWNWXKxwT) to ask questions, provide your feedback and participate in further developments.
