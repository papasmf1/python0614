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
