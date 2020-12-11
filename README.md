# eyeTracking
## C209 - Laboratório

|Nome|Matrícula|Curso|
|---------|---------|---------|
|Danilo Ribeiro|1411|Eng. Computação|
|Gustavo|XXXX|Eng. Computação|
|Rafaela|XXXX|Eng. Computação|
|Rairon|XXXX|Eng. Computação|

---
## Introdução

Este trabalho tem o intúito de apresentar alguns dos conteúdos estudados nesta disciplina durante este semestre, assim como, uma solução para a identificação de olhos (*eye tracking*) baseado em vídeo.

## Instalação

Para a instalação faça o download do arquivo zip [aqui](https://github.com/dmax101/eyeTracking.git).

Extraia o conteúdo em uma pasta.

![Download Zip](/assets/zip.png)


Se preferir você pode clonar o projeto com o git, caso tenha instalado em sua máquina executando o comando:

`$ git clone https://github.com/dmax101/eyeTracking.git`

Este comando irá criar uma pasta com o nome do projeto "eyeTracking".

---
## Instruções para a execução
Este projeto foi feito em Python e utiliza a biblioteca OpenCV que precisa estar instalada. Para isso execute o seguinte comando no terminal:

`$ pip install opencv-python`

Pronto. Agora o projeto está preparado para ser executado. Execute o seguinte comando para iniciar:

`$ python haarCascadeDetection.py`

---
## Programa
Após a execução a câmera irá aparecer em uma janela e se a aplicação identificar um rosto e os olhos criará um círculo conforme a imagem a seguir:
![Janela da Aplicação](/assets/saved_image.png)