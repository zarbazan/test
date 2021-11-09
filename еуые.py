i = 0
a = 1
c = 2

def test(b, d):
    b+=b
    d=d**2
    return b, d


while (i < 10):
    a, c = test(a, c)

    print(a, c, -c)
    i+=1



