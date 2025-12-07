# def count_substring(string, sub_string):
#     count = 0
#     len_sub_string = len(sub_string)
    
#     for ch in range(len(string)):
#         if string[ch: ch+len_sub_string] == sub_string:
#             count += 1
            
# #     return count

# def count_substring(s, sub):
#     L = len(sub)
#     return sum(1 for i in range(len(s)) if s[i:i+L] == sub)    
    
# import re

# def count_substring(s, sub):
#     return len(re.findall(f'(?={re.escape(sub)})', s))

def count_substring(s, sub):
    count = start = 0
    while True:
        start = s.find(sub, start)
        if start == -1:
            return count
        count += 1
        start += 1  # move forward by 1 to allow overlaps


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
