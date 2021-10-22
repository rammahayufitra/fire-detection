import cv2
import numpy as np

video = cv2.VideoCapture('./video/fire.mp4')

frame_width = int(video.get(3))
frame_height = int(video.get(4))
save_output = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while True:
    ret, frame = video.read()
    blur = cv2.GaussianBlur(frame,(15,15),0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    lower = [10,50,50]
    upper = [35,255,255]
    lower = np.array(lower, dtype='uint8')
    upper = np.array(upper, dtype='uint8')
    mask = cv2.inRange(hsv,lower,upper)
    output = cv2.bitwise_and(frame, hsv, mask = mask)
    number_of_total = cv2.countNonZero(mask)
    if int(number_of_total) > 15000:
        print("fire detected")
    if ret == False:
        break
    cv2.putText(output,"Fire Detected",(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(209, 80, 0, 255), 3)
    save_output.write(output)
    cv2.imshow('frame', frame)
    cv2.imshow('fire', output)
    if cv2.waitKey(30) &0xFF == ord('q'):
        break

video.release()
save_output.release()
cv2.destroyAllWindows()



