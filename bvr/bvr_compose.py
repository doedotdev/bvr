

def bvr_compose(decorators, arg=None):
    def bvr_compose_decorator(func):
        for decorator in decorators:
            print("IN  PROGRESS....")
            print(decorator.__name__)
            func = decorator(func)
        return func

    if callable(arg):
        return bvr_compose_decorator(arg)

    return bvr_compose_decorator
