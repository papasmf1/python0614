# Function2.py 
#기본값이 있는 함수 
def times(a=10, b=20):
    return a*b 

#호출
print( times() )
print( times(5) )
print( times(5,6) )

#키워드인자(매개변수명을 지정)
def connectURI(server, port):
    str = "http://" + server + ":" + port 
    return str 

#호출
print( connectURI("credu.com", "80") )
print( connectURI(port="80", server="credu.com") )

#가변 인자를 처리하는 함수
def union(*ar):
    #지역변수로 리스트 초기화
    result = []
    #HAM(0) | EGG(1)
    for item in ar:
        # H(0) | A(1) | M(2)
        for x in item:
            if x not in result:
                result.append(x)
    return result 

#함수 호출
print( union("HAM","EGG") )
print( union("HAM","EGG","SPAM") )

#정의되지 않은 인자 
def userURIBuilder(server, port, **user):
    str = "http:" + server + ":" + port + "/?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str 

#호출
print( userURIBuilder("credu.com", "80", id="kim", password="1234") )
print( userURIBuilder("credu.com", "80", id="kim", password="1234", 
    name="mike", age="30") )

#람다함수 정의(간단하게 함수를 정의하는 문법)
g = lambda x,y:x*y 
print( g(3,4) )
print( g(5,6) )
#임시로 사용(즉흥적으로)
print( (lambda x:x*x)(3) )

print( globals() )

