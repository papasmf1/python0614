# DemoDict2.py 
phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print( len(phone) )
print( phone["lee"] )
print( "park" in phone )
print( "moon" not in phone )

#참조를 복사 
p = phone
p["kang"] = "1234"
print( id(phone) )
print( id(p) )
print(phone)
print(p)

#논리 표현식 연습(bool: True, False)
print("---논리식---")
print( 1 < 2 )
print( 1 != 2 )
print( 1 == 2 )

#and는 ~이면서, ~이고 
print( True and True and True )
print( True and True and False )
#or는 ~이거나 
print( True or False or False)

#파이썬은 참과 거짓은 판단하는 근거가 단순
#숫자는 0이 아니면, 문자열은 ""이 아니면, 객체는 None이 아니면 
print("----숫자,문자열,객체----")
print( bool(0) )
print( bool(1) )
print( bool("") )
print( bool("test") )
print( bool(None) )
print( bool([1,2,3]) )

#네이밍룰(이름규칙): 일관성있게 코딩 
#변수명, 메서드명: strCustomer (여러개의 단어를 붙일때 첫단어는 전부 소문자)
#(카멜표기법)      getCustomer(), setCustomer() 
#클래스명(형식 이름): DemoCustomer(각 단어의 첫글자를 대문자로 사용)
#(파스칼표기법)

#얕은 복사
a = [1,2,3]
b = a 
a[0] = 38
print(a)
print(b)
print( id(a), id(b) )

#깊은 복사
a = [1,2,3]
b = a[:] 
a[0] = 38
print(a)
print(b)
print( id(a), id(b) )

#리스트가 아닌 형식이면?
import copy 
a = [100,200,300]
b = copy.deepcopy(a)
a[0] = 101
print(a)
print(b)
print(id(a), id(b) )
