def pig_it(text):
    return " ".join(el[1:] + el[0] + "ay" if not set('?!').intersection(el) else el for el in text.split())
