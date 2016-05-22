import cv
import datetime , time
import RPi.GPIO as GPIO
 
# ---------------------------
# Setup the webcam and font
# ---------------------------
 
# define image size
imageWidth = 640
imageHeight = 480
 
# create a window object
cv.NamedWindow("window1", cv.CV_WINDOW_AUTOSIZE)
camera_index = 0
 
# create a camera object
capture = cv.CaptureFromCAM(camera_index)
 
# set capture width and height
cv.SetCaptureProperty( capture, cv.CV_CAP_PROP_FRAME_WIDTH, imageWidth );
cv.SetCaptureProperty( capture, cv.CV_CAP_PROP_FRAME_HEIGHT, imageHeight );
 
# create a font
font = cv.InitFont(cv.CV_FONT_HERSHEY_COMPLEX_SMALL , 0.5, 0.5, 0, 1, cv.CV_AA)


GPIO.setmode(GPIO.BOARD)
sw = 11
GPIO.setup(11, GPIO.IN)

print "Hello, This is Capture photo program."
print "Press 'q' : to Ending program."
print "Press 'sw' : to Save the image."
print ""
time.sleep(0.5)
    

while True:
 
    # get image from webcam
    frame = cv.QueryFrame(capture)
 
    # -------------------------------------------
    # Draw the time stamp on a white background
    # -------------------------------------------  
    cv.Rectangle(frame, (0,0), (imageWidth, 15), (255,255,255),cv.CV_FILLED,8,0)
    # get the current date and time
    timeStampString = datetime.datetime.now().strftime("%A %Y-%m-%d %I:%M %p")
    # insert the date time in the image
    cv.PutText(frame, timeStampString, (10,10), font, (0,0,0))
 
    # -----------------------------
    # show the image on the screen
    # -----------------------------
    cv.ShowImage("window1", frame)
 
    # -----------------------
    # wait for user command
    # -----------------------
    command = cv.WaitKey(10)

    # if press 'q' -> exit program
    if command == ord('q'):
        print "Ending program"
        break  # end program
 
    # if press 'sw' -> save the image
    if(GPIO.input(sw) == 0):
    	print "Saving... "
    	time.sleep(0.3)
    	print "."
    	time.sleep(0.3)
    	print ".."
    	time.sleep(0.4)
    	print "..."
    	time.sleep(0.5)
    	cv.SaveImage(timeStampString + ".jpg", frame)
    	print ""
    	print "Save success!"
    	print "====================="
    	print ""
    	time.sleep(0.2)
