# class2.py 
# 클래스 형식을 정의
class Person:
    #클래스의 멤버 변수(데이터 공유)
    num_person = 0 
    #인스턴스의 초기화를 담당
    def __init__(self):
        self.name = "default name"
        Person.num_person += 1 
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스 생성
p1 = Person()
p2 = Person()
p3 = Person() 
print("인스턴스 개수:{0}".format(Person.num_person) )


