def vokon_zahlen(x):
    vowel=0
    consonant=0
    x=x.lower()
    for buchstabe in x:
        if buchstabe.isalpha():
            if buchstabe in "aeiou":
                vowel=vowel+1
            else:
                consonant=consonant+1
    return vowel, consonant

print("Es gibt", vowel, "Vokale und" , consonant , "Konsonanten")
            
