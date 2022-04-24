import cv2


def custom_cascade():
    (width, height) = (130, 100)

# '0' is used for my webcam,
# if you've any other camera
#  attached use '1' like this
# face_cascade = cv2.CascadeClassifier(
#     cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    face_cascade = cv2.CascadeClassifier(
        r"C:\Users\NaifBalbaid\Downloads\face-detection-data-master\face-detection-data-master\Training-Data\classifier\cascade.xml")
    webcam = cv2.VideoCapture(0)

    # The program loops until it has 30 images of the face.
    count = 1
    while True:
        (_, im) = webcam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 3)
        print(faces)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (width, height))
        count += 1

        cv2.imshow('OpenCV', im)
        key = cv2.waitKey(10)
        if key == 27:
            break


def haar_cascade():
    (width, height) = (130, 100)

# '0' is used for my webcam,
# if you've any other camera
#  attached use '1' like this
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    # face_cascade = cv2.CascadeClassifier(
    #     r"C:\Users\NaifBalbaid\Downloads\face-detection-data-master\face-detection-data-master\Training-Data\classifier\cascade.xml")
    webcam = cv2.VideoCapture(0)

    # The program loops until it has 30 images of the face.
    count = 1
    while True:
        (_, im) = webcam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 4)
        print(faces)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (width, height))
        count += 1

        cv2.imshow('OpenCV', im)
        key = cv2.waitKey(10)
        if key == 27:
            break


custom_cascade()
