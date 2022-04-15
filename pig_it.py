from re import sub


def pig_it(text):
    return " ".join(el[1:] + el[0] + "ay" if not set('?!').intersection(el) else el for el in text.split())


def pig_it_2(text):
    return sub(r'(\w)(\w+)( ?)', r'\2\1ay\3', text)
