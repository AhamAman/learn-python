# 
# from collections import Counter

# k = int(input().strip())
# nums = list(map(int, input().split()))

# count = Counter(nums)

# for num, freq in count.items():
#     if freq == 1:
#         print(num)
#         break


# k = int(input())
# arr = list(map(int, input().split()))

# print( (sum(set(arr))*k - sum(arr)) // (k-1) )

k = int(input())
numbers = list(map(int, input().split()))

freq = {}

for num in numbers:
    freq[num] = freq.get(num, 0) + 1

for num in freq:
    if freq[num] == 1:
        print(num)
        break
