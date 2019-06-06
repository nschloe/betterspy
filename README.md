# betterspy

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/betterspy/master.svg)](https://circleci.com/gh/nschloe/betterspy)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/betterspy.svg)](https://codecov.io/gh/nschloe/betterspy)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![PyPi Version](https://img.shields.io/pypi/v/betterspy.svg)](https://pypi.org/project/betterspy)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/betterspy.svg?logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/betterspy)

Show sparsity patterns of sparse matrices or write them to image files.

Example:
```python
import betterspy

A = sparse.rand(20, 20, density=0.1)
betterspy.show(A)
betterspy.write_png(
    "out.png", A,
    # border_width=2,
    # border_color="red",
    # colormap="viridis"
    )
```

<img src="https://nschloe.github.io/betterspy/plain.png"> |
<img src="https://nschloe.github.io/betterspy/viridis.png">
:-------------------:|:------------------:|
no colormap          |  viridis           |

There is a command-line tool that can be used to show matrix-market files:
```
betterspy msc00726.mtx [out.png]
```
See `betterspy -h` for all options.


### Installation

betterspy is [available from the Python Package
Index](https://pypi.org/project/betterspy/), so simply do
```
pip3 install betterspy --user
```
to install.


### Testing

To run the betterspy unit tests, check out this repository and type
```
pytest
```

### License

betterspy is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
