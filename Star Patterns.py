# n=int(input("Enter no. of rows - odd no. - "))
# a=int((n+1)/2)
# b=int((n-1)/2)

# for i in range(1,a+1):
#       print((" * ")*i)

# for i in range(1,b+1):
#     print((" * ")*(a-i))

# print()
# print()

# n=int(input("Enter no. of rows - "))

# for i in range (0,n):
#     j=int(2*i+1)
#     s=int((((n*2)-1)-j)/2)
#     print("   "*s, " * "*j, "   "*s)

# print()
# print()

# rows=int(input("Enter no. of rows - "))
# rows+=1
# for i in range(0,rows):
#     for j in range(0,i-1):
#         print("*", end=' ')
#     print(" ")

# print()
# print()    

# rows=int(input("Enter no. of rows - "))
# rows+=1
# for i in range(rows,0, -1):
#     for j in range(0,i-1):
#         print("*", end=' ')
#     print(" ")

# print()
# print()

# n=int(input("Enter no. of rows - greater than 1 - "))
# print("", " * "*((n*2)-1))
# for i in range(1,n-1):
#     j=(n-i-2)*2
#     print("   "*i, " * ", "", "   "*j, " * ", "   "*i)
# print("   "*(n-1), " * ", "   "*(n-1))

# print()
# print()

# rows=int(input("Enter no. of rows (even) - "))
# n=int(rows/2)
# for i in range(0,n):
#     print("*"*(n-i), "  "*i, "*"*(n-i), sep="")
# for j in range(n-1,-1,-1):
#     print("*"*(n-j), "  "*j, "*"*(n-j), sep="")
