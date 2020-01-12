word = input("Words to count: ")
spaced_word = ""
for x in word:
    if x == " ":
        spaced_word = spaced_word + "."
    elif x == ".":
        spaced_word = spaced_word
    else:
        spaced_word = spaced_word + x

counted_words = ""
i = 0
for x in spaced_word:
    if x == ".":
        if i == 0:
            i += 2
        elif i >= 0:
            i += 1
        
print("There are " + str(i) + " words.")
input()
