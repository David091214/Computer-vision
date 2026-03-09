# first is to load the  video 
import cv2
video = cv2.VideoCapture("./mountain.mp4")

# check if video was cpatured
while True:
    ret, frame = video.read()
    if not ret:
       break
    cv2.imshow("Video window", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows