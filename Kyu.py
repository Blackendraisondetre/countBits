def countBits(n):
    amount = 0
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    for x in b:
        print(x)
        if x == '1': amount = amount + 1
        else : amount = amount + 0
    return (amount)




