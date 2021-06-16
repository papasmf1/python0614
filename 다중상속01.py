#오픈소스를 받아서 사용중 
class Tiger:
    def jump(self):
        print("호랑이 점프")
    def cry(self):
        print("호랑이 어흥~~")

class Lion:
    def bite(self):
        print("사자 물어뜯기")
    def cry(self):
        print("사자 으르릉~~")

#다중상속을 받은 경우 
class Liger(Lion, Tiger):
    def play(self):
        print("라이거와 놀기")


l = Liger()
l.cry()
print("상속받은 순서(MRO):", Liger.__mro__)


        
