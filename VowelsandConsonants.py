s = input("Enter a string: ")

vowels = "aeiouAEIOU"
v_count = 0
c_count = 0

for ch in s:
    if ch.isalpha():          # count only letters
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)
print("Total letters:", v_count + c_count)