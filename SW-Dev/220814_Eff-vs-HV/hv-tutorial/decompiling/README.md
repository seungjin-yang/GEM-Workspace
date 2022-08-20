## recipe
### setup
```bash
conda create -n python-decompiler-py39 python=3.9
conda activate python-decompiler-py39
pip install uncompyle6
```

### decompile
```bash
uncompyle6 GEMDCSP5Monitor.pyc > GEMDCSP5Monitor.py
```

the output code has the wrong indent but `dbName` and `dbAccount` have been successfully restored.

- https://github.com/gem-dpg-pfa/P5GEMOfflineMonitor/blob/master/GEMDCSP5Monitor.py


```yaml
dbName: cms_omds_adg
dbAccount: CMS_COND_GENERAL_R/p3105rof@
```

