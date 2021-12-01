def czy_palindrom(text):
    check = ""
    for letter in text.lower():
        if letter.isalnum():
            check += letter
    return check == check[::-1]

if __name__ == "__main__":
    x = input("Podaj tekst: ")
    if czy_palindrom(x):
        print("palindrom")
    if not czy_palindrom(x):
        print("nie palindrom")