customer = ["sadikturan","ahmetyilmaz","cinarturan","yigitbilgi"]
order_totals=[12000,13000,5000,15000]

#sadikturan kullanıcısnın 5000 liralık siparişini listeye ekleyiniz.

yeniKayıt= customer.append("sadikturan")
siparişlerYeniKayıt=order_totals.append(5000)

print(f"{customer[4]} adlı kullanıcı "  +str(order_totals[4])+ " miktarında yeni alışveriş yaptı")

# #son eklenen siparişi silme
#
# customer.pop()
# print(customer)
#
# order_totals.pop()
# print(order_totals)

print(f"{customer[0]} isimli müşterinin sipariş toplamı: {order_totals[0]+order_totals[4]}")
print(f"{customer[1]} isimli müşterinin sipariş toplamı: {order_totals[1]}")
print(f"{customer[2]} isimli müşterinin sipariş toplamı: {order_totals[2]}")
print(f"{customer[3]} isimli müşterinin sipariş toplamı: {order_totals[3]}")