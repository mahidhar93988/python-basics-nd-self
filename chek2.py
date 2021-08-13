# prime number
# # n = int(input())  # 35
# # if n > 1:
# #     count = 0  # 1

# #     for i in range(2, n):
# #         if n % i == 0:   # 35%2=0
# #             count = count+1
# #     if (count == 0):
# #         print("yes Prime")
# #     else:
# #         print("Not prime")


# Armstrong number

# # 153 = 1 ^ 3+5 ^ 3+3 ^ 3 armstrong number
# armstrong number
# # num = int(input())  # 1535
# # sum = 0
# # power = len(str(num))
# # main_num = num
# # while(num > 0):
# #     digit = num % 10
# #     sum += digit**power
# #     num = num//10

# # if(sum == main_num):
# #     print("Yes Armstrong")
# # else:
# #     print("Not Armstrong")

# #1535 [1,5,3,5]
# # num = int(input())
# # outputlst = []
# # input_num = num
# # count = 0
# # while(num > 0):
# #     output = num % 10  # 1535=5 153%10=3
# #     # outputlst.insert(0, output)  # 5,3,5,1
# #     outputlst = [output]+outputlst
# #     num = num//10  # 1//10=0

# # count = 0
# # for i in (outputlst):
# #     count = count+i**len(outputlst)  # 1535 == i**4
# # # print(input_num, num)
# # if (count == input_num):
# #     print("armstrong")
# # else:
# #     print("not armstrong")


# # palindrome for strings

# # str1 = input()
# # s = 0
# # st = ""

# # for i in str1:
# #     s = s+1
# # for i in range(1, s+1):   # hello = "olleh"+ip[s-2]  hello
# #     st = st+str1[s-i]
# # if str1 == st:
# #     print("Yes palindrome")
# # else:
# #     print("Not Palindromem random import shuffle")

# # P = int(input())
# # T = int(input())
# # R = int(input())

# # simple_intrest = (P * T * R)/100

# # print(int(simple_intrest))


# add = 0
# while(n > 0):
#     add = add + n % 10
#     n = n//10


# # product of intigers

# prod = 1
# while(m > 0):
#     prod = prod * (m % 10)
#     m = m//10


# difference = prod - add

# print(difference)


# growth

# n = int(input())
# list = []
# for i in range(n):
#     element = int(input())
#     list.append(element)

# add = 0
# for i in range(0, len(list)):
#     add = add + list[i]

# ave = add / n

# if ave > 100:
#     print("Excellent!")
# else:
#     print("Not Excellent!")


# n = int(input())
# list1 = []
# for i in range(n):
#     element = int(input())
#     list1.append(element)

#     if max(list1) == element:
#         print(element)
#     elif max(list1) > element:
#         print(max(list1))
