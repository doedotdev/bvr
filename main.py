from bvr.bvr_hi import bvr_hi
from bvr.bvr_try import bvr_try
from bvr.logger import Logger


@bvr_hi
def say_something():
    print("something")

logger = Logger()


@bvr_try(logger_class=logger, exception_type=Exception, should_raise=False)
def divide_zero():
    x = 1
    y = 0
    return x/y

x = divide_zero()
print(x)
