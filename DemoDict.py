# DemoDict.py 

d = dict(a=1, b=2, c=3)
print( d )
print( type(d) )

#초기화를 간단하게 
color = {"apple":"red", "banana":"yellow"}
#검색
print( color["apple"] )
print( len(color) )
#print( color[0] )
#입력
#중단점(Break Point)
color["kiwi"] = "green"
#반복구문
for item in color.items():
    print(item)

#삭제
del color["apple"]
print( color )

color.clear()
print( color )

#모바일 앱 팀(장비 관리)
device = {"아이폰":5, "아이패드":10, "윈도우":20}
print( device["아이폰"] )
#입력
device["맥프레"] = 15 
print( device )
#수정
device["아이폰"] = 6 
print( device )
#삭제
del device["아이폰"]
print( device )

for item in device.items():
    print(item)

for k,v in device.items():
    print(k, v)

#키만 리턴 
for k in device.keys():
    print(k)

#값만 리턴 
for v in device.values():
    print(v)
