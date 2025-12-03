import time
import datetime

def time_log(func):
    def wrapper(*args, **kwargs):
        print("Executing Function")
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        time_taken = end_time - start_time
        print(f"{time_taken.total_seconds()} Total time taken by function")
        return result
    return wrapper
        
@time_log        
def counter(x, sleep_time=1):
    for x in range(1,x):
        print(x)
        time.sleep(sleep_time)
        
counter(10, 1)


    
        

        
        
        