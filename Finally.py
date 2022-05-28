try:
    k = 5//0  # raises divide by zero exception.
    print(k)
 
except ZeroDivisionError:
    print("Can't divide by zero")
 
finally:
    print('This is always executed')
