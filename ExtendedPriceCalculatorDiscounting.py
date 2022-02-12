# This is code for an online cart
item = input("Enter an item description: ")
unit_price = input("Enter the unit price: ")
quantity = input("Enter the quantity: ")
extended_price = float(unit_price) * float(quantity)

if int(quantity) >= 5 and int(quantity) < 25:
    discount = 0.1
elif int(quantity) >= 25:
    discount = 0.2
else:
    discount = 0.0

final_price = extended_price - extended_price * discount

print(item + ":")
print("\tUnit Price:\t\t" + "$" + format(float(unit_price), "8.2f"))
print("\tQuantity:\t\t" + format(int(quantity), "9"))
print("\tExtended Price:\t\t" + "$" + format(float(unit_price) * int(quantity), "8.2f"))
# Seven whitespaces because %\t\t\b-$ is the same as %\t-$
print("\tDiscount: " + str(discount*100) + "%\t       -$" + format(float(extended_price) * float(discount), "8.2f"))
print("\tFinal Price:\t\t" + "$" + format(float(final_price), "8.2f"))