import sys
try:
 x= int(input("x: "))
 y= int(input("y: "))
except ValueError:
    print("Error:Invalide Value //Try to give numeric values only")
    sys.exit(1)
try:
 result= x/y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)
print(f"{x}/{y}={result}")# exception will be raised when divided by "0"
#if "try" and "except"block is not added as like above
