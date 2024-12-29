from random_word import RandomWords
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()

# Inicializa a classe RandomWords
r = RandomWords()

# Gera uma palavra aleatória
palavra_aleatoria = r.get_random_word().lower()

# Configuração inicial para jogo
palavra_oculta = ['_'] * len(palavra_aleatoria)
vidas = 6

print("Bem-vindo ao jogo da forca!")
print(' '.join(palavra_oculta))

while '_' in palavra_oculta and vidas > 0:
    chute = input("\nEscolha uma letra: ").lower()
    
    if len(chute) != 1 or not chute.isalpha():
        print("Por favor, insira apenas uma letra válida!")
        continue

    if chute in palavra_aleatoria:
        for i, letra in enumerate(palavra_aleatoria):
            if letra == chute:
                palavra_oculta[i] = letra
        limpar_tela()
        print(f"Boa! A letra '{chute}' está na palavra.\n")
    else:
        vidas -= 1
        limpar_tela()
        print(f"A letra '{chute}' não está na palavra. Você perdeu uma vida. Vidas restantes: {vidas}\n")
    
    print(' '.join(palavra_oculta))


if '_' not in palavra_oculta:
    print("\nParabéns! Você acertou a palavra:", palavra_aleatoria)
else:
    print("\nVocê perdeu! A palavra era:", palavra_aleatoria)