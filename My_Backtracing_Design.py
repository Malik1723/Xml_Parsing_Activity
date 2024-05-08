import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class My_Project_Window(QMainWindow):
    def __init__(self,parent = None):
        super(My_Project_Window,self).__init__(parent)
        self.initUi()




    def initUi(self):
        #self.setMinimumSize(800,600)
        #self.setMaximumSize(800,600)
        self.setWindowTitle("Backtracing Generator")
        self.setGeometry(0, 0, 800, 600)
        #self.Background_Label = QLabel(self)
        #self.Background_Label.setGeometry(0,0,800,600)
        #PixelMap = QPixmap("oui.jpg")
        #self.Background_Label.setPixmap(PixelMap)
        #self.Background_Label.setScaledContents(True)
        self.b1 = QPushButton()

        self.lbl = QLabel("ENter Tetxt Here")
        self.Load_Project_Button = QPushButton()
        self.Console_Project =QLineEdit()
        #form = QHBoxLayout()
        #form.addWidget(self.Load_Project_Button )
        #form.addStretch()
        #form.addWidget(self.Console_Project)
        #self.setLayout(form)
        #Layout = QHBoxLayout()
        #Layout.addWidget(self.Load_Project_Button)
        #Layout.addWidget(self.Console_Project)
        #Layout.addWidget(self.lbl)
        #self.setLayout(Layout)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = My_Project_Window()
    window.show()
    sys.exit(app.exec_())
