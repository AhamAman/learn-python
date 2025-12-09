if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))
    num_cmds = int(input())
    

    # n = int(input())
    # s = set(map(int, input().split())) 
    # num_cmds = int(input())
    
    # for _ in range(num_cmds):
    #     cmd = list(input().strip().split(' '))
    #     if cmd[0] == 'pop':
    #         s.pop()
    #     elif cmd[0] == 'remove':
    #         s.remove(int(cmd[1]))
    #     elif cmd[0] == 'discard':
    #         s.discard(int(cmd[1]))
    
    # print(sum(s))
    
    for _ in range(num_cmds):
        cmd = input().split()

        if cmd[0] == 'pop':
            if s:        # guard
                s.pop()

        elif cmd[0] == 'remove':
            x = int(cmd[1])
            if x in s:   # guard
                s.remove(x)

        elif cmd[0] == 'discard':
            x = int(cmd[1])
            s.discard(x)

    print(sum(s))
