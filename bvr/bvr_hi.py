import functools
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def bvr_hi(arg=None):
    def bvr_hi_decorator(func):
        @functools.wraps(func)
        def bvr_hi_wrapper(*args, **kwargs):
            logger.info("Hi")
            return_value = func(*args, **kwargs)
            logger.info("Hi")
            return return_value
        return bvr_hi_wrapper

    if callable(arg):
        return bvr_hi_decorator(arg)

    return bvr_hi_decorator
