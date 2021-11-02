x = input("Podaj słowo lub zdanie: ")
def czyPolindrom(x):
    for letters in x:
        letter = letters.isalpha()
        if letter == True:
            pass
        else:
            x = x.replace(letters, "").lower()
    n = len(x)
    for i in range(n-1):
        if x[i] != x[n-1-i]:
            return False
        else:
            return True
if czyPolindrom(x) == True:
    polindrom = f" '{x}' jest polidromem"
else:
    polindrom = f" '{x}' nie jest polidromem"
print(polindrom)