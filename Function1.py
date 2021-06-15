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

#불변형식 
print("---불변형식---")
a = 1.2 
print( id(a) )
a = 2.3 
print( id(a) )

#가변형식
print("---가변형식---")
lst = [1,2,3]
print( id(lst) )
lst.append(4)
print( id(lst) )

#가변형식으로 입력 + 출력 
def change(x):
    #복사본을 만들어서 사용
    x1 = x[:]
    x1[0] = "H"
    print("함수내부:", x1)

#함수 호출
wordlist = ["J","A","M"]
change(wordlist)
print("함수호출후:", wordlist)

#함수 내부의 이름을 해석(스코핑룰): LGB(Local, Global, Built-in)
x = 5 
def func1(a):
    return a+x 

#호출
print( func1(1) )

def func2(a):
    x = 2 
    return a+x 

#호출
print( func2(1) )
