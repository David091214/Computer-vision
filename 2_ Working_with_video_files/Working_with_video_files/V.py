# first is to load the  video 
import cv2 

video = cv2.VideoCapture(./"mountain.mp4")

while True:
    ret, frame = video.read()
    if not ret:
        break
    cv2.imshow("video project", video)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindowss


fourcc = cv2.VideoWriter_fourcc(*"mp4v") #the "v" is very important

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter("newwww.mp4", fourcc , 30 , (width, height))

while True:
    ret , frame = video.get()
    if not ret:
        break
    out.write(frame)

video.release()
out.release()
cv2.destroyAllWindows


   


