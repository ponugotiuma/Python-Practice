#Count vowels and consonants.
name="UmaPonugoti"
vowels=0
consonants=0
for char in name:
    if char in "aeiouAEIOU":
        vowels=vowels+1
    elif char.isalpha():
        consonants=consonants+1
    else :
        print(name)
print("vowels:", vowels)
print("Consonants:",consonants)
