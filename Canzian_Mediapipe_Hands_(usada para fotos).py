import cv2
import mediapipe as mp

""" Opciones de configuración:
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

with mp_hands.Hands( #Configurar las opciones de configuración
    static_image_mode = True,
    max_num_hands = 2,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5) as hands:

    image = cv2.imread("palmas.jpg") #Lee la imagen
    height, width, _ = image.shape #Saca ancho y altura de la imagen
    image = cv2.flip(image, 1) #Da vuelta la imagen

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #Pasa la imagen de BGR a RGB (necesita q sea RGB para las detecciones)

    results = hands.process(image_rgb)
    """
    HANDEDNESS: print("Handedness: ", results.multi_handedness)
    Sirve para 3 valores: index (enumera las palmas detectadas), score (probabilidad de que sea la dicha) y label (mano right o left)
    HAND LAND_MARKS: print("Hand Land_Marks: ", results.multi_hand_landmarks)
    Representa las posiciones (x, y, z) en decimales no enteros, de la lista de 21 puntos de coordenadas de la mano
    """

    if results.multi_hand_landmarks is not None:
        #---------------------------------------------------------------------------------------------------------------------------------------
        #Dibujar los puntos y sus conexiones con mediapipe
        for hand_landmarks in results.multi_hand_landmarks: #Recorre cada grupo de 21 puntos por cada mano detectada
            #print(hand_landmarks) # Los 21 puntos por cada mano en cada iteración
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS, 
                            #(donde queremos)(los 21 puntos)(para que se dibujen las conecciónes entre los puntos) 
                                        mp_drawing.DrawingSpec(color=(100,100,100), thickness = 4, circle_radius = 5), # Primero modifico los círculos
                                        mp_drawing.DrawingSpec(color=(240,240,0), thickness = 4, circle_radius = 5)) # Segundo modifico las líneas
    


    image = cv2.flip(image, 1) #Da vuelta la imagen
cv2.imshow("palmas", image) #Acá le pongo eel nombre a la imagen y la muestro
cv2.waitKey(0) #Delay
cv2.destroyAllWindows()

