import random
result = random.randint(1, 45)
#while문을 사용하여 1부터 45까지의 랜덤한 수 6개를 생성하고
#이를 result 리스트 변수에 추가하는 코드를 작성하라.



result=[]
i=0
while i<6:
    i=i+1
    result.append(random.randint(1, 45))

print(result)