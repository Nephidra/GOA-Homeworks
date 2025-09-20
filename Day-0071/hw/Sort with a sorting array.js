function sort(initialArray, sortingArray) {
    const result = [];
    for (let i = 0; i < sortingArray.length; i++) {
        result[sortingArray[i]] = initialArray[i];
    }
    return result;
}