def filter_numbers(string):
    return "".join(x for x in string if not x.isdigit())


def duplicate_count(text):
    text = text.lower()
    return sum(1 for c in set(text) if text.count(c) > 1)


function uniquePush(arr, obj) {
  if (!obj || !obj.phoneNumber) return false;
  const exists = arr.some(p => p.phoneNumber === obj.phoneNumber);
  if (exists) return false;
  arr.push(obj);
  return true;
}


