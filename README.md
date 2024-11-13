Jogo de Seguir o Objeto

*Grupo:* Giuliano Campra, Lucas Patricio, Tiago Gimenes e Murilo Graciano

Este é um jogo interativo desenvolvido em Python, onde o jogador precisa mover um objeto (como uma bola) na tela para alcançar alvos. O controle do jogo é feito utilizando uma câmera, e a movimentação do objeto é detectada por meio de um processo de detecção de imagem, utilizando a biblioteca OpenCV.

## Como Jogar

1. *Início do Jogo:*
   Ao iniciar o jogo, o jogador terá 5 segundos de contagem regressiva enquanto a área central da tela é identificada. Durante essa contagem, a câmera captura a cor média da área central da tela, que será usada para identificar o objeto controlado pelo jogador.

2. *Controle do Objeto:*
   O jogador deve mover um objeto (por exemplo, uma bola) dentro da área visível da câmera, de modo que ele seja detectado pela cor que foi capturada na etapa anterior.

Nota Importante: O objeto utilizado pelo jogador não deve ser de cor preta ou branca, para evitar interferências com o ambiente externo e garantir que a detecção de cor funcione corretamente.

3. *Alvos:*
   O jogo gera aleatoriamente alvos (círculos vermelhos) que o jogador deve alcançar. O jogador deve mover o objeto até o centro de cada alvo. O objetivo é acertar os alvos dentro de um tempo limite (3 segundos por alvo).

4. *Fases do Jogo:*
   - O jogo começa com a detecção da cor do objeto e a exibição de alvos na tela.
   - Cada alvo acertado aumenta a pontuação do jogador.
   - Após acertar todos os alvos, uma mensagem de "Parabéns!" será exibida.
   - Se o tempo para acertar um alvo for excedido, o jogo terminará.

5. *Controles:*
   - *Pressione 'q' para sair.*
   - **Pressione 'p' para reiniciar o jogo.

## Funcionalidades

- *Detecção de Objeto:* O jogo utiliza a câmera para capturar a cor do objeto e detectar sua posição na tela em tempo real.
- *Detecção de Alvos:* Círculos vermelhos aleatórios aparecem na tela. O jogador deve mover o objeto até o centro desses círculos para marcar um ponto.
- *Contagem Regresiva:* Antes do jogo começar, há uma contagem regressiva de 5 segundos, e a área central da tela é destacada para capturar a cor do objeto.
- *Detecção de Falhas:* Se o tempo para atingir um alvo for excedido (3 segundos), o jogo é finalizado e o jogador pode optar por reiniciar ou sair.

## Requisitos

- *Python 3.12.7*
- *Bibliotecas:*
  - OpenCV (cv2)
  - NumPy

Para instalar as dependências, use:

bash
pip install opencv-python numpy


## Como Rodar

1. Clone o repositório do projeto.
2. Execute o script Python follow_object.py:

bash
python follow_object.py


## Estrutura do Código

- *Função iniciar_jogo()*: Controla o fluxo principal do jogo, incluindo a contagem regressiva, captura da cor do objeto e a lógica de detecção de alvos.
- *Função contagem_regressiva()*: Exibe o tempo restante antes do início do jogo e destaca a área central da tela para captura de cor.
- *Detecção de Cor:* A cor do objeto é capturada da área central da tela e usada para identificar o objeto em movimento.
- *Lógica de Alvos:* A cada 3 segundos, um novo alvo é gerado. O jogador precisa mover o objeto até o centro do alvo para marcá-lo como atingido.
