#다음 리스트 변수의 평균 값을 구하여라. 평균값을 구할 때는 for 반복문을 사용하여라
my_list=[100,200,400,800,1000,1300]
result=0
for i in my_list:
    result = result+i

ave=result/len(my_list)
print(int(ave))
