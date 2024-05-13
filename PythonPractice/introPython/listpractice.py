party_attendees = ['Adela', 'Fleda', 
                   'Owen', 'May', 'Mona', 
                   'Gilbert', 'Ford']

def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1


print(fashionably_late(party_attendees, "May"))


squares = []
for i in range(10):
    squares.append(i**2)
print(squares)