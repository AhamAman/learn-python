if __name__ == '__main__':
    s = input()
     
    # checks = [
    #     str.isalnum,
    #     str.isalpha,
    #     str.isdigit,
    #     str.islower,
    #     str.isupper
    # ]
    # for f in checks:
    #     print(any(f(ch) for ch in s))
    
     #using generator and  lazy evaluation
    print (any(ch.isalnum() for ch in s))
    print (any(ch.isalpha() for ch in s))
    print (any(ch.isdigit() for ch in s))
    print (any(ch.islower() for ch in s))
    print (any(ch.isupper() for ch in s))
   
