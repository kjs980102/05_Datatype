#while문을 사용하여 1부터 100까지 수에 존재하는 모든 홀수의 합을 구하시오.
a=0
c=[]
while a<100:
    a=a+1
    if a%2==1:
        c.append(a)

d=sum(c)
print(d)

#no list,sum
#변수 두개로 해결, b에 연산 결과 값을 저장
a=0
b=0
while a<100:
    a=a+1
    if a%2==1:
        b=b+a

print(b)