# def minion_game(string):
#     # your code goes here
#     vowels = ['A', 'E', 'I', 'O', 'U']
#     score_kevin = 0
#     score_stuart = 0
    
#     for index in range(len(string)):
#         if string[index] in vowels:
#             score_kevin += len(string) - index
#         else:
#             score_stuart += len(string) - index

#     if score_kevin > score_stuart:
#         print("Kevin {}".format(score_kevin))
#     elif score_kevin < score_stuart:
#         print("Stuart {}".format(score_stuart))
#     else:
#         print("Draw")
    
# time limit issue
# def minion_game(string):
#     vowels = "AEIOU"
#     kevin = stuart = 0

#     for i in range(len(string)):
#         for j in range(i+1, len(string)+1):
#             if string[i] in vowels:
#                 kevin += 1
#             else:
#                 stuart += 1

#     if kevin > stuart:
#         print("Kevin", kevin)
#     elif stuart > kevin:
#         print("Stuart", stuart)
#     else:
#         print("Draw")

def minion_game(s):
    vowels = "AEIOU"
    kevin = stuart = 0
    n = len(s)

    for i, ch in enumerate(s):
        if ch in vowels:
            kevin += n - i
        else:
            stuart += n - i

    print("Kevin", kevin) if kevin > stuart else \
    print("Stuart", stuart) if stuart > kevin else \
    print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
