const romanNumerals = {
  M: 1000,
  D: 500,
  C: 100,
  L: 50,
  X: 10,
  V: 5,
  I: 1,
};

function toRomanLazy(num) {
  let answer = "";
  // iterate through values in obj and compare to num
  for (rKey of Object.keys(romanNumerals)) {
    const rValue = romanNumerals[rKey];
    // if value is greater than or equal
    if (num >= rValue) {
      // 's' * 3 = 'sss' DIDN'T WORK (PY)
      answer += rKey.repeat(Math.floor(num / rValue));
      num = num % rValue;
    }
  }
  return answer;
}

function toRoman(num) {
  return "";
}

const result = toRomanLazy(6);
// console.log(result)

module.exports = { toRoman, toRomanLazy };
