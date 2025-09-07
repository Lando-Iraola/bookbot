def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_num_chars(book_text):
    chars_dic = {}

    for c in book_text:
        if c.lower() not in chars_dic:
            chars_dic[c.lower()] = 1
            continue
        chars_dic[c.lower()] += 1

    return chars_dic

def sort_on(items):
    return items["num"]

def sort_dictionary(dic):
    prep_dic = []
    for key, value in dic.items():
        prep_dic.append({"char": key,"num": value})

    prep_dic.sort(reverse=True,key=sort_on)
    return prep_dic

    

