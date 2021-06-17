# web1.py
#from 패키지명 import 모듈명 
from bs4 import BeautifulSoup

#페이지 로딩(메서드 체인)
page = open("c:/work/test01.html", encoding="utf-8").read()
#검색이 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")
#보여달라~~
print( soup.prettify() )

