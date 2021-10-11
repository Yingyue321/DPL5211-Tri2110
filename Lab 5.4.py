# Student ID : 1201201400
# Student Name : Tan Ying Yue

width = int(input("Enter width: "))
length = int(input("Enter length: "))

def rectangle(width,length):
    area = width*length
    return area

def triangle(width,length):
    area = width*length/2
    return area

area_rec = rectangle(width,length)
area_tri = triangle(width,length)

print("Rectangle area: {:.2f}".format(area_rec))
print("Triangle area: {:.2f}".format(area_tri))