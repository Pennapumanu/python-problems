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

---------------- factorial 
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
        