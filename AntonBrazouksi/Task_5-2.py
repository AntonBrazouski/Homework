def most_common_words(filepath, number_of_words=3):
    lorem = []
    words = []
    common = {}
    bad_chars = ['.', ',', '!', '*', '?']

    with open(filepath, 'r') as f:
        lorem = f.readlines()

    for line in lorem:
        words = line.split()
        for word in words:
            for ch in word:
                clean_word = ''
                if ch in bad_chars:
                    clean_word = word.replace(ch, '')
                else:
                    clean_word = word
            common[clean_word] = common.get(clean_word, 0) + 1   

    result = list({key: val for key, val in sorted(
        common.items(), key = lambda ele: ele[1], reverse=True 
    )})
    
    return result[:number_of_words]

      

print(most_common_words('../data/lorem_ipsum.txt'))