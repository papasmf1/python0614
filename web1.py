# web1.py
#from 패키지명 import 모듈명 
from bs4 import BeautifulSoup

#페이지 로딩(메서드 체인)
page = open("c:/work/test01.html", encoding="utf-8").read()
#검색이 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")
#보여달라~~
#print( soup.prettify() )

#<p>태그를 전부 가져와~~ (리턴형 리스트)
#print( soup.find_all("p") )

#<p>하나를 가져와
#print( soup.find("p") )

#<p class="outer-text"> 조건이 있는 경우
#print( soup.find_all("p", class_="outer-text") )

#태그 안쪽에 컨텐츠를 출력
for tag in soup.find_all("p"):
    #컨텐츠만 출력
    print( tag.text.replace("\n", "").strip() )

