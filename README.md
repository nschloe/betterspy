# betterspy

[![PyPi Version](https://img.shields.io/pypi/v/betterspy.svg?style=flat-square)](https://pypi.org/project/betterspy)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/betterspy.svg?style=flat-square)](https://pypi.org/pypi/betterspy/)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/betterspy.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/betterspy)
[![PyPi downloads](https://img.shields.io/pypi/dm/betterspy.svg?style=flat-square)](https://pypistats.org/packages/betterspy)

[![Discord](https://img.shields.io/static/v1?logo=discord&label=chat&message=on%20discord&color=7289da&style=flat-square)](https://discord.com/channels/818781969562599434/818781969562599438)

[![gh-actions](https://img.shields.io/github/workflow/status/nschloe/betterspy/ci?style=flat-square)](https://github.com/nschloe/betterspy/actions?query=workflow%3Aci)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/betterspy.svg?style=flat-square)](https://codecov.io/gh/nschloe/betterspy)
[![LGTM](https://img.shields.io/lgtm/grade/python/github/nschloe/betterspy.svg?style=flat-square)](https://lgtm.com/projects/g/nschloe/betterspy)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

Show sparsity patterns of sparse matrices or write them to image files.

Example:
```python
import betterspy
from scipy import sparse

A = sparse.rand(20, 20, density=0.1)

# betterspy.plot()
# set attributes on gca()
# plt.show()
# or directly

betterspy.show(A)

betterspy.write_png(
    "out.png",
    A,
    # border_width=2,
    # border_color="red",
    # colormap="viridis"
)
```

<img src="https://nschloe.github.io/betterspy/plain.png"> | <img src="https://nschloe.github.io/betterspy/viridis.png">
:-------------------:|:------------------:|
no colormap          |  viridis           |

There is a command-line tool that can be used to show [matrix-market
files](https://math.nist.gov/MatrixMarket/):
```
betterspy msc00726.mtx [out.png]
```
See `betterspy -h` for all options.


### Installation

betterspy is [available from the Python Package
Index](https://pypi.org/project/betterspy/), so simply do
```
pip install betterspy
```
to install.


### License
This software is published under the [GPLv3 license](https://www.gnu.org/licenses/gpl-3.0.en.html).
