def f(n):
    if n in dic : return dic[n]
    cur_cal = min(f(n//2)+n%2, f(n//3)+n%3) + 1
    dic[n] = cur_cal
    return cur_cal

dic = {1:0, 2:1, 3:1}
print(f(int(input())))