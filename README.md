# bvr
BVR: Log like a Beaver

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI version](https://badge.fury.io/py/bvr.svg)](https://badge.fury.io/py/bvr)
![GitHub](https://img.shields.io/github/license/doedotdev/bvr)




## Install
```
pip install bvr
```

### @bvr_start
- Logs when a method is starting

Example:
```
@bvr_start
def example_one():
    print("hello")
    return 3

example_one()

# STARTED | FUNCTION: example_one | ARGS: () | KWARGS: {} 
```

Example with ARGS:
```
@bvr_start
def example_two(msg, value):
    print(msg)
    return value

example_two("Hi", 4)

# STARTED | FUNCTION: example_two | ARGS: ('Hi', 4) | KWARGS: {}
```

Example with KWARGS
```
@bvr_start
def example_three(msg, value):
    print(msg)
    return value

example_two(msg="Hi", value=4)

# STARTED | FUNCTION: example_two | ARGS: () | KWARGS: {'msg': 'Hi', 'value': 4} 
```

### bvr_end
Logs after the function is called

### bvr_start_end
Utilizes 


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
