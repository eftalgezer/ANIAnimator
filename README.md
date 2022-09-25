# ANIAnimator
[![PyPI version](https://badge.fury.io/py/ANIAnimator.svg)](https://badge.fury.io/py/ANIAnimator)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ANIAnimator.svg)](https://pypi.python.org/pypi/ANIAnimator/)
[![Python package](https://github.com/eftalgezer/ANIAnimator/actions/workflows/python-package.yml/badge.svg)](https://github.com/eftalgezer/ANIAnimator/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/gh/eftalgezer/ANIAnimator/branch/main/graph/badge.svg?token=Q9TJFIN1U1)](https://codecov.io/gh/eftalgezer/ANIAnimator)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/4ff526bd45e642bb81b300f2243baef2)](https://www.codacy.com/gh/eftalgezer/ANIAnimator/dashboard?utm_source=github.com&utm_medium=referral&utm_content=eftalgezer/ANIAnimator&utm_campaign=Badge_Coverage)
[![PyPI download month](https://img.shields.io/pypi/dm/ANIAnimator.svg)](https://pypi.python.org/pypi/ANIAnimator/)
[![PyPI download week](https://img.shields.io/pypi/dw/ANIAnimator.svg)](https://pypi.python.org/pypi/ANIAnimator/)
[![PyPI download day](https://img.shields.io/pypi/dd/ANIAnimator.svg)](https://pypi.python.org/pypi/ANIAnimator/)
![GitHub all releases](https://img.shields.io/github/downloads/eftalgezer/ANIAnimator/total?style=flat)
[![GitHub contributors](https://img.shields.io/github/contributors/eftalgezer/ANIAnimator.svg)](https://github.com/eftalgezer/ANIAnimator/graphs/contributors/)
[![CodeFactor](https://www.codefactor.io/repository/github/eftalgezer/siestastepper/badge)](https://www.codefactor.io/repository/github/eftalgezer/siestastepper)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/4ff526bd45e642bb81b300f2243baef2)](https://www.codacy.com/gh/eftalgezer/ANIAnimator/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=eftalgezer/ANIAnimator&amp;utm_campaign=Badge_Grade)
[![PyPI license](https://img.shields.io/pypi/l/ANIAnimator.svg)](https://pypi.python.org/pypi/ANIAnimator/)
[![DOI](https://zenodo.org/badge/532944393.svg)](https://zenodo.org/badge/latestdoi/532944393)

ANIAnimator makes the GIF file from a given chemical ANI file.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ANIAnimator.

```bash
$ pip install ANIAnimator

# to make sure you have the latest version
$ pip install -U ANIAnimator

# latest available code base
$ pip install -U git+https://github.com/eftalgezer/ANIAnimator.git
```

## Tutorial

- [ANIAnimator v0.0.1 tutorial](https://beyondthearistotelian.blogspot.com/2022/09/anianimator-v001-tutorial.html)

## Usage

### In code

#### Simple usage

```python
ANIAnimator.animate(anifile="graphene.ANI")

```

#### Advance usage

```python
ANIAnimator.animate(anifile="graphene.ANI", width=1920, height=1080) # defaults are 1920 × 1080, respectively

ANIAnimator.animate(anifile="graphene.ANI", loop=1) # default is 0; 0 means loop, 1 means no loop

ANIAnimator.animate(bonds_param=1.3) # default is 1.3, sets the bonds between atoms

```



### In terminal

#### Simple usage

```sh
$ python -m ANIAnimator graphene.ANI
```

#### Advance usage

```sh
$ python -m ANIAnimator <ANI file> <width> <height> <loop> <bonds_param>

$ python -m ANIAnimator graphene.ANI 1920 1080 1 1.3

```

### About `bonds_param` parameter
ANIAnimator uses [mogli](https://github.com/sciapp/mogli) to create PNG images of the steps in ANI files. The default of mogli package is `1.0`. ANIAnimator default is `1.3` since the experience shows that `1.3` is better. For details, see the [README.md of mogli package](https://github.com/sciapp/mogli/blob/master/README.md).

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Citation
If you are using ANIAnimator, please citate relevant version. You can find the relevant citation [here]().

```bibtex

```

## License
[GNU General Public License v3.0](https://github.com/eftalgezer/ANIAnimator/blob/master/LICENSE) 
 
