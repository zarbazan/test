i = 0
a = 1

def test(b):
    b+=b
    return b


while (i < 10):
    a, c = test(a), test(a)

    print(a, c)
    i+=1



P 1000.0 I 1010.0 D 500.0
P 100000.0 I 101000.0 D 50000.0
1000 1000 -0.7562469138557764
