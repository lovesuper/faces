import os

import cv2

ix = 0
for root, directories, file_names in os.walk('/home/lovesuper/Documents/Photos/Male/Black'):
    if ix > 10:
        break

    for filename in file_names:
        try:
            imagePath = os.path.join(root, filename)
            image = cv2.imread(imagePath)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            faces = faceCascade.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=1, minSize=(300, 300))
            print("[INFO] Found {0} Faces.".format(len(faces)))
            (x, y, w, h) = faces[0]
            roi_color = image[y:y + h, x:x + w]
            print("[INFO] Object found. Saving locally.")
            cv2.imwrite('res/' + str(ix) + '.jpg', roi_color)
        except:
            pass
        else:
            print("saved.")
            ix += 1
