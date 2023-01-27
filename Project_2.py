x = int(input('Insert your Solar year or Gregorian year:'))
if x < 1500:
 y = x + 621
 print(f"This Is Your Gregorian Year:{y}")
else:
 y= x - 621
 print(f"This Is Your Solar Year:{y}")