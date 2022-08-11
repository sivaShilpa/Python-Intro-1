def word_histogram(words):
    dictionary = {}
    for word in words.split():
        if word in dictionary.keys():
            dictionary[word] = dictionary[word] + 1
        else:
            dictionary[word] = 1

    print(dictionary)
