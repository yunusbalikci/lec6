universal = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
p = set([1, 2, 5])
q = set([2, 4, 8])


def complement(element):
    return universal - element


unionpq = (p | q)

com_p = complement(p)
com_q = complement(q)
intersect_pq = com_p & com_q

print(intersect_pq)
print(complement(p | q))

if complement(p | q) == intersect_pq:
    print("These sets are equal")
else:
    print("These sets are not equal ")