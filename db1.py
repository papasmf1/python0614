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
#입력 파라메터로 처리 
name = "gildong"
phoneNumber = "010-123"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))
#여러건을 입력
datalist = (("dsp","010-333"), ("tom","010-567"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

