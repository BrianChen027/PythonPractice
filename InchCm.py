# 英吋公分轉換, 輸入數字再輸入單位OK了
while True:
    value = float(input("請輸入長度"))
    unit = input("請輸入單位")

    if unit == ('inch' or 'in'):
        print("%f in = %f cm" % (value, value * 2.54))
    elif unit == 'cm':
        print("%f cm = %f in" % (value, value / 2.54))
    else:
        print("清輸入cm或是inch")

    switch = input("還要繼續使用嗎? (y/n)")
    if switch == ('y' or 'yes'):
        continue
    elif switch == ('n' or 'no'):
        print("謝謝使用本單位轉換器")
        break
    else:
        print("看不太懂您的回答, 那就先結束囉")
        break