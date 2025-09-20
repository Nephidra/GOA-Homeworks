def manual(lst, x) :
    lst_2 = []
    for i in range(len(lst)) :
        if lst[i] != x :
            lst_2.append(lst[i])
    return lst_2
print(manual([64, 34, 25, 11, 22, 11, 90], 11))