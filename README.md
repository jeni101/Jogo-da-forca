# Jogo da Forca

Este é um jogo simples de forca em Python que simula o tradicional jogo da forca, com palavras aleatórias geradas a cada rodada.

## Requisitos

Este projeto utiliza a biblioteca `random-word` para gerar palavras aleatórias.

### Como instalar as dependências

Para instalar as dependências necessárias, execute o seguinte comando no terminal:

pip install -r requirements.txt

### Como jogar

1. Clone o repositório usando o comando:
    ```
    git clone https://github.com/jeni101/Jogo-da-forca.git
    ```
2. Acesse a pasta do repositório:
    ```
    cd Jogo-da-forca
    ```
3. Instale as dependências:
    ```
    pip install -r requirements.txt
    ```
4. Execute o arquivo `hangman.py` para jogar:
    ```
    python hangman.py
    ```

### Observações:
Esta é a versão simples do jogo, então fique atento às seguintes regras:

- **Chutes de letras repetidas:** Letras repetidas serão tratadas como chutes novos. Caso a letra não esteja na palavra, você perderá uma vida.
- **Entrada válida: Apenas uma letra por vez é permitida.
- **Vidas limitadas: Você tem 6 vidas/tentativas para acertar a palavra. Caso as vidas acabem sem acertar, o jogo será encerrado e a palavra será revelada.

Com isso em mente, divirta-se jogando! Boa sorte! 🎉
