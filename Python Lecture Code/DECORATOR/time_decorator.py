import functools
import time
def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args):
        #The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function
        #double star allows us to pass through keyword arguments; used to pass a keyworded, variable-length argument list
        start_time=time.perf_counter()
        value=func(*args)
        end_time=time.perf_counter()
        run_time=end_time-start_time
        print(f"Finished {func.__name__!r} in { run_time:.4f} secs")
        return value
    return wrapper_timer
