# DemoRE.py 
#특정한 패턴이 있는 문자열을 검색(정규 표현식)
import re 

print( re.search("[0-9]*th", "35th") )
print( re.match("[0-9]*th", "35th") )

print( bool(re.search("[0-9]*th", "  35th")) )
print( bool(re.match("[0-9]*th", "  35th")) )

#apple이란 단어
print("---apple단어---")
print( bool(re.search("apple", "this is apple")) )
print( bool(re.match("apple", "this is apple")) )

#우편번호, 년도
print("---우편번호---")
print( bool(re.search("\d{4}", "올해는 2021년")) )
print( bool(re.search("\d{5}", "우리동네는 52300")) )


