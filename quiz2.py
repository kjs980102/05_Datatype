#다음과 같이 판매기가 저장된 리스트가 있을 때
#부가세가 포함된 가격을 for문을 사용해서 화면에 출력하라.
#단 부가세는 10%로 가정한다.
numbers=[100,200,300]
for num in numbers :
    b=(int(num+0.1*num))
    print(b)

