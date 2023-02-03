sentence = "This is a common interview question"

def number_of_occurrences(sentence):
    char_array = [*sentence]
    char = []
    count = []
    for item in char_array:
        if item not in char:
            char.append(item)
            count.append(char_array.count(item))
    occurrences = (list(zip(char, count)))
    return sorted(occurrences, key = lambda kv: kv[1], reverse=True)[0]


print(number_of_occurrences(sentence))