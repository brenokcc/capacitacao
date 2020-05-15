
def intersect(d1, d2):
    d1_keys = d1.keys()
    d2_keys = d2.keys()
    keys = d1_keys & d2_keys
    d = {k: (d1[k], d2[k]) for k in keys}
    return d