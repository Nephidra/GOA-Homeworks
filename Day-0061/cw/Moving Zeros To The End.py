def move_zeros(lst):
    lst_2 = []
    total = lst.count(0)
    for i in range(len(lst)) :
        if lst[i] != 0 :
            lst_2.append(lst[i])
            
    for j in range(total) :
        lst_2.append(0)
    return lst_2