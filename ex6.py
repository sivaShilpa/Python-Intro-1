def slice_it(array):
    output = ''
    for word in array:
        output += word[slice(2)]
    return output