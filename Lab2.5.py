# Student ID 1201201400
# Student Name: Tan Ying Yue

PRICE = 0.15

print("Natural Mineral Water Dispenser")
print("---------------------------------")

amountoflitres = float(input("\nEnter amount of litres: "))

print("\nPrice per litre   = RM {:.2f} ".format(PRICE))
print("Number of litres  = {:.0f}".format(amountoflitres))

Total = PRICE * amountoflitres
print ("\nTotal: RM {:.2f}".format(Total))