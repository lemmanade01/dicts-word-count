def counting_words(file):
    """Count words in file."""

    opened_file = open(file)
    
    word_count = {}

    for line in opened_file:
        list_of_words = line.split(" ")
        for word in list_of_words:
            word_count[word] = word_count.get(word, 0) + 1

        
    # for each_word in opened_file:
    #     word_count[each_word] = word_count.get(each_word, 0) + 1

    return word_count

print(counting_words("test.txt"))
