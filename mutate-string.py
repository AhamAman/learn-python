def mutate_string(s, pos, ch):
    # changed_to_list  = list(string)
    # changed_to_list[position]= character
    # changed_string = ''.join(changed_to_list)
    # return changed_string
    # return s[:pos] + ch + s[pos+1:]
    return ''.join(ch if i == pos else s[i] for i in range(len(s)))

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
