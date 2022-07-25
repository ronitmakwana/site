
# import numpy as np
# import cv2
 
# #Create the circle
# colour = (0,255,0)
# lineWidth = 3       #-1 will result in filled circle
# radius = 0
# point = (0,0)

# #function for detecting left mouse click
# def click(event, x,y, flags, param):
#     global point, pressed
    
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print("Pressed", x,y)
#         point = (x,y)
#         return point
         
# #event handler
# cv2.namedWindow("Frame")      #must match the imshow 1st argument
# cap = cv2.VideoCapture('D8dog1.avi')
# mask_Cir = []
# #Loop for video stream
# while (True):
     
#     stream = cv2.waitKey(20)   #Load video every 1ms and to detect user entered key
     
#     #Read from videoCapture stream and display
#     ret,frame = cap.read()
#     cv2.setMouseCallback("Frame", click)
    
#     mask = np.zeros(frame.shape, dtype=np.uint8) 
#     # mask_Cir.append(point)
#     # for i in mask_Cir:
#     #     mask = cv2.circle(mask,i, 50, (255,255,255), -1) 
#     #     result = cv2.bitwise_or(frame, mask)
#     #     cv2.imshow('Frame', result)
#     mask = cv2.circle(mask,point, 300, (255,255,255), -1) 
#     result = cv2.bitwise_and(frame, mask)
#     cv2.imshow('Frame', result)
     
#     if stream & 0XFF == ord('q'):  #If statement to stop loop,Letter 'q' is the escape key
#         break                      #get out of loop
         
# cap.release()
# cv2.destroyAllWindows()



import numpy as np
import cv2
ix,iy,sx,sy = -1,-1,-1,-1
new_pol = 00
mask_vid = 00
pts = []
# mouse callback function
def draw_lines(event, x, y, flags, param):
    global ix,iy,sx,sy,mask_vid,new_pol
    # if the left mouse button was clicked, record the starting
    if event == cv2.EVENT_LBUTTONDOWN:
        if new_pol == 11:
            pts.clear()
            print('new polygon >>>>>>>>>>>>>>>>>>>>>>>>>>')
            ix = -1
            new_pol = 00            
        # draw circle of 2px
        cv2.circle(im, (x, y), 3, (0, 0, 127), -1)
        pts.append((x,y))
        print(pts)
        if ix != -1: # if ix and iy are not first points, then draw a line
            cv2.line(im, (ix, iy), (x, y), (0, 0, 127), 2, cv2.LINE_AA)
        else: # if ix and iy are first points, store as starting points
            sx, sy = x, y
        ix,iy = x, y
        
    elif event == cv2.EVENT_MBUTTONDOWN:
        # if flags == 33: # if alt key is pressed, create line between start and end points to create polygon
        cv2.line(im, (ix, iy), (x, y), (0, 0, 127), 2, cv2.LINE_AA)
        cv2.line(im, (x, y), (sx, sy), (0, 0, 127), 2, cv2.LINE_AA)
        pts.append((x,y))
        cv2.fillPoly(im, np.array([pts]), (255, 255, 255))        
        mask_vid = 11
        ix, iy = -1, -1 # reset ix and iy
        new_pol = 11
        return mask_vid
# read image from path and add callback
cap = cv2.VideoCapture('D8dog1.avi')  #D8dog1.avi
im = cv2.imread('122.png')
im = cv2.resize(im, dsize=(1500, 900))
cv2.namedWindow("OpenCV")
x, y = 0, 0
while(1):
    rat, frame = cap.read()
    mask = np.zeros(frame.shape, dtype=np.uint8)
    frame = cv2.resize(frame, dsize=(1500, 900))   
    cv2.setMouseCallback('OpenCV',draw_lines)  
    # print(pts)
    
    # print(polygon)
    # try:
    # print('poly', polygon)
    if mask_vid == 11:            
        frame = cv2.bitwise_and(frame, im)                                 
# except:
    else:
        frame = cv2.bitwise_or(frame, im)
    cv2.imshow("OpenCV",frame)

    if cv2.waitKey(25) & 0XFF == ord('q'):  #If statement to stop loop,Letter 'q' is the escape key
        break                      #get out of loop
    
cap.release()
cv2.destroyAllWindows()

