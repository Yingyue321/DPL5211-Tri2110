# Student ID : 1201201400
# Student Name : Tan Ying Yue

# In main():
# Display the menu.
# Ask the user to enter their choice [1 or 2].
# Using a switch-case statement:
# If choice is 1 call function get_cm().
# If choice is 2 call function get_meter().
# Else print “Invalid choice”

#   In get_cm():
#   Get the value of centimetre from the user.
#	Call function cm_to_meter(…) and pass centimeter to calculate meter.
#	Display the centimeter and meter.


def cm_to_meter(centimeter):
    meter = centimeter / 100
    return meter

def get_cm():
    cm = float(input("Please enter a value for centimeter: "))
    m = cm_to_meter(cm)
    print(" {:.2f} centimeters is {:.2f} meters ".format(cm,m))

def get_meter(m):
    cm = meter_to_cm(m)
    print("{:.2f} meters is equals to {:.2f} centimeters".format(m,cm))

def meter_to_cm(meter):
    centimeter = meter * 100
    return centimeter

print("======================================")
print("\t\t  MENU ")
print("1.    Convert centimeter to meter")
print("2.    Convert meter to centimeter")
print("======================================")

choice = int(input("Enter your choice : "))
if choice == 1:
    get_cm()
elif choice == 2:
    get_meter()
else:
    print("Invalid Choice")