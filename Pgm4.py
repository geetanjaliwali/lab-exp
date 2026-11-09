def word_count(file_name):
    #with open(file_name, 'r') as f:
    f=open(file_name,'r')
    text = f.read()

    words = text.split()

    word_frequency = {}

    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    sorted_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

    return sorted_words[:]


file_name = 'example.txt'
print(word_count(file_name))
