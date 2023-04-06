#  MLPerf™ Inference Results in the MLCommons CM format

This is the repository containing results of the MLPerf™ Inference benchmark 
in the [MLCommons CM format](https://github.com/mlcommons/ck)
for the [Collective Knowledge Playground](https://github.com/mlcommons/ck/tree/master/platform)

For benchmark code and rules please see the [GitHub repository](https://github.com/mlcommons/inference).

#  How to re-generate

Install [MLCommons CM framework](https://github.com/mlcommons/ck/blob/master/docs/installation.md).

Pull CM repository with automation recipes:
```bash
cm pull repo mlcommons@ck
```

Install repositories with raw MLPerf inference benchmark results:
```bash
cm run script "get git repo _repo.https://github.com/mlcommons/inference_results_v2.0" --env.CM_GIT_CHECKOUT=master --extra_cache_tags=mlperf-inference-results,version-2.0
cm run script "get git repo _repo.https://github.com/mlcommons/inference_results_v2.1" --env.CM_GIT_CHECKOUT=master --extra_cache_tags=mlperf-inference-results,version-2.1
cm run script "get git repo _repo.https://github.com/mlcommons/inference_results_v3.0" --env.CM_GIT_CHECKOUT=master --extra_cache_tags=mlperf-inference-results,version-3.0
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
