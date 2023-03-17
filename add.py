"""
wrong code
----------
a,b=input().split()
c=a+b;
print(c)
correct code
---------------
a,b=map(int,input().split())
c=a+b;
print(c)
"""
a=int(input())
b=int(input())
c=a+b
print(c)
print("add=",c)
