import time

def decorator(fn):
    def execute(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        total_time = time.time() - start
        print(f"Time execution: {total_time}")
        return result
    return execute

@decorator
def gen_list(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i)
    return result

gen_list(500000)