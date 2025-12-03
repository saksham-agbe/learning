from src.functions.decorator import my_function

# def my_decorator(func):
#     def wrapper():
#         print("Before function runs")
#         func()
#         print("After function runs")
#     return wrapper

# @my_decorator
# def greet():
#     print("Hello!")

# greet()

def my_function(func):
    def my_inner():
        return func().upper()
    return my_inner

@my_function
def my_function1():
    return





    