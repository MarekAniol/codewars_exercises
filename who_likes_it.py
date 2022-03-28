def likes(names):
    if len(names) == 0:
        resp = "no one likes this"
    elif len(names) == 1:
        resp = f"{names[0]} likes this"
    elif len(names) == 2:
        resp = f"{names[0]} and {names[1]} likes this"
    elif len(names) == 3:
        resp = f"{names[0]}, {names[1]} and {names[2]} likes this"
    elif len(names) > 3:
        resp = f"{names[0]}, {names[1]} and {len(names)-2} others like this"
    return resp

print(likes([]))
print(likes(['Peter']))
print(likes(['Jacob', 'Alex']))
print(likes(['Max', 'John', 'Mark']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))