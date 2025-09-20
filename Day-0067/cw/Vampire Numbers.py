def vampire_test(fang1, fang2):
    final = fang1 * fang2
    fang_str = str(fang1) + str(fang2)
    final_str = str(final)
    
    return sorted(fang_str) == sorted(final_str)