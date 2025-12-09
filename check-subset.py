# Enter your code here. Read input from STDIN. Print output to STDOUT

# for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted. 
#     a = int(input()); A = set(input().split()) 
#     b = int(input()); B = set(input().split())
#     print(len((A - B)) == 0)
    
# for _ in range(int(input())):
#     input(); A = set(input().split())
#     input(); B = set(input().split())
#     print(A.issubset(B))
    
# for _ in range(int(input())):
#     input(); A=set(input().split())
#     input(); B=set(input().split())
#     print(A <= B)
    
# for _ in range(int(input())):
#     input(); A=set(input().split())
#     input(); B=set(input().split())
#     print(not (A - B))
    
# for _ in range(int(input())):
#     input(); A=input().split()
#     input(); B=set(input().split())
#     print(all(x in B for x in A))

# for _ in range(int(input())):
#     input(); A=input().split()
#     input(); B=set(input().split())
#     print(False not in [x in B for x in A])
    
for _ in range(int(input())):
    input(); A=set(input().split())
    input(); B=set(input().split())
    print(A & B == A)
