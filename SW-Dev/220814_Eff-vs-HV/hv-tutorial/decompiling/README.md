## recipe
### setup
```bash
conda create -n python-decompiler-py39 python=3.9
conda activate python-decompiler-py39
pip install uncompyle6
```

### decompile and translate to python3.9
```bash
uncompyle6 GEMDCSP5Monitor.pyc > GEMDCSP5Monitor.py
2to3-3.9 GEMDCSP5Monitor.py --write --nobackups --no-diffs
```

