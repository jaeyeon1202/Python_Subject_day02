print("1+3+5+7+9 =", 1+3+5+7+9)

#1~100
for i in range(1,101):
    print(i,end="")
print("")

#1~100 홀수만
for i in range(1,101):
    if i % 2 == 1:
        print(i,end="")
print("")

#1~100 합
s=0
for i in range(1,101):
    s=s+i #누적합 
print("합",s)

#1~100 홀수합
s=0
for i in range(1,101):
    if i % 2 == 1:
        s=s+i
print("홀수합",s)

#1~100 짝수합
s=0
for i in range(1,101):
    if i % 2 == 0:
        s=s+i
print("짝수합",s)
