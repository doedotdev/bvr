from bvr import bvr_start, bvr_start_end, bvr_end


@bvr_start
def example_start():
    print("hello")
    return 3


@bvr_end
def example_end():
    print("hello")
    return 3


@bvr_start_end
def example_start_end():
    print("hello")
    return 3


example_end()
example_start()
example_start_end()