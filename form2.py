# form2.py(로직을 구현) + form2.ui(화면을 만든 파일)
import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic 
#웹서버와 통신
import urllib.request
#뷰티플스프 
from bs4 import BeautifulSoup



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
        data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
        soup = BeautifulSoup(data, "html.parser")
        cartoons = soup.find_all("td", class_="title")
        #기존에 파일이 있으면 뒤쪽에 첨부 
        f = open("c:/work/webtoon.txt", "a+", encoding="utf-8")
        for item in cartoons:
            title = item.find("a")
            print(title.text.strip()) 
            f.write(title.text.strip() + "\n")
        f.close() 
        self.label.setText("웹툰 리스트 저장 완료!")
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