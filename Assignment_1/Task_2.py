text=input("Enter a string:")
vowels_count=0
consonant_count=0
vowels="aeiouAEIOU"
for char in text:
    if char.isalpha():
        if char in vowels:
            vowels_count+=1
        else:
            consonant_count+=1
print("Vowels count:",vowels_count)
print("Consonants count:",consonant_count)
