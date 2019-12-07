# bvr
BVR: Log like a Beaver

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI version](https://badge.fury.io/py/bvr.svg)](https://badge.fury.io/py/bvr)
![GitHub](https://img.shields.io/github/license/doedotdev/bvr)

## Install
```
pip install bvr
```

### bvr decorators
- [@bvr_start | log when a method starts](#bvr_start)
- [@bvr_end | log when a method ends](#go-to-bvr-end)
- [@bvr_start_end | log when a method starts and ends](#go-to-bvr-start-end)
- [@bvr_rest_before | log and sleep before a method starts](#go-to-bvr-rest-before)
- [@bvr_rest_after | log and sleep after a method ends](#go-to-bvr-rest-after)
- [@bvr_time | log the amount of time a method takes](#go-to-bvr-time)
- [@bvr_try | log and catch an exception](#go-to-bvr-try)
- [@bvr_repeat | log and repeat a method](#go-to-bvr-repeat)
- [@bvr_compose | compose multiple other bvr decorators on a single method](#go-to-bvr-compose)


### bvr_start 
| log when a method starts

Example:
```
from bvr import bvr_start

@bvr_start
def example_one():
    print("hello")
    return 3

example_one()
```

Output:
```
STARTED | FUNCTION: example_one | ARGS: () | KWARGS: {}

hello
```


### @bvr_end | log when a method ends (#go-to-bvr-end)

Example:
```
from bvr import bvr_end

@bvr_end
def example_one():
    print("hello")
    return 3

example_one()
```

Output:
```
hello

ENDED | FUNCTION: example_one | ARGS: () | KWARGS: {}
```

### @bvr_start_end | log when a method starts and ends (#go-to-bvr-start-end)

Example:
```
from bvr import bvr_start_end

@bvr_start_end
def example_one():
    print("hello")
    return 3

example_one()
```

Output:
```
STARTED | FUNCTION: example_one | ARGS: () | KWARGS: {}

hello

ENDED | FUNCTION: example_one | ARGS: () | KWARGS: {} 
```

### @bvr_rest_before | log and sleep before a method starts (#go-to-bvr-rest-before)
Coming Soon!

### @bvr_rest_after | log and sleep after a method ends (#go-to-bvr-rest-after)
Coming Soon!

### @bvr_time | log the amount of time a method takes (#go-to-bvr-time)
Coming Soon!

### @bvr_try | log and catch an exception (#go-to-bvr-try)
Coming Soon!

### @bvr_repeat | log and repeat a method n times (#go-to-bvr-repeat)
Coming Soon!

### @bvr_compose | compose multiple other bvr decorators on a single method (#go-to-bvr-compose)
Coming Soon!


# TODO:
- Docs Badge passing
- test passing
- build passing
- requirements up to date and passing
- package info pypi
- test pypi
- supported python versions
- cocverage info
- travis ci info
- pylint score 10/10
- apply to the class level
- Smoke test that pip installs the latest version
- smoke test then runs tests against that version to make sure no issues
- todo: emd of deploy script deletes dist and egg files to clean itself up
- todo: rem,ove initial arg which is not really needed
