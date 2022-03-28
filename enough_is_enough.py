def delete_nth(order, max_e):  # first try...
    order_rev = order[::-1]
    for elem in order_rev:
        if order_rev.count(elem) > max_e:
            order_rev.pop(order_rev.index(elem))
    return order_rev[::-1]

def delete_nth_2(order, max_e):  # Goooddd!
    new = []
    for elem in order:
        if new.count(elem) < max_e:
            new.append(elem)
    return new

def delete_nth_3(order, max_e):  # Great!
    return [order[i] for i in range(len(order)) if order[0:i].count(order[i]) < max_e]

print(delete_nth_3([1,1,3,3,7,2,2,2,2], 3))