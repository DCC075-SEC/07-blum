
import os                # usado para descobrir a pasta do script
import sys               # usado para encerrar o programa em caso de erro
from math import gcd     # máximo divisor comum (MDC), usado para checar a semente


# Verifica se um número é primo por divisão por tentativas.
# Basta testar divisores até a raiz quadrada de n.
def eh_primo(n):
    if n < 2:            
        return False
    i = 2
    while i * i <= n:    # testa divisores de 2 até sqrt(n)
        if n % i == 0:   
            return False
        i += 1
    return True          # nenhum divisor encontrado, é primo


# Mostra uma mensagem de erro na tela e encerra o programa.
def erro(msg):
    print("ERRO:", msg)
    sys.exit(1)


# Implementação do BBS: recebe p, q, a semente s e a quantidade
# de bits desejada, e devolve uma lista de bits (0 e 1).
def bbs(p, q, s, n_bits):
    #Validação das premissas do algoritmo 
    if not eh_primo(p):
        erro(f"p = {p} não é primo.")
    if not eh_primo(q):
        erro(f"q = {q} não é primo.")
    if p % 4 != 3:      # exigência do BBS: p ≡ 3 (mod 4)
        erro(f"p = {p} não é congruente a 3 (mod 4).")
    if q % 4 != 3:      # exigência do BBS: q ≡ 3 (mod 4)
        erro(f"q = {q} não é congruente a 3 (mod 4).")
    if p == q:          
        erro("p e q devem ser diferentes.")

    n = p * q           # módulo do gerador

    # A semente deve ser coprima de n (MDC = 1), ou seja,
    # não pode ser múltipla de p nem de q.
    if gcd(s, n) != 1:
        erro(f"s = {s} não é coprimo de n = {n}.")

    # Geração da sequência 
    x = (s * s) % n              # estado inicial
    bits = []
    for _ in range(n_bits):
        x = (x * x) % n          # próximo estado
        bits.append(x % 2)       # bit de saída: bit menos significativo (LSB)
    return bits


# Bloco principal: só executa quando o arquivo é rodado diretamente.
if __name__ == "__main__":
    # Parâmetros do gerador: dois primos p e q (> 10000, ≡ 3 mod 4)
    # e a semente s
    p, q, s = 10007, 10039, 123457

    # Quantidade de bits a gerar (a suíte NIST precisa de sequências longas)
    N_BITS = 1_000_000

    # Gera os bits e junta tudo em uma string, ex.: "1110010111..."
    bits = bbs(p, q, s, N_BITS)
    seq = "".join(map(str, bits))

    # Salva a sequência em um arquivo .txt na mesma pasta do script,
    # para colar depois na ferramenta de testes NIST
    caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sequencia_bbs.txt")
    with open(caminho, "w") as f:
        f.write(seq)

    # Resumo na tela
    print("Salvo em:", caminho)
    print(f"p={p}, q={q}, n={p*q}, s={s}")
    print(f"Primeiros 64 bits: {seq[:64]}")
    print(f"Quantidade de 1s: {sum(bits)} de {N_BITS}")   