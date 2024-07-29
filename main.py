'1st program'
print(9**0.5*5)
'2nd program'
print(9.99>9.98 and 1000 != 1000.1)
'3rd program'
print(1234//10%100+5678//10%100)
'4th program'
a = 13.42
b = 42.13
int_a, frac_a = divmod(a, 1)
int_b, frac_b = divmod(b, 1)
int_a = int(int_a)
int_b = int(int_b)
frac_a = int(round(frac_a * 100))
frac_b = int(round(frac_b * 100))
print(int_a == frac_b and int_b == frac_a)
print(int_a == frac_b or int_b == frac_a)
#divmod=//, %
#round= округление числа(-цифры после запятой)
#int= для изменения с str в целочисленный вид(ну в int, очевидно впринципе)
#ещё int=целая часть числа frac= дробная 
# через обычные вычислительные команды были какие то траблы с цифрами(вместо 42=41.9999999993 вместо 0,13= 0,13000000000000256)
