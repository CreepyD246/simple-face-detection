import cv2 # OpenCV Library

# Insert path to haarcascade in the string variable below.
path = "path\\to\\haarcascade\\in\\here"

# Reference to HaarCascade
cascade = cv2.CascadeClassifier(path)

# Reference to webcam
video = cv2.VideoCapture(0)

# Loop to capture webcam footage and display current image
while True:
    success, image = video.read() # Retrieving current frame
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Converting current frame to gray image

    # Detecting faces
    faces = cascade.detectMultiScale(gray_scale, 1.2, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2) # Drawing rectangle

    # Displaying the result
    cv2.imshow("img", image)
    cv2.waitKey(1)