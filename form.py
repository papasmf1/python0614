# form.py(로직을 구현) + form.ui(화면을 만든 파일)
import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic 

#화면을 로딩
form_class = uic.loadUiType("form.ui")[0]

#화면 클래스 정의
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 Qt데모")

#진입점을 체크해서 직접 로딩한 경우면
if __name__ == "__main__":
    #실행 프로세스 만들기
    app = QApplication(sys.argv)
    #윈도우 실행
    demoWindow = DemoForm()
    #화면 보여주기
    demoWindow.show()
    app.exec_() 