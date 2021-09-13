# Student ID 1201201400
# Student Name: Tan Ying Yue

priceofbananas = 1.50
priceofgrapes = 5.60

print("Invoice for Fruits Purchase")
print("---------------------------------")

qofbananas = float(input("\nEnter the quantity (comb) of bananas bought: "))

qofgrapes = float(input("Enter the amount (kg) of grapes bought: "))

total_price_bananas = float(qofbananas * priceofbananas)
total_price_grapes = float(qofgrapes * priceofgrapes)

print("\nItem \t \t \t Qty \t Price \t \t Total")
print("Banana(combs) \t \t {:.0f} \t RM1.50 \t RM{:.2f}".format(qofbananas,total_price_bananas))
print("Grapes(kg) \t \t {:.0f} \t RM5.60 \t RM{:.2f}".format(qofgrapes,total_price_grapes))

Total = total_price_grapes + total_price_bananas
print ("\nTotal: RM {:.2f}".format(Total))
