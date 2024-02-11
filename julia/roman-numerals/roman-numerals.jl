function to_roman(number)
  if number <= 0 || number > 3999
    throw(ErrorException("Must be between 1 and 3999"))
  end

  thousands = ["", "M", "MM", "MMM"]
  hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
  tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
  ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX",]
  result = ""
  
  result = result * thousands[div(number, 1000) + 1]
  number = number % 1000
  result = result * hundreds[div(number, 100) + 1]
  number = number % 100
  result = result * tens[div(number, 10) + 1]
  number = number % 10
  result = result * ones[number + 1]
end
