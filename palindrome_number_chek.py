# palindrome number

# n = int(input())
# temp = n
# i = 0

# while (n > 0):
#     dig = n % 10          # if we want to add another
#     i = i * 10 + dig
#     n = n // 10

# if temp == i:
#     print("True")
# else:
#     print("False")


n = int(input())
temp = n
i = 0
while(n > 0):
    dig = n % 10
    i = i * 10 + dig
    n = n//10

if temp == i:
    print("True")
else:
    print("False")


'''
class Solution:
def isPalindrome(self, x: int) -> bool:
x=str(x)
if(len(x)==0 ) :
return False
elif(len(x)==1):
return True
else :
for i in range(len(x)//2) :
if x[i::]==x[::-(i+1)]:
return True
else:
return False
'''
