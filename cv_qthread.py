from json import load
from operator import imod
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QApplication
import qdarkstyle
# import breeze_resources
import uuid


class MainWindow(QTabWidget):
    def __init__(self):
        
        super(MainWindow, self).__init__()

        self.VBL = QVBoxLayout()

        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)
        self.startv = QPushButton("Start")
        self.startv.clicked.connect(self.st)
        self.VBL.addWidget(self.startv)

        self.CancelBTN = QPushButton("Cancel")
        self.CancelBTN.clicked.connect(self.cancelf)
        self.VBL.addWidget(self.CancelBTN)

        self.w=worker()
     

        
     
       
        self.w.Imageupdate.connect(self.Isolot)

        self.setLayout(self.VBL)

    def Isolot(self,Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))
    def st(self):
        self.w.start()
        # App.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
    def cancelf(self):
        self.w.sr()
        print('----------------------------')
        # a = 10
        # b = 20
        # c = a + b
        # print(c)
        # exit()
    
class worker(QThread):
    Imageupdate = pyqtSignal(QImage)

    def run(self):
        self.threadActive = False
       
        cap = cv2.VideoCapture('/home/ronit/Downloads/SampleVideo_1280x720_5mb.mp4')
        while True:
            ret,frame = cap.read()
            if ret:
                Image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                fi = cv2.flip(Image,1)
                con = QImage(fi.data,fi.shape[1],fi.shape[0],QImage.Format_RGB888)
                pic = con.scaled(1240,880,Qt.KeepAspectRatio)
                self.Imageupdate.emit(pic)
            # return frame
            
            
         

    
    def sr(self):

        self.c = 10 + 20
        print('sucessfully working')
    
       
        # cv2.imwrite("frame"+str(uuid.uuid4())+".jpg",self.run())
        return self.c
     

    # x = sr()

              

    def stop(self):
        self.threadActive = False
        # self.quit()
        print('-----------------')
        return 0
        exit()
   
      
      
# if __name__ == "__main__":
