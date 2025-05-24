words = input("Enter words: ").split()
acronym = ""
for word in words:
    if word: 
        acronym += word[0].upper()
print("Acronym:", acronym)