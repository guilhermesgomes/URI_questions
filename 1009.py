#Salário com bônus

name_wrkr = str(input())
salary = float(input())
value_sales = float(input())
TOTAL = (((15 / 100) * value_sales) + salary)

print("TOTAL = R$ {:.2f}".format(TOTAL))