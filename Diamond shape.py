#โปรเเกรมทำรูปข้าวหลามตัด
number = int(input())


for i in range(1,number + 1,1):
    print(end = " " * (number - i)) 
    print("*" * ((2 * i) - 1))
for i in range(number - 1,0,-1):
    print(end = " " * (number - i))
    print("*" * ((2 * i) - 1))
