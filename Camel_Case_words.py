def count_camel_case_words(string):
    word_count = 1  
    for i in range(1, len(string)):
        if string[i].isupper():
            word_count += 1
    return word_count
input_sequence = input()
word_count = count_camel_case_words(input_sequence)
print(word_count)
