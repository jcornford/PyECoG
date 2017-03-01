[![PyPI version](https://badge.fury.io/py/pyecog.svg)](https://badge.fury.io/py/pyecog)
## PyECoG
This module is for detecting epileptiform activity from *single* channel intracranial EEG (or ECoG) recordings.
Currently under heavy construction!

Strongly recommended to use python 3.6, untested and likely (more) buggy with 2. 

### Installing PyECoG


1. Install miniconda. Choose the Python 3.6 64-bit version for your operating system (Linux, Windows, or OS X).
2. Download the [environment file](https://github.com/mikailweston/pyecog/blob/master/environment.yml)
3. Open a terminal (on Windows, cmd) in the directory where you saved the file and type:
```{bash}
conda env create -n pyecog
source activate pyecog  or  activate pyecog on windows
pip install pyecog
```
### How to use
- [Loading ndf files] (https://github.com/jcornford/pyecog/blob/master/documentation_notebooks/demo_loading_ndfs_notebook.ipynb)

### Repository contents:
* NDF:          code is the current working directory.
* light_code:   contains old code. PyECoG was originally "networkclassifer", this is that code, kept for analysing further experiments.
* visualisation: contains a bunch of visualisation experiments




