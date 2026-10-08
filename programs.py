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


def automorphic(num):
  sqNum = num*num
  count = 0
  temp=num
  while temp>0:
    temp//=10
    count+=1

  lastDig = sqNum%(10**count)
  if num == lastDig:
    print(f'{num} is a automorphic')
  else:
    print(f'{num} is not a automorphic')

automorphic(5)


def spynum(num):
  temp = num
  sum = 0
  prod = 1
  while temp>0:
    digit = temp%10
    sum = sum + digit
    prod = prod*digit
    temp = temp//10

  if sum == prod:
    print(f'{num} is a spynumber')
  else:
    print(f'{num} is not a spynumber')

spynum(1124)

def logic(num):
  last = num%10
  first = 0
  while num > 10:
     num = num//10
     first = num
  print(f'the first and last digit is : {first},{last}')
logic(35458)
    

for num in range(45, 101):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)


n = 24

# Previous prime find cheyyadam
previous = n - 1

while True:
    is_prime = True

    for i in range(2, previous):
        if previous % i == 0:
            is_prime = False
            break

    if is_prime:
        break

    previous = previous - 1


# Next prime find cheyyadam
next_num = n + 1

while True:
    is_prime = True

    for i in range(2, next_num):
        if next_num % i == 0:
            is_prime = False
            break

    if is_prime:
        break

    next_num = next_num + 1


# Distances calculate cheyyadam
previous_distance = n - previous
next_distance = next_num - n


# Nearest prime find cheyyadam
if previous_distance <= next_distance:
    print("Nearest prime:", previous)
else:
    print("Nearest prime:", next_num)


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False


arr = [0, 1, 0, 3, 12]
non = []
zero = []
for i in arr:
  if i != 0 and i > 0:
    non+=[i]
  else:
    zero+=[i]
new = non + zero
print(new)

arr = [10, 20, 20, 8, 15, 15, 5]

lar = arr[0]
sec = arr[0]

for i in arr:
    if i > lar:
        sec = lar
        lar = i
    elif i > sec and i != lar:
        sec = i

print(lar)
print(sec)


arr = [10, 5, 8, 20, 15]

lar = arr[0]
sec = arr[0]

for i in arr:
    if i > lar:
        sec = lar
        lar = i
    elif i > sec:
        sec = i

print(sec)


arr = [1, 2, 3, 5, 6]
n = 6 
expected = n*(n+1)//2
actual = 0
for i in arr:
  actual = actual + i

missing = expected - actual 
print(missing)


s = "{[()]}"

stack = []

for ch in s:

    if ch == '(' or ch == '[' or ch == '{':
        stack.append(ch)

    else:
        if len(stack) == 0:
            print("Not Balanced")
            break

        top = stack[-1]

        if (ch == ')' and top == '(') or \
           (ch == ']' and top == '[') or \
           (ch == '}' and top == '{'):

            stack.pop()

        else:
            print("Not Balanced")
            break

else:
    if len(stack) == 0:
        print("Balanced")
    else:
        print("Not Balanced")


s = "tree"

# Step 1: Count frequency
freq = {}

for ch in s:
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] += 1

# Step 2: Find highest frequency repeatedly
result = ""

while freq:
    max_count = 0
    max_char = ""

    for ch in freq:
        if freq[ch] > max_count:
            max_count = freq[ch]
            max_char = ch

    # Character ni frequency times add cheyyi
    for i in range(max_count):
        result += max_char

    # Already processed character remove cheyyi
    del freq[max_char]

print(result)


arr = [1,8,9,6,7]
leaders = []

for i in range(len(arr)):
  is_leaders = True

  for j in range(i+1,len(arr)):
    if arr[i]<=arr[j]:
      is_leaders = False
      break

  if is_leaders:
    leaders.append(arr[i])

print(leaders)



arr = [4, 2, 2, 1, 4, 3]

dup = []

for ch in arr:
  if ch not in dup:
    dup+=[ch]
    
for i in range(len(dup)):
  for j in range(i+1,len(dup)):
    if dup[j]<dup[i]:
      dup[i],dup[j] = dup[j],dup[i]

print(dup)
      

arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]

i = 0
j = 0

platforms = 0
max_platforms = 0

while i < len(arrival) and j < len(departure):

    if arrival[i] <= departure[j]:
        platforms += 1
        i += 1

        if platforms > max_platforms:
            max_platforms = platforms

    else:
        platforms -= 1
        j += 1

print(max_platforms)
