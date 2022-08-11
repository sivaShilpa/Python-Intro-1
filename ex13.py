def frame_it(wordlist):
    longest = max(wordlist, key=len)
    llength = len(longest)
    print((llength+4)* '*')

    for word in wordlist:
        if len(word) < llength:
            print('* ' + word + (llength - len(word)) * ' '+' *')
        else:
            print('* ' + word + ' *')

    print((len(longest) + 4) * '*')