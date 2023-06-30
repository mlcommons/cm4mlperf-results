# Updating MLPerf results in the CM format

Update your update logic [here](customize.py) and then run:


```bash
cmr "process mlperf results _tiny"
cmr "process mlperf results _training"
cmr "process mlperf results _inference"
```
