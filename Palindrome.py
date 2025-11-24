text = input("Enter a string or number: ")

# Reverse the string
rev = text[::-1]

if text == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")
