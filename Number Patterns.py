# i=int(input("Enter no. of rows - "))
# for i in range(0,i+1):
#     for j in range(1,i+1):
#         print(i, end=' ')
#     print(" ")

# print()
# print()

# i=int(input("Enter no. of rows - "))
# for i in range(0,i+1):
#     for j in range(1,i+1):
#         print(j, end=' ')
#     print(" ")

# print()
# print()

# n=int(input("Enter no. of rows - "))
# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         print(i, end=" ")
#     print(" ")

# print()
# print()


# n=int(input("Enter no. of rows - "))
# for i in range(0,n+1):
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print(" ")

# print()
# print()

# n=int(input("Enter no. of rows - "))
# for i in range(1,n+1):
#     for j in range((i-1)**2 +1,i**2 +1):
#         print(j, end=" ")
#     print(" ")

# print()
# print()

# import math as m
# a=int(input('Enter no. of rows - '))
# for b in range(0,a):
#     print(((' ')*(a-(a//4)))*(a-b-1), end='')
#     for c in range(0,b+1):
#         print(int((m.factorial(b))/((m.factorial(c)*(m.factorial(b-c))))), end=(' ')*(a+(a//2)))
#     print()

# print()
# print()

# x=input("Enter - a - for nth term of Fibonacci series \nEnter - b - for terms till nth term of Fibonacci series -\n")
# n=int(input("Enter n - "))
# a1,a2,a3=0,1,0
# if n>2:
#     for i in range(0,n):
#         if x=="b":
#             print(a3, end=" ")
#         elif i==n-1:
#             print(a3)
#         a1=a2
#         a2=a3
#         a3=a1+a2        
# elif n==2:
#     if x=="b":
#         print(a1, a2)
#     else:
#         print(a2)
# else:
#     print(a1)

# print()
# print()

# n=int(input("Enter no. of terms - "))
# n+=1
# fib=(0,1,1)
# for i in range(n-3):
#     fib=fib+(fib[i+1]+fib[i+2],)
# print(fib)
