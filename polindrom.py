def czyPalindrom(x):
    x = x.lower().replace(" ", "").replace("?", "").replace("!", "").replace("-", "").replace(",", "").replace(".", "")
    n = len(x)
    for i in range(n-1):
        if x[i] != x[n-1-i]:
            return False
        else:
            return True
print("Podaj słowo lub zdanie: ")
x = input()
if czyPalindrom(x) == True:
    polindrom = f" '{x}' jest polidromem"
else:
    polindrom = f" '{x}' nie jest polidromem"
print(polindrom)