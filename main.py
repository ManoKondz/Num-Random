from random import randint
user_loop = int(input("Quantas vezes você quer que o loop se repita: "))
error = 0
sux = 0
for i in range(user_loop):
    num = randint(1,3)
    user = int(input("Qual número foi gerado?\n"))
    if user > 3 or user < 1:
        user = int(input("Número inválido, digite um número válido\n"))
    elif num == user:
        print("Você acertou!")
        print("O número gerado foi = ", num)
        sux += 1
    else:
        print("Você errou, tente outra vez!")
        print("O número gerado foi = ", num)
        error += 1
print(f"Você acertou {sux} vezes")
print(f"Você errou {error} vezes")
percent = ( sux / 5) * 100
percenter = ( error /5) * 100
print(f"Você acertou {percent}% das questões")
print(f"Você acertou {percenter}% das questões")
if sux > error:
    print("Você ganhou!")
elif sux == error:
    print("Você empatou!")
else:
    print("Você perdeu!")