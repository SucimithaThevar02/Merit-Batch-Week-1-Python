text = input("Enter a word or number: ")
cleaned = text.lower().replace(" ", "")

if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
