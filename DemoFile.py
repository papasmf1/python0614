# DemoFile.py 
url = "http://www.credu.com/?page=" + str(1) 
print(url)

#숫자를 출력
for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---오른쪽정렬---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3) )

print("---0으로 채우기---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).zfill(3) )


#서식문자 사용 
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(150000000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))

#파일처리(한글이 깨지는 경우는 인코딩방식 지정)
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
#내용을 쓰고 줄바꿈 
f.write("첫번째\n두번째\n1234\n")
f.close()

#파일 읽기
f = open("c:/work/demo.txt", "rt", encoding="utf-8")
#한번에 문자열 변수로 읽어오기 
result = f.read() 
print(result)

print( f.tell() )
#다시 처음으로 돌아오기(첫줄)
f.seek(0)
#한줄씩 읽기 
print( f.readline(), end="" )
print( f.readline(), end="" )
f.seek(0)
#리스트 형식으로 읽어오기 
lst = f.readlines()
print( lst )
f.close() 

#기존 파일에 첨부를 하는 경우
f = open("c:/work/demo.txt", "wt", encoding="utf-8")
f.write("새로운 데이터\n")
f.close() 
