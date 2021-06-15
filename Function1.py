# Function1.py 
#함수를 정의
def setValue(newValue):
    x = newValue
    print(x)

#함수를 호출
result = setValue(5)
print(result)

#함수 정의
def swap(x,y):
    return y,x 

#호출
result = swap(3,4)
print(result)

#교집합 문자를 리턴하는 함수
def intersect(prelist, postlist):
    #지역변수에 교집합 문자를 모아두기(저장)
    retList = []
    # H(0) | A(1) | M(2) 
    for x in prelist:
        if x in postlist and x not in retList:
            retList.append(x)
    return retList 

#함수 호출
#중단점(Break Point)
print( intersect("HAM", "SPAM") )
