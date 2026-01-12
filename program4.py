def factorial(n):
 if n==0 or 1:
  return 1\
  #recursive case:n!=n*(n-1)!
 else:
  return n*(n-1)
number=int(input("enter a number:"))
if number<0:
 
    print("/nError:factorial is not defined for negative numbers")
else:
        result=factorial(number)
        print(f"\nThe factorial of{number} is {result}")






