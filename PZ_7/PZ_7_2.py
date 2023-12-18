# Дана строка, состоящая из русских слов, разделённых пробелами (одним или несколькими). Найдите длинну самого
# длинного слова
def get_tell_word(args):
    tell_word = ''

    for i in args:
        if len(tell_word) > 0:
            word = i.strip()
            if len(word) > len(tell_word):
                tell_word = word
        else:
            tell_word = i.strip()
            continue

    return tell_word


while True:
    words = input('Input your words: ')

    if words == '/quit':
        break
    else:
        tell_word = get_tell_word(words.split())
        print(f'Length word {tell_word} is {len(tell_word)}')
