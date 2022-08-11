def vowel_counter(sentence):
    counter = 0
    for i in sentence:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            counter += 1

    return f"Number of vowels: {counter}"