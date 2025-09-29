import time
from functools import wraps

def timeit_deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(f"[timeit] {func.__name__}: {time.time() - start:.6f} сек")
        return res
    return wrapper

def trace_deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[trace] {func.__name__} args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

def rescue_nan(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[rescue_nan] {func.__name__}: {e}")
            return float("nan")
    return wrapper

