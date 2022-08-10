from ex1 import hello_world
from ex10 import calculator
from ex2 import array_to_string

# ex1
# hello_world("3")

# ex2
# array = [1, 2, 3]
# result = array_to_string(array)
# print(result)

# ex3
from ex3 import add_numbers

# array = [1.0, 1.1, "1"]
# result = add_numbers(array)
# print(result)

# ex4
from ex4 import count_words

# sentence = input("Enter sentence: ")
# num_words = count_words(sentence)
# print(num_words)

# ex5
from ex5 import replace_period

# sentence = "Test.  This is a test.  Testing."
# sentence2 = replace_period(sentence, "!")
# print(sentence2)

# ex6
from ex6 import slice_it

# array = ["this", "is", "another", "test"]
# r = slice_it(array)
# print(r)

# ex7
from ex7 import calc_total

# array = [2.00, 4.00, 4.00]
# tax = "10%"
# result = calc_total(array, tax)
# print(result)

# ex8
from ex8 import f_to_c, c_to_f

# print(f_to_c(22))
# print(c_to_f(-6))

# ex9
from ex9 import vowel_counter

# sentence = "This is a test"
# num_vowels = vowel_counter(sentence)
# print(num_vowels)

# ex10
while True:
    result = calculator()
    print(result)