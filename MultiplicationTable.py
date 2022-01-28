number = int(input("請問您是要幾乘幾的表呢?"))

for i in range(1, number+1):
    for j in range(1, number+1):
        print("%d x %d = %d" %  (i ,j , i*j ))
