# Gerador Blum Blum Shub (BBS) em Python

Implementação simples do gerador de bits pseudoaleatórios **Blum Blum Shub (BBS)**.

## O que é o BBS

O BBS é um gerador de bits pseudoaleatórios criptograficamente seguro (CSPRBG). Sua segurança se baseia na dificuldade de fatorar `n = p × q`.

Funcionamento:

1. Escolhem-se dois primos grandes `p` e `q`, ambos com `p ≡ q ≡ 3 (mod 4)`.
2. Calcula-se `n = p × q`.
3. Escolhe-se uma semente `s`, coprima de `n` (`gcd(s, n) = 1`).
4. Calcula-se o estado inicial: `x0 = s² mod n`.
5. A cada passo: `x_i = (x_{i-1})² mod n`, e o bit de saída é o bit menos significativo de `x_i` (`x_i mod 2`).

## Parâmetros utilizados

| Parâmetro | Valor | Observação |
|-----------|-------|------------|
| `p` | 10007 | primo, 10007 mod 4 = 3 |
| `q` | 10039 | primo, 10039 mod 4 = 3 |
| `n` | 100460273 | `p × q` |
| `s` | 123457 | `gcd(s, n) = 1` |
| Bits gerados | 1.000.000 | tamanho adequado para os testes NIST |

Os valores de `p`, `q` e `s` ficam na linha `p, q, s = ...` do bloco principal do código e podem ser alterados.

> **Atenção:** o período da sequência depende de `p`, `q` e `s`. Se for menor que a quantidade de bits gerados, a sequência se repete e os testes NIST tendem a falhar. Com os valores acima, o período é 1.785.714, maior que 1.000.000 de bits.

## Estrutura do código

| Parte | Função |
|-------|--------|
| `eh_primo(n)` | Verifica se `n` é primo por divisão por tentativas. |
| `erro(msg)` | Mostra uma mensagem de erro na tela e encerra o programa. |
| `bbs(p, q, s, n_bits)` | Valida as premissas do algoritmo e gera a lista de bits. |
| Bloco principal | Define `p`, `q`, `s`, gera a sequência, salva em arquivo e mostra um resumo. |

As validações feitas antes de gerar os bits são: `p` e `q` primos, `p ≡ 3 (mod 4)`, `q ≡ 3 (mod 4)`, `p ≠ q` e `gcd(s, n) = 1`. Se alguma falhar, o programa mostra a mensagem `ERRO: ...` e para.


### 1. Executar

Abra o terminal na pasta onde está o arquivo e rode:

**Windows**
```
python blum.py
```

**Linux / Mac**
```
python3 blum.py
```

Também é possível executar pelo VS Code, clicando em "Run Python File".

### 2. Saída esperada

```
Salvo em: <pasta do script>/sequencia_bbs.txt
p=10007, q=10039, n=100460273, s=123457
Primeiros 64 bits: 1110010111010001100101100001100101001010000010010111101110110110
Quantidade de 1s: 500396 de 1000000
```

O programa cria o arquivo `sequencia_bbs.txt` **na mesma pasta do script**, contendo os 1.000.000 de bits (apenas 0 e 1, sem espaços).

## Testes NIST SP 800-22

Para validar a aleatoriedade da sequência foi usada a ferramenta online:

https://zsomotech.com/random-bitstream-tester/

Passos:

1. Abra o arquivo `sequencia_bbs.txt` e copie todo o conteúdo.
2. Na página, escolha **Manual bitstream input** e cole a sequência.
3. Clique em **Start Test**.
4. Cada teste gera um *p-value*: se for **≥ 0,01**, a sequência passa naquele teste.


