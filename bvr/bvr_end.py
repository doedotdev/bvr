

def bvr_end(arg=None):
    def bvr_end_decorator(func):
        def bvr_end_wrapper(*args, **kwargs):
            msg = ("ENDED | "
                   "FUNCTION: {} | "
                   "ARGS: {} | "
                   "KWARGS: {} ").format(func.__name__,
                                         args,
                                         kwargs)

            print(msg)

            return_value = func(*args, **kwargs)
            return return_value
        return bvr_end_wrapper

    if callable(arg):
        return bvr_end_decorator(arg)
    else:
        return bvr_end_decorator
