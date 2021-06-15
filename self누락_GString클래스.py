#전역변수 
str = "Not Class Member"
#클래스 정의
class GString:
    def __init__(self):
        #인스턴스 멤버 변수 
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #약간의 버그(멤버 변수)
        print(self.str)

g = GString()
g.set("First Message")
g.print()
