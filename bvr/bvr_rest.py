

def bvr_rest():
    pass


# import functools

def repeat(_func=None, *, num_times=2):

    def decorator_repeat(func):
        print(func.__name__)

        # @functools.wraps(func) # Just Keeps Identity of Function that is Decorated
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)


@repeat
def say_hi():
    print('Hi')

say_hi()

print(say_hi.__name__)
