function topScorers(users, minScore) {
  return users
    .filter(u => u.score >= minScore)
    .sort((a, b) => b.score - a.score)
    .map(u => u.name);
}

function flattenArray(arr) {
  return arr.reduce((acc, val) => 
    Array.isArray(val) ? acc.concat(flattenArray(val)) : acc.concat(val)
  , []);
}

function removeFalsy(obj) {
  const result = {};
  for (let key in obj) {
    if (obj[key]) result[key] = obj[key];
  }
  return result;
}

function filterEvenNumbers(arr) {
  return arr.filter(n => n % 2 === 0);
}

function reverseWords(str) {
  const words = str.trim().split(" ");
  if (words.length <= 1) return str;
  return words.pop() + " " + reverseWords(words.join(" "));
}