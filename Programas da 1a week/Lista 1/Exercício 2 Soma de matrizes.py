
def sameShape(m1, m2):
    if type(m1) != type(m2):
        return False
    if type(m1) == list:
        if len(m1) != len(m2):
            return False
        for i in range(len(m1)):
            if not sameShape(m1[i], m2[i]):
                return False

    return True

def soma_matrizes(m1, m2):
    if not sameShape(m1, m2):
        return False
    else:
        m1 = [i for j in m1 for i in j]
        m2 = [i for j in m2 for i in j]

        s = [sum(t) for t in zip(m1, m2)] 
        k = int(len(s) / 2)
        return [s[:k], s[k:]]
