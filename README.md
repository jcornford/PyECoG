[![PyPI version](https://badge.fury.io/py/pyecog.svg)](https://badge.fury.io/py/pyecog)
## PyECoG
This module is for detecting epileptiform activity from *single* channel intracranial EEG (or ECoG) recordings.
Currently under heavy construction! 

### Installing PyECoG
```{bash}
pip install pyecog
```

##### Installing PyQt4
You will also need to install PyQt4 to use the gui elements:
Unfortunately PyQt4 cannot be installed from pip (http://stackoverflow.com/questions/22640640/how-to-install-pyqt4-on-windows-using-pip), you will need to install from here
https://riverbankcomputing.com/software/pyqt/download

##### Installing Pomegranate
This is required for the Hidden Markov decoding of classifier predictions. There are sometimes issues (on a mac)
```python
38 from .hmm import *
...
ImportError: No module named utils
```
When installing on a conda environment. (https://github.com/jmschrei/pomegranate/issues/114)

```bash
pip uninstall pomegranate
pip install pomegranate --no-cache-dir
```
On windows you will also need to install visual studio in order to install pomegranate.

### How to use
- [Loading ndf files] (https://github.com/jcornford/pyecog/blob/master/documentation_notebooks/demo_loading_ndfs_notebook.ipynb)

### Repository contents:
* NDF:          code is the current working directory.
* light_code:   contains old code. PyECoG was originally "networkclassifer", this is that code, kept for analysing further experiments.
* visualisation: contains a bunch of visualisation experiments




