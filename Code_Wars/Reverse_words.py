def reverse_words(text):
    words = text.split(' ')
    for i in range(len(words)):
        words[i] = words[i][::-1]
            
    return ' '.join(words)


sentence = "Hello World"
print(reverse_words(sentence))