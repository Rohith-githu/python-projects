import cv2

capture = cv2.VideoCapture(0)
capture.set(9,750)
capture.set(3,750)

while True:
    success, img = capture.read()
    cv2.imshow('Logitech c270',img)
    if cv2.waitKey(1) & 0xFF == ord('w'):
       break