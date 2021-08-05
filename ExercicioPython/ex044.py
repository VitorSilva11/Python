
def fatorial(num, show=False):
    fat = 1
    for cont in range(num, 0, -1):
        fat *= cont
        if show == True:
            print(f'{cont}', end='')

            if cont > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')

    return fat



print(fatorial(5, show=True))


