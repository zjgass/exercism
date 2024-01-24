proc reverse*(s: string): string =
  var len = s.len - 1
  for i in countdown(len, 0):
    result.add(s[i])
  return
  
