#KAPREKAR PROGRAM
num = input()
length = len(num)
num = int(num)
sq = num * num
z = 10
sum_ = 0
if length > 1:
    z = z ** length
    mod = sq % z
    n = num - mod
    if n > 0:
        sum_ = mod + n
        if sum_ == num:
            print("Kaprekar Number")
        else:
            print("Not a Kaprekar Number")
    else:
        print("Not a Kaprekar Number")
else:
    mod = sq % z
    n = num - mod
    sum_ = mod + n
    if sum_ == num:
        print("Kaprekar Number")
    else:
        print("Not a Kaprekar Number")