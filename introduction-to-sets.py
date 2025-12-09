def average(array):
    # your code goes here
    uniq = set(array)
    
    return sum(uniq)/len(uniq)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
