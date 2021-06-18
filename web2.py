# web2.py 
#웹서버와 통신
import urllib.request
#뷰티플스프 
from bs4 import BeautifulSoup



#웹서버에 페이지 실행을 요청
data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
#검색이 용이한 객체
soup = BeautifulSoup(data, "html.parser")

#블럭을 선택하고 ctrl + / 
# <td class="title">
#    <a href="/webtoon/detail.nhn?">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>
cartoons = soup.find_all("td", class_="title")
#슬라이싱(0번)
title = cartoons[0].find("a").text 
link = cartoons[0].find("a")["href"]
print(title)
print(link)
print("건수:{0}".format(len(cartoons)) )

#반복구문 
f = open("c:/work/webtoon.txt", "wt", encoding="utf-8")
for item in cartoons:
    title = item.find("a")
    print(title.text.strip()) 
    f.write(title.text.strip() + "\n")

f.close() 

