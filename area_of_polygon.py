import math tan,pi
n_sides = int(input("input number of sides: "))
s_length = float(input("input the length of a side: "))
p_area = n_sides * (s_length **2) / (4 * tan(pi / n_sides))
print("the area of the polygon is : ",p_area)
