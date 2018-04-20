# betterspy

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/betterspy/master.svg)](https://circleci.com/gh/nschloe/betterspy)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/betterspy.svg)](https://codecov.io/gh/nschloe/betterspy)
[![Codacy grade](https://img.shields.io/codacy/grade/df2f2e53e5e3465f9475e6c79d7003f2.svg)](https://app.codacy.com/app/nschloe/betterspy/dashboard)
[![PyPi Version](https://img.shields.io/pypi/v/betterspy.svg)](https://pypi.org/project/betterspy)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/betterspy.svg?logo=github&label=Stars)](https://github.com/nschloe/betterspy)

Show sparsity patterns of sparse matrices or write them to image files.

Example:
```python
import betterspy

A = sparse.rand(20, 20, density=0.1)
betterspy.show(A)
betterspy.write_png('out1.png', A, border_width=2)
betterspy.write_png('out2.png', A, border_width=2, colormap='viridis')
```

<img src="https://nschloe.github.io/betterspy/plain.png"> |
<img src="https://nschloe.github.io/betterspy/viridis.png">
:-------------------:|:------------------:|
no colormap          |  viridis           |


### Installation

betterspy is [available from the Python Package
Index](https://pypi.org/project/betterspy/), so simply do
```
pip install -U betterspy
```
to install or upgrade. Use `sudo -H` to install as root or the `--user` option
of `pip` to install in `$HOME`.


### Testing

To run the betterspy unit tests, check out this repository and type
```
pytest
```

### Distribution
To create a new release

1. bump the `__version__` number,

2. publish to PyPi and tag on GitHub:
    ```
    $ make publish
    ```

### License

betterspy is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
