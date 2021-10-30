def czyPalindrom(x):
    x = x.lower().replace(" ", "")
    n = len(x)
    for i in range(n-1):
        if x[i] != x[n-1-i]:
            return False
        else:
            return True