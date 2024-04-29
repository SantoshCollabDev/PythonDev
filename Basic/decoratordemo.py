# # ====================================

# # DECORATOR demostration # 2

from datetime import datetime

def trace_my(func):
    def wrapper():
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"function excution started at {current_time}.")
        func()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"Fcuntion executed completed at {current_time}.")
    return wrapper

@trace_my
def write_to_database():
    print("writing to database")

write_to_database()

# # ====================================

# # ====================================

# # DECORATOR demostration # 1

# def decorator(func):
#     def wrapper():
#         print("somthing is heppening before the function is called.")
#         func()
#         print("something is heppaning after the function is called. ")
#     return wrapper

# @decorator
# def say_test():
#     print("testing")

# say_test()

# # ====================================

# def shoot(name):
#   print(f"i will shoot you {name}")

# def greet(name):
#   print(f"Welcome {name}, How are you doing")

# shoot('xyz')
# greet('xyz')

# # ====================================

# # NESTED FUNCTION EXAMPLE
# def parent():
#     def child_1():
#       print("child 1")
#     def child_2():
#       print("child 2")
#     child_1()
#     child_2()

# parent()

# # ====================================

# # VARIABLE HOLDING & CALLING A FUNCTION

# def say_hello():
#     print("Hello")

# # assigning a finction to varialble
# x = say_hello
# # calling function
# x()
# # ====================================

