# DemoRandom.py 
import random

#임의의 실수 생성
print( random.random() )
print( random.random() )

print("---구간을 지정---")
print( random.uniform(2.0, 5.0) )
print( random.uniform(2.0, 5.0) )

#임의의 정수(리스트 컴프리헨션, 리스트 내장 방식)
print( [random.randrange(20) for i in range(10)] )
print( [random.randrange(20) for i in range(10)] )
#유일한 값을 출력
print("---유일한 값을 샘플링---")
print( random.sample(range(20), 10) )
print( random.sample(range(20), 10) )

#로또번호 생성
print("---로또번호생성---")
lotto = list(range(1,46))
print( lotto )
random.shuffle(lotto)
for item in range(5):
    print( lotto.pop() )


#파일 다루기 
print("---파일 다루기---")
from os.path import * 
print( abspath("demo.py") )
print( basename("c:/work/demo.txt") )
print( exists("c:/python38/python.exe") )
print( getsize("c:/python38/python.exe") )

