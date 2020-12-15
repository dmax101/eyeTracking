from __future__ import print_function
from cv2 import cv2 # pip install opencv-python
import argparse


def detectAndDisplay(frame):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)
    # Detectar faces
    # Divide a imagem em diversos retângulos e retorna uma lista com eles
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        # Elipses rosas
        frame = cv2.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h,x:x+w]

        # Em cada face, detectar olhos
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            # Circulos azuis
            frame = cv2.circle(frame, eye_center, radius, (255, 0, 0 ), 4)

    # Frame invertido horizontalmente por questão de estética =)       
    frame = cv2.flip(frame, 1)
    cv2.imshow('Deteccao de Face e Olho', frame)
    return frame

def onPressed1(state):
  if state == 1:
    ret, frame = cap.read() # Não podíamos alterar nada aqui
    frame = detectAndDisplay(frame)
    cv2.imwrite("saved_image.png", frame)
    print('Frame salvo com sucesso!')

def onPressed2(state):
  if state == 1:
    img = cv2.imread("saved_image.png")
    if img is None:
        print('Não foi possível ler o frame.')
    else:
        cv2.imshow("Frame salvo", img)        

parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')

# Definindo os cascades. Existem alguns deles nas pastas 'haarcascades' e 'lbpcascades'
parser.add_argument('--face_cascade', help='Path to face cascade.', default='haarcascades/haarcascade_frontalface_alt.xml')
parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default='haarcascades/haarcascade_eye_tree_eyeglasses.xml')
parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)
args = parser.parse_args()
face_cascade_name = args.face_cascade
eyes_cascade_name = args.eyes_cascade

# Modelos pré-treinados de Cascade Classifiers
face_cascade = cv2.CascadeClassifier()
eyes_cascade = cv2.CascadeClassifier()
# Etapa 1. Carregar os cascades
if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):
    print('--(!) Erro ao carregar face_cascade')
    exit(0)
if not eyes_cascade.load(cv2.samples.findFile(eyes_cascade_name)):
    print('--(!) Erro ao carregar eyes_cascade')
    exit(0)
camera_device = args.camera
# Etapa 2. Ler o video da camera
cap = cv2.VideoCapture(camera_device)
if not cap.isOpened:
    print('--(!) Erro ao abrir a captura de video')
    exit(0)


while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) Frame não foi capturado -- Break!')
        break
    detectAndDisplay(frame)
    button1state = 0
    cv2.createTrackbar(
      "Salvar",
      "Deteccao de Face e Olho",
      button1state,
      1,
      onPressed1)
    
    button2state = 0
    cv2.createTrackbar(
      "Mostrar",
      "Deteccao de Face e Olho",
      button2state,
      1,
      onPressed2)
    if cv2.waitKey(10) == 27:
        break