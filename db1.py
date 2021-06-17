# db1.py 
import sqlite3

#커넥션객체 생성(임시로 메모리에 저장)
con = sqlite3.connect(":memory:")

#구문을 실행할 커서 객체 
cur = con.cursor()
#데이터를 저장할 테이블 생성(자료구조)
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook values ('derick', '010-111');")

#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

