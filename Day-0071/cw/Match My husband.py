def match(usefulness, months):
    total_usefulness = sum(usefulness)
    needs = 100 * (0.85 ** months)
    if total_usefulness >= needs :
        return "Match!"
    else :
        return "No match!"
