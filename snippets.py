import cv2
import mediapipe as mp


def detectHands(frame):
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=4, min_detection_confidence=0.5)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    mp_drawing = mp.solutions.drawing_utils
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # print(hand_landmarks.landmark)
            if(hand_landmarks.landmark[5].y > hand_landmarks.landmark[17].y):
                print("left")
            else:
                print("right")
            for id , lm in enumerate(hand_landmarks.landmark):
                print(id, lm.x, lm)

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)




def face_landmarks(frame):
    mp_face_mesh = mp.solutions.face_mesh
    faceMesh = mp_face_mesh.FaceMesh(max_num_faces=2)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(rgb_frame)
    mp_drawing = mp.solutions.drawing_utils
    drawSpec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(frame, face_landmarks, mp_face_mesh.FACEMESH_CONTOURS,drawSpec,drawSpec)
            for id, lm in enumerate(face_landmarks.landmark):
                ih, iw , c = frame.shape
                x, y = int(lm.x*iw), int(lm.y*ih)
                print(id , x , y)


cap = cv2.VideoCapture(0)
frameWidth = 640
frameHeight = 480
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    #detectHands(frame)
    face_landmarks(frame)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
