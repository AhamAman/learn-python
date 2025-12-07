if __name__ == '__main__':
    N = int(input())
    
    final_list = []
    for _ in range(N):
        args = input().strip().split()
        cmd = args[0]
        if cmd == 'insert':
            final_list.insert(int(args[1]), int(args[2]))
        elif cmd == 'remove':
            final_list.remove(int(args[1]))
        elif cmd == 'append':
            final_list.append(int(args[1]))
        elif cmd == 'print':
            print(final_list)
        elif cmd == 'sort':
            final_list.sort()
        elif cmd == 'pop':
            final_list.pop()
        elif cmd == 'reverse':
            final_list.reverse()
    
