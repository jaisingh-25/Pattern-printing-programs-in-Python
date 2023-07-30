# l=[]
# for i in range(1,51):
#     l.append(i**2)
# t=tuple(l)
# print(t)

# print()
# print()

# l=[]
# for i in range(97,123):
#     l.append(chr(i)*(i-96))
# t=tuple(l)
# print(t)

# print()
# print()

# a=[]
# for i in range(0,50):
#     l=[i]
#     a=a+l
# print(a)

# print()

# a=[]
# for i in range(1,50):
#     b=i**2
#     l=[b]
#     a=a+l
# print(a)

# print()

# a=[]
# for i in range(65,91):
#     b=chr(i)
#     c=i-64
#     l=[b*c]
#     a=a+l
# print(a)

# print()
# print()

# n=int(input("Enter no. of rows - "))
# for i in range(65,65+n):
#     for j in range(65,i+1):
#         print(chr(j), end=" ")
#     print()

# print()
# print()

# n=int(input("Enter no. of rows - "))
# for i in range(65,65+n):
#     print("  "*(n+64-i),end="")
#     for j in range(65,i+1):
#         print(chr(j), end=" ")
#     for j in range(i,65,-1):
#         print(chr(j-1), end=" ")
#     print()

# print()
# print()

# n=int(input("Enter no. of rows - "))
# for i in range(n,0,-1):
#     for j in range(i+64,65+n):
#         print(chr(j), end="")
#     print()
