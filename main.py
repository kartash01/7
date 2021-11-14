def merge(*gta):
    gta_s = []
    for i in gta:
        gta_s += i
    
    if len(gta_s) < 2:
        return gta_s
    else:
        a = gta_s[0]
        minimal = [i for i in gta_s[1:] if i <= a]
        more = [i for i in gta_s[1:] if i > a]
    return merge(minimal) + [a] + merge(more)