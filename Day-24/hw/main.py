def sorting_words() :
    l1 = ["Ae", "Bae", "Zeea", "Goa", "Amga"]
    for i in range(0, len(l1)):
        for l in range(i+1, len(l1)):
            if len(l1[i]) >= len(l1[l]):
                (l1[i]), (l1[l]) = (l1[l]), (l1[i])

    print(l1[0])
sorting_words()