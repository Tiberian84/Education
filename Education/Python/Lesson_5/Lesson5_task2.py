#Ввод слова
word = input()

#определяем гласные
vowels = "aeiou"

#счетчик
vowels_count = 0
consonant_count = 0

#словарь для подсчёта каждой гласной буквы
vowels_counts = {vowel: 0 for vowel in vowels}


for l in word:
    if l in vowels:
        vowels_count += 1
        vowels_counts[l] +=1
    elif l.isalpha(): #Проверяем что это буква а не символ или цифра.
        consonant_count +=1
    
# Выводим результаты
print(f"Гласных букв: {vowels_count}")
print(f"Согласных букв: {consonant_count}")


# Выводим количество каждой гласной буквы
for vowel in vowels:
    if vowels_counts[vowel] > 0:
        print(f"{vowel}: {vowels_counts[vowel]}")
    else:
        print(f"{vowel}: False")