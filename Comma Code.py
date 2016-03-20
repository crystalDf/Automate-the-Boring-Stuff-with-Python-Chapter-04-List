def comma(spam_list):
    comma_string = ''
    for i in range(len(spam_list)):
        if i < len(spam_list) - 1:
            comma_string += spam_list[i] + ', '
        else:
            comma_string += 'and ' + spam_list[i]

    return comma_string

spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma(spam))
