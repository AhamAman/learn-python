def print_formatted(number):
    # # your code goes here
    # align = len(bin(number)[2:])
    
    # for num in range(1, number+1):
    #     num_dec = str(num)
    #     num_oct = oct(num)[2:]
    #     num_hex = hex(num)[2:].upper()
    #     num_bin = bin(num)[2:]
        
    #     print(num_dec.rjust(align), num_oct.rjust(align), num_hex.rjust(align), num_bin.rjust(align))
    
    # width = len(format(number, 'b'))

    # for i in range(1, number + 1):
    #     print(
    #         str(i).rjust(width),
    #         format(i, 'o').rjust(width),
    #         format(i, 'X').rjust(width),
    #         format(i, 'b').rjust(width)
    #     )
        w = len(f"{number:b}")
        for i in range(1, number+1):
            print(f"{i:>{w}} {i:>{w}o} {i:>{w}X} {i:>{w}b}")        
            

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
