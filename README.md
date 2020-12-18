# eyeTracking
## C209 - Laboratório

|Nome|Matrícula|Curso|
|---------|---------|---------|
|Danilo Ribeiro|1411|Eng. Computação|
|Gustavo Simões|1470|Eng. Computação|
|Rafaela Ferraz|1461|Eng. Computação|
|Rairon Ferreira|1519|Eng. Computação|

---
## Introdução

Este trabalho tem o intúito de apresentar alguns dos conteúdos estudados nesta disciplina durante este semestre, assim como, uma solução para a identificação de olhos (*eye tracking*) baseado em vídeo.

Clique [aqui](https://www.youtube.com/watch?v=SEVcy4dxWTY) para acessar o vídeo da apresentação do projeto.

## Instalação

Para a instalação faça o download do arquivo zip [aqui](https://github.com/dmax101/eyeTracking.git).

Extraia o conteúdo em uma pasta.

![Download Zip](/assets/zip.png)


Se preferir você pode clonar o projeto com o git, caso tenha instalado em sua máquina executando o comando:

```
$ git clone https://github.com/dmax101/eyeTracking.git
```

Este comando irá criar uma pasta com o nome do projeto "eyeTracking".

---
## Instruções para a execução
Este projeto foi feito em Python e utiliza a biblioteca OpenCV que precisa estar instalada. Para isso execute o seguinte comando no terminal:

```
$ pip install opencv-python
```
Será necessário instalar as bibliotecas Scipy e Matplotlib

```
$ pip install matplotlib
$ pip install scipy
```

Pronto. Agora o projeto está preparado para ser executado. Execute o seguinte comando para iniciar:

```
$ python haarCascadeDetection.py
```

---
## Programa
Após a execução a câmera irá aparecer em uma janela e se a aplicação identificar um rosto e os olhos criará um círculo conforme a imagem a seguir:

![Janela da Aplicação](/assets/frame.png)

Ps.: Para uma melhor detecção, o ambiente deverá estar bem iluminado.

Para salvar uma captura do frame clique em "Salvar...me" e um arquivo será criado com o nome "saved_image.png"

### Encerramento da aplicação
Para encerrar a aplicação precione `ctrl + c` no terminal.

---

## Compressão e descompressão de imagem
Com o arquivo "saved_image.png" gerado anteriormente pelo eyeTraking, precisamos rodar o script de compressão e descompressão. Digite o comando para iniciar:

```
$ python compression.py
```