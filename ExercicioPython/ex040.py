from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1

    if passo < 0:
        passo *= -1

    print("=-" * 20)
    print(f'A contage é de {inicio} até {fim} em {passo}')
    sleep(2)
    if(inicio < fim):
        cont = inicio
        while cont <= fim:
            print(f"{cont}", end=' ')
            sleep(0.5)
            cont += passo
        print(" Fim!")
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= passo
        print("FIM!")

#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)

print("Agora é sua vez de personalizar!")

ini = int(input("Digite o inicio: "))
fim = int(input("Digite o fim: "))
passo = int(input("Digite o passo: "))

contador(ini, fim, passo)
