import  face_recognition
import os

def perform_recogintion(image):
    result = [False]
    img1 = face_recognition.load_image_file(image)
    img1_encodings = face_recognition.face_encodings(img1)[0]
    for i in range(1,8):
        img2 = face_recognition.load_image_file(f'./images/image{i}.jpg')
        img2_encodings = face_recognition.face_encodings(img2)[0]
        result = face_recognition.compare_faces([img1_encodings],img2_encodings)
        if result == [True]:
            print(f"Match Found with image{i}")
            return
        else:
            print("Match Not Found...")
    pass


