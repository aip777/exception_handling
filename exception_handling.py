import sys

def divide(a:int, b:int)->float:
    try:
        return a / b
    except ZeroDivisionError as exp:
        print(exp)

def cls_name_exception(a:int, b:int)->float:
    try:
        return a / b
    except:
        exp = [sys.exc_info()[0], sys.exc_info()[1]]
        print(exp)

# obj = divide(10,2)
# print(obj)

obj = cls_name_exception(10,0)
print(obj)
