def translator(str):
    translation = ""
    for letter in str:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "M"
            else:
                translation = translation + "m"
        else:
            translation = translation + letter
    return translation


print(translator(input("enter root phrase: ")))
