def diagonal_printer(sentence):
    words = sentence.split()
    i = 0
    for word in words:
        for letter in word:
            print(i * ' ' + letter)
            i += 1
        i = 0
