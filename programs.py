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
        

# program to print middle character(s) in the given string or number.

s = "Manohar"

if len(s)%2==0:
  middle = len(s)//2
  print(s[middle-1],[middle])
else:
  middle = len(s)//2
  print(s[middle])


n = 58361

# Last digit
last = n % 10

# First digit
temp = n
while temp >= 10:
    temp = temp // 10

first = temp

# Middle digits check
temp = n // 10
is_valid = True

while temp >= 10:
    digit = temp % 10

    if digit >= first or digit >= last:
        is_valid = False
        break

    temp = temp // 10


n = 75547
last = n % 10
temp = n // 10
middle_sum = 0

while temp >= 10:
    digit = temp % 10
    middle_sum = digit + middle_sum
    temp = temp // 10

outer = last + temp

if middle_sum == outer:
    print('both are equal')
else:
    print('not equal')
if is_valid:
    print("true")
else:
    print("false")




Middle Character(s)
s = "Wonder"

if len(s) % 2 == 0:
    middle = len(s) // 2
    print(s[middle - 1] + s[middle])
else:
    middle = len(s) // 2
    print(s[middle])
    
# 2. First + Last Digit vs Middle Digits

n = 75547

last = n % 10
temp = n // 10

middle_sum = 0

while temp >= 10:
    digit = temp % 10
    middle_sum = middle_sum + digit
    temp = temp // 10

outer = last + temp

if middle_sum == outer:
    print("both are equal")
else:
    print("not equal")


# 3. Check Middle Digits
n = 58361

last = n % 10

temp = n
while temp >= 10:
    temp = temp // 10

first = temp

temp = n // 10
is_valid = True

while temp >= 10:
    digit = temp % 10

    if digit >= first or digit >= last:
        is_valid = False
        break

    temp = temp // 10

if is_valid:
    print("true")
else:
    print("false")


# 4. Reverse Vowels
s = "Helloworld"
rev = ""

for i in s:
    if i in "aeiou":
        rev = i + rev

print(rev)
