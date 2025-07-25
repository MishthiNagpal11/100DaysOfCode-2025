def count_vowels_and_consonants(s):
    
    vowels = set("aeiouAEIOU")
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    
    vowel_count = 0
    consonant_count = 0
    
    for char in s:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
            
    return vowel_count, consonant_count

user_input = input("Enter a string to count vowels and consonants: ")

vowels_count, consonants_count = count_vowels_and_consonants(user_input)

print("\nResults:")
print(f"Number of vowels: {vowels_count}")
print(f"Number of consonants: {consonants_count}")
