def add(x,y):
    return x+y

def divide(x,y):
    if y == 0:
        raise ZeroDivisionError("Divide by zero")
    else:
        return x/y