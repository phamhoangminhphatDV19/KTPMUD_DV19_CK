def kiemtra_SNT(n):
    flag = True
 
    # Kiểm tra SNT
    if (n < 2):
        flag = False
    elif (n == 2):
        flag = True
    elif (n % 2 == 0):
        flag = False
    else:
        # Lặp qua các số lẻ nên bắt đầu từ 3 với bước nhảy là 2
        for i in range(3, n, 2):
            if (n % i == 0):
                flag = False
 
    return flag
 
# Chương trình chính
tong = 0
 
for i in range(0, 4):
    if (kiemtra_SNT(i)):
        print(i)
        tong += i
 
print("=> Tính tổng các SN là: ", tong)