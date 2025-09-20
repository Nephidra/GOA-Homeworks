def create_identity_matrix(n):
    m = []
    ls = []
    for i in range(n) :
        for _ in range(n) :
            ls.append(0)
        m.append(ls)
        ls= []
        m[i][i] = 1
    return m