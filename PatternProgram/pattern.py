h = int(input("Enter the number of lines for design:"))
l = ['F','O','R','M','U','L','A','Q','S','O','L','U','T','I','O','N','S']
for x in range(h // 2 + 1):
    print(" " * (h // 2 - x), end="")
    for y in range(x, 3 * x + 1):
        print(l[y % 17], end="")
    print()
if h % 2 == 0:
  for x in range(h // 2 + 1, h + 1):
    print(" " * (x - (h // 2)), end="")
    for y in range(x, (h * 2) - x + 1): 
        print(l[y % 17], end="")
    print()
else:
   for x in range(h // 2 + 1, h):
      print(" " * (x- (h // 2)), end="")
      for y in range(x, ( h * 2)- x - 1):
         print(l[y % 17], end="")
      print()