#  Start of Exercise 4

def remove_chars(word, n):
    new_word = word [n:]
    if n >= len(word):
        return "Enter smalest 'n'"
    return new_word

print (remove_chars("Pynative", 4))
print (remove_chars("Pynative", 2))
print (remove_chars("Pynative", 8))

#  Start of Exercise 4