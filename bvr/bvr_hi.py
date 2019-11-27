

def bvr_hi(arg=None):
    def bvr_hi_decorator(func):
        def bvr_hi_wrapper(*args, **kwargs):
            print("Hi")
            return_value = func(*args, **kwargs)
            print("Hi")
            return return_value
        return bvr_hi_wrapper

    if callable(arg):
        return bvr_hi_decorator(arg)
    else:
        return bvr_hi_decorator
