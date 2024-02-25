import cv2
import time 

def minimizeWindow():
    import win32gui,win32con
    window = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(window,win32con.SW_MINIMIZE)



def cctv():
    video = cv2.VideoCapture(0)
    video.set(3,640)
    video.set(4,480)
    width = video.get(3)
    height = video.get(4)
    print("Video resolation is set to",width,"x",height)
    print("Help-- \n1 . Press esc key to exit. \n2. Prees m to minimize ")
    fourcc = cv2.videoWriter_fourcc(*"XVID")
    date_time = time.strftime("recording %H-%M-%d -%m -%y")
    output = cv2.Videowriter("footages/"+date_time+".mp4")
    while video.isOpened():
        if check == True:
            frame = cv2.flip(frame,1)
            t = time.ctime()
            cv2.rectangle(frame,(5,5,100,20),(255,255,255,cv2.FILLED))
            cv2.putText(frame,"camera 1",(20,20),cv2.FONT_HERSHEY_DUPLEX,0.5,(5,5,5),1)
            if cv2.waitkey(1) == 27:
                print("Video footage saved in ")
                print("Video footage saved in current directory") 
                break
            elif cv2.waitkey(1) == ord("m"):
                minimizeWindow()

            else:
                print("canot open camera,check configuration")
                break
            

