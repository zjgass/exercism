//
// This is only a SKELETON file for the 'Reverse String' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const reverseString = (wordToReverse) => {
  let charArray = wordToReverse.split("");
  let reversedString = [];
  for (var i = charArray.length; i > - 1; i--) {
    reversedString.push(charArray[i]);
  }

  return reversedString.join("");
};
