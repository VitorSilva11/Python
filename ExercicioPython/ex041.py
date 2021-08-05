from time import sleep

def parmMaior(*num):
    print("=-" * 30)
    maior = 0
    print("Analisando os válores ",end="")
    for param in num:
        print(f"{param}", end=" ")
        sleep(0.5)
        if maior < param:
            maior = param

    print(f"- {len(num)} valores ao todo!")
    print(f"O maior número digitado foi: {maior}")

#principal
parmMaior(2, 9, 4, 5, 7, 1)
parmMaior(4, 7, 0)
parmMaior(1, 2)
parmMaior(6)
parmMaior(0)
