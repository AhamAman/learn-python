def swap_case(s):
    # message = ''
    
    # for ch in s:
    #     if ch.isalpha():
    #         if ch.islower():
    #             message += ch.capitalize()
    #         else:
    #             message += ch.lower()
    #     else:
    #         message += ch
    
    # return message
    
    
    ## more pythoic way
    # result = ""
    # for ch in s:
    #     result += ch.upper() if ch.islower() else ch.lower()
    # return result
    
    
    # return ''.join(ch.upper() if ch.islower() else ch.lower() for ch in s)
    
    
    return s.swapcase()
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
