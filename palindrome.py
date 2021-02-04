def palindrome():
    l = input("Enter a word: ")

    if l[::-1] == l:
        print("It is a palindrome")

    else:
        print("It's not a palindrome")

palindrome()

