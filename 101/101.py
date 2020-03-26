# Modify the program so that it also prints the count of the Pythagorean triples at the end.

countlist = []
for c in range(1, 48):
    for b in range(1, c):
        for a in range(1, b):
            if a * a + b * b == c * c:
                countlist.append(a)
                # Now let's print it
                print('{:3d}, {:3d}, {:3d}'.format(a, b, c))
print('Total triples:', len(countlist))