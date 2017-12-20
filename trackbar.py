#import opencv library
import cv2
import numpy

frame = cv2.imread('dove.png')

def hsv_shift():
    frame = cv2.imread('dove.png')

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV);
    
    int_h = cv2.getTrackbarPos('Hue', 'frame')
    int_s = cv2.getTrackbarPos('Saturation', 'frame')
    int_v = cv2.getTrackbarPos('Value', 'frame')

    hue_shift = (int_h - 180.0) / 2.0
    s_shift = (int_s - 100.0) / 100.0
    v_shift = (int_v - 100.0) / 100.0

    for j in range(0, hsv_frame.shape[0]):
        for i in range(0, hsv_frame.shape[1]):
            h = frame[j, i, 0]
            s = frame[j, i, 1]
            v = frame[j, i, 2]

            h_plus_shift = h;
            h_plus_shift += hue_shift;

            if h_plus_shift < 0:
                h = 180 + h_plus_shift
            elif h_plus_shift > 180:
                h = h_plus_shift - 180
            else:
		h = h_plus_shift

	    hsv_frame[j, i, 0] = h

	    s_plus_shift = s + 255.0*s_shift;

            if s_plus_shift < 0:
		s_plus_shift = 0
	    elif s_plus_shift > 255:
		s_plus_shift = 255
		
	    hsv_frame[j, i, 1] = s_plus_shift

	    v_plus_shift = v + 255.0*v_shift

            if v_plus_shift < 0:
		v_plus_shift = 0
	    elif v_plus_shift > 255:
		v_plus_shift = 255

	    hsv_frame[j, i, 2] = v_plus_shift



    frame = cv2.cvtColor(hsv_frame, cv2.COLOR_HSV2BGR);

    cv2.imshow('frame', frame);

    

def onHueTrackbarChange(trackbarValue):
    hsv_shift()

def onSaturationTrackbarChange(trackbarValue):
    hsv_shift()

def onValueTrackbarChange(trackbarValue):
    hsv_shift() 

if frame is None:
    exit()


cv2.namedWindow('frame', cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('Hue', 'frame', 180, 360, onHueTrackbarChange)
cv2.createTrackbar('Saturation', 'frame', 100, 200, onSaturationTrackbarChange)
cv2.createTrackbar('Value', 'frame', 100, 200, onValueTrackbarChange)
cv2.imshow('frame', frame);

hsv_shift()

cv2.waitKey()
cv2.destroyAllWindows() 
