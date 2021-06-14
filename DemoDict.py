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


