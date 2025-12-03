# try:
#   print(x)
# except:
#   print("An exception occurred")

# try:
#   x = 10
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")
  

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Program ended.")
    

    
  
