import functools
from bvr.bvr_start import bvr_start
from bvr.bvr_end import bvr_end

@bvr_start
@bvr_end
def bvr_start_end(arg=None):

    def bvr_start_end_decorator(func):
        @functools.wraps(func)  # Just Keeps Identity of Function that is Decorated
        def bvr_start_end_wrapper(*args, **kwargs):
            print(func.__name__)
            # msg = ("SEND | "
            #        "FUNCTION: {} | "
            #        "ARGS: {} | "
            #        "KWARGS: {} ").format(func.__name__,
            #                              args,
            #                              kwargs)
            #
            # print(msg)
            return_value = func(*args, **kwargs)
            return return_value
        return bvr_start_end_wrapper

    if callable(arg):
        return bvr_start_end_decorator(arg)
    else:
        return bvr_start_end_decorator

# @bvr_start_end
@bvr_start_end
# @bvr_end
# @bvr_start
def hi(msg):
    print("Inside the main function: " + msg)

hi("hello")
