import cv2
import mediapipe as mp
import numpy as np
from math import acos, degrees
#Voy a hacer un código el cual analize en tiempo real los 21 puntos de la mano que analiza mediapipe

"""
STATIC_IMAGE_MODE
    Por defecto: False
        Si es False = Trata a las imagenes de entrada como un video scream. Aplica la detección de la palma y el modelo Hand LandMarks, pero usa tracking(se actualiza para obtener la nueva ubicación de la palma)
        Si es True = Los detectores se aplican en cada imagen, mejor usarla con imagenes sin relación entre sí
MAX_NUM_HANDS (número máximo de manos a detectar)
    Por defecto: 2
MIN_DETECTION_CONFIDENCE (Valor mínimo de confianza del modelo de detección de manos, para que la detección sea considerada como exitosa)
    Por defecto: 0.5
MIN_TRACKING_CONFIDENCE (valor mínimo de confianza del modelo de rastreo de los 21 puntos de la palma de los LandMarks, para que el rastreo sea considerado exitoso)
    Por defecto: 0.5 (en caso de no ser exitoso, se invoca al detector de manos nuevamente en la siguiente imagen, si STATIC_IMAGE_MODE es TRUE este es ignorado)
"""

mp_drawing = mp.solutions.drawing_utils #Dibuja los resultados de las conexiones con los puntos
mp_hands = mp.solutions.hands
cap =cv2.VideoCapture(0, cv2.CAP_DSHOW) #Toma el video desde la web cam

with mp_hands.Hands(
    static_image_mode = False,
    model_complexity = 1,
    max_num_hands = 2,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5) as hands:

    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        height, width, _ = frame.shape
        frame = cv2.flip(frame, 1) #Voltea los fotogramas

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resultado = hands.process(frame_rgb)
        if resultado.multi_hand_landmarks is not None:
            for hand_landmarks in resultado.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
cv2.release()
cv2.destroyAllWindows()
