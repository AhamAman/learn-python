# import string
# alpha = string.ascii_lowercase

# def print_rangoli(size):
#     lines = []
#     for row in range(size):
#         to_print = "-".join(alpha[row:size])
#         lines.append(to_print[::-1] + to_print[1:])
#     width = len(lines[0])
    
#     for row in range(size-1, 0, -1):
#         print(lines[row].center(width, '-'))
        
#     for row in range(size):
#         print(lines[row].center(width, '-'))
        
   
# import string

# def print_rangoli(n):
#     alpha = string.ascii_lowercase
#     width = 4*n - 3

#     for i in range(n-1, -1, -1):
#         left = [alpha[j] for j in range(n-1, i-1, -1)]
#         right = [alpha[j] for j in range(i+1, n)]
#         row = "-".join(left + right)
#         print(row.center(width, "-"))

#     for i in range(1, n):
#         left = [alpha[j] for j in range(n-1, i-1, -1)]
#         right = [alpha[j] for j in range(i+1, n)]
#         row = "-".join(left + right)
#         print(row.center(width, "-"))
  
# import string

# def print_rangoli(n):
#     alpha = string.ascii_lowercase
#     rows = []

#     for i in range(n):
#         letters = alpha[n-1:i:-1] + alpha[i:n]
#         rows.append("-".join(letters))

#     width = len(rows[0])
#     for row in rows[::-1] + rows[1:]:
#         print(row.center(width, '-'))
   
import string

def print_rangoli(n):
    alpha = string.ascii_lowercase
    L = []

    for i in range(n):
        s = "-".join(alpha[n-1:i:-1] + alpha[i:n])
        L.append(s)

    width = len(L[0])
    print('\n'.join([row.center(width,'-') for row in L[::-1] + L[1:]]))
   
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
