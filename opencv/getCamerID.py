import cv2
ID = 0
for x in range(0,10000):
    cap = cv2.VideoCapture(ID)
    # get a frame
    ret, frame = cap.read()
    if ret == False:
        ID += 1
    else:
        print(ID)
        break
    