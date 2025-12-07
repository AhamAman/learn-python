if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        students.append([name, score])
    
    # lowest = min([el[1] for el in students])
    # second_low = min(list(filter(lambda a: a > lowest, [el[1] for el in students])))
    
    # out = [el[0] for el in students if (el[1] == second_low)]
    # out.sort()
    
    # print("\n".join(out))

    #set comprehention is faster than list
    #filtering out list for lowest
    second_lowest = sorted({score for _, score in students})[1]
    
    names = [name for name, score in students if score == second_lowest]
    names.sort()
    
    for name in names:
        print(name)
