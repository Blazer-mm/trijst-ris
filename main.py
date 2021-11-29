def LenkaParbaude(len1,len2,len3):
  rezultats=False
  if len1+len2+len3==180:
    rezultats=True
  return rezultats
len1 = int(input("Ievadi 1. lenķi "))
len2 = int(input("Ievadi 2. lenķi "))
len3 = int(input("Ievadi 3. lenķi "))
rezultats = LenkaParbaude(len1,len2,len3)
if rezultats:
  print("Trijstūris eksistē!")
else:
  print("Trijstūris neeksistē!")