# DemoLoop.py 
lst = [1,2,3,4,5,6,7,8,9,10]

#반복구문을 탈출하는 경우(break)
for i in lst:
    #블럭으로 주석처리: ctrl + / 
    if i > 5:
        break 
    print("Item:{0}".format(i))

#지속적으로 실행하는 남은 블럭을 스킵(continue)
for i in lst:
    #블럭으로 주석처리: ctrl + / 
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))

#약방의 감초: 규칙이 있는 수열을 만드는 함수
print("---수열함수---")
print( list(range(10)) )
print( list(range(1,11)) )
print( list(range(2000, 2022)) )

#수동으로 5번 루프 돌기
print("---수동으로 루프돌기---")
for i in range(10):
    print(i)

