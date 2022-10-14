#Cálculo simples

cod_item1, amount_item1, value_unit_item1 = (input().split(" "))

cod_item1 = int(cod_item1)
amount_item1 = int(amount_item1)
value_unit_item1 = float(value_unit_item1 )

cod_item2, amount_item2, value_unit_item2 = (input().split(" "))

cod_item2 = int(cod_item2)
amount_item2 = int(amount_item2)
value_unit_item2 = float(value_unit_item2)


TOTAL = ((amount_item1 * value_unit_item1) + (amount_item2 * value_unit_item2))

print("VALOR A PAGAR: R$ {:.2f}".format(TOTAL))