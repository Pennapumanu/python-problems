------------prime number 
n = 7 
count = 0

for i in range(1,n+1):
    if n%i==0:
        count+=1
        
if count == 2:
    print("prime ")
else:
    print("not a prime")

5! = 5 * 4* 3* 2* 1 = 120

# ---------------- factorial 
n = 5
factorial = 1

for i in range (1,n+1):
    factorial = factorial*i
    
print(factorial)




#---------- palindrone 

name = "madam"
count = 0
for i in range(len(name)):
    if name[i]==name[-i-1]:
        count+=1
if count == len(name):
    print("palindrone")
else:
    print("not a palindrone")



#  -----Factorial using Recursion



def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n-1)

# Fibonacci using Recursion

# Program:

def fib(num):
    if num == 1 or num == 2:
        return 1

    return fib(num-1) + fib(num-2)


# Sum of N Numbers using Recursion

# Program:

def total(n):
    if n == 1:
        return 1

    return n + total(n-1)

# except and try



try:
    print(10/0)
except:
    print("Cannot divide by zero")

# selection sort

n = [29, 10, 14, 37, 13]

for i in range(len(n)):
  smallest = n[i]
  min_index = 0
  for j in range(i+1,len(n)):
    if n[j]<smallest:
      smallest = n[j]
      min_index = j
      n[i],n[min_index] = n[min_index],n[i]
print(n)
        
