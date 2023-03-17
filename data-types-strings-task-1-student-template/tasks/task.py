def get_fractions(a_b: str, c_b: str) -> str:
    a=[]
    c=[]
    sum = 0
    for i in a_b.split('/'):
        a.append(i)
    for i in c_b.split('/'):
        c.append(i)
    sum = int(a[0])+int(c[0])
    result = a_b + ' + ' + c_b + ' = ' + str(sum) + '/' + str(a[1])
    return result