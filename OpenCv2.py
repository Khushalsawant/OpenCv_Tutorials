import numpy as np
import cv2


'''
Playing Video from file

https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html#display-video
'''
path_of_video = 'C:/Users/khushal/Pictures/Khushal_videos/khushal.mkv'

cap = cv2.VideoCapture(path_of_video)

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

'''
Save video file :
This time we create a VideoWriter object.
We should specify the output file name (eg: output.avi).
Then we should specify the FourCC code (details in next paragraph).
Then number of frames per second (fps) and frame size should be passed.
And last one is isColor flag. If it is True, encoder expect color frame, otherwise it works with grayscale frame.


'''

cap = cv2.VideoCapture(path_of_video)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('C:/Users/khushal/Pictures/Khushal_videos/khushal-1.mkv',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()