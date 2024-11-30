import random

def jogar_moeda():
    """Joga uma moeda para decidir quem começa."""
    resultado = random.choice(["jogador", "computador"])
    print(f"A moeda foi jogada... Quem começa é: {resultado.upper()}")
    return resultado

def jogador_tenta_adivinhar(numero_secreto):
    """Lógica para o jogador tentar adivinhar o número do computador."""
    tentativas = 0
    print("Tente adivinhar o número escolhido pelo computador!")
    
    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        tentativas += 1
        if palpite < numero_secreto:
            print("O número é maior!")
        elif palpite > numero_secreto:
            print("O número é menor!")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
            break

def computador_tenta_adivinhar(inicio, fim, numero_escolhido):
    """Lógica para o computador tentar adivinhar o número do jogador usando pesquisa binária."""
    tentativas = 0
    print(f"O computador irá tentar adivinhar o número entre {inicio} e {fim}.")
    
    while inicio <= fim:
        palpite = (inicio + fim) // 2
        tentativas += 1
        print(f"O computador chutou: {palpite}")
        
        resposta = input("O número é maior, menor ou correto? (Digite 'maior', 'menor' ou 'correto'): ").strip().lower()
        if resposta == "maior":
            inicio = palpite + 1
        elif resposta == "menor":
            fim = palpite - 1
        elif resposta == "correto":
            print(f"O computador acertou o número {numero_escolhido} em {tentativas} tentativas!")
            break
        else:
            print("Resposta inválida. Por favor, responda com 'maior', 'menor' ou 'correto'.")

def jogar_adivinhacao():
    """Inicia o jogo com a lógica de escolha e adivinhação."""
    print("Bem-vindo ao Jogo da Adivinhação com Moeda!")
    inicio = int(input("Defina o número inicial do intervalo: "))
    fim = int(input("Defina o número final do intervalo: "))

    if inicio >= fim:
        print("O intervalo é inválido. O número inicial deve ser menor que o final.")
        return

    quem_comeca = jogar_moeda()
    
    if quem_comeca == "jogador":
        print("Você começa escolhendo um número para o computador adivinhar!")
        numero_escolhido = int(input(f"Escolha um número entre {inicio} e {fim}: "))
        if numero_escolhido < inicio or numero_escolhido > fim:
            print("Número fora do intervalo!")
            return
        computador_tenta_adivinhar(inicio, fim, numero_escolhido)
    else:
        print("O computador começa escolhendo um número para você adivinhar!")
        numero_secreto = random.randint(inicio, fim)
        jogador_tenta_adivinhar(numero_secreto)

# Executa o jogo
if __name__ == "__main__":
    jogar_adivinhacao()
