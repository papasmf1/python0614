# form2.py(로직을 구현) + form2.ui(화면을 만든 파일)
import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic 

#화면을 로딩(form2.ui)
form_class = uic.loadUiType("form2.ui")[0]

#화면 클래스 정의(QMainWindow)
class DemoForm(QMainWindow, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #슬롯메서드(시그널 처리)
    def firstClick(self):
        self.label.setText("첫번째 클릭")
    def secondClick(self):
        self.label.setText("두번째 클릭~~")
    def thirdClick(self):
        self.label.setText("세번째 클릭~~~~")


#진입점을 체크해서 직접 로딩한 경우면
if __name__ == "__main__":
    #실행 프로세스 만들기
    app = QApplication(sys.argv)
    #윈도우 실행
    demoWindow = DemoForm()
    #화면 보여주기
    demoWindow.show()
    app.exec_() 