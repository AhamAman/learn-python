if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # first = max(arr)
    
    # print(max(list(filter(lambda element: element!=first, arr))))
    
    #another way
    second = sorted(set(arr))[-2]
    print(second)

    # first = max(arr)
    
    # arr2 = [x for x in arr if x != first]
    # second = max(arr2)
    
    # print(second)


#     first = second = float('-inf')
#     for num in arr:
#         if num > first:
#             second = first
#             first = num
#         elif first > num > second:
#             second = num

# print(second)
