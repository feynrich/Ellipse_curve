import math

F_len = int(input("Input group order: "))
F = []

a = int(input("Input coefficient a: "))
b = int(input("Input coefficient b: "))

extra_sqr = {}

for i in range (-(F_len-1)//2, ((F_len-1)//2)+1):
    if i >= 0:
        extra_sqr[((i**2)%F_len)] = i
    F.append(i)

size_F_group = len(F)

while (-4*a**3 - 27*b**2)%F_len == 0:
    print("Dude, try other coefficients: ")

    a = int(input("Input coefficient a: "))
    b = int(input("Input coefficient b: "))

def int_x3_y3(chisl1, point):
    chisl2 = chisl1
    while (chisl1/(2*point[1])**2)%1 != 0:
        chisl1 += F_len
        chisl2 -= F_len
        if (chisl2/(2*point[1])**2)%1 == 0:
            return chisl2/(2*point[1])
        return chisl1/(2*point[1])

def int2_x3_y3(chisl1, point1, point2):
    chisl2 = chisl1
    if chisl1 == 0:
        return chisl1/(point2[0] - point1[0])

    while (chisl1/(point2[0] - point1[0]))%1 != 0:
        chisl1 += F_len
        chisl2 -= F_len
        if str(chisl2/(point2[0] - point1[0])).isnumeric():
            return chisl2/(point2[0] - point1[0])
    return chisl1/(point2[0] - point1[0])

def gen_points(a, b, F_len):

    points = [0]

    for j in F:
        y = (j**3 + a*j + b)%F_len

        if int(y) in extra_sqr:
            if y != 0:
                points.append([j, -extra_sqr[int(y)]])
            points.append([j, int(extra_sqr[int(y)])])
    print("Points of your elliptic curve: ", points)
    return points

def sum_same(point, a, points):
    chisl = ((3*(point[0]**2) + a))
        
    if point[1] != 0:
       x_3 = int(int_x3_y3(chisl, point)**2 - 2*point[0])%F_len
       y_3 = int(int_x3_y3(chisl, point)*(point[0] - x_3) - point[1])%F_len
    else:
       x_3 = point[0]
       y_3 = point[1]
    
    y_31 = y_3
    x_31 = x_3
    while y_3 not in F:
        y_31 += F_len
        y_3 -= F_len
        if y_31 in F:
            y_3 = y_31

    while x_3 not in F:
        x_31 += F_len
        x_3 -= F_len
        if x_31 in F:
            x_3 = x_31  

    return [x_3, y_3]

def sum_diff(point2, point1, points):
    chisl = (point2[1] - point1[1])
    if point2[0] - point1[0] != 0:
       x_3 = int(int2_x3_y3(chisl, point1, point2)**2 - point1[0] - point2[0])%F_len
       y_3 = int(int2_x3_y3(chisl, point1, point2)*(point1[0] - x_3) - point1[1])%F_len
    else:
       x_3 = point2[0]
       y_3 = point2[1]

    y_31 = y_3
    x_31 = x_3
    while y_3 not in F:
        y_31 += F_len
        y_3 -= F_len
        if y_31 in F:
            y_3 = y_31

    while x_3 not in F:
        x_31 += F_len
        x_3 -= F_len
        if x_31 in F:
            x_3 = x_31  

    return [(x_3), (y_3)]

def sum_all_points(a, points):
    for i in range(9, len(points)):
        P = sum_same(points[i], a, points)
        P_last = 0
        count = 1
        num_el = [0, points[i], P]
        while P_last != P:
            P_last = P
            P = sum_diff(P, points[i], points)
            count += 1
            num_el.append(P)
        if count == len(points) - 1:
            num_el.pop()
            return num_el
        num_el = []
        


def num_el_group(num_el, points):
    num_el2 = []
    for i in range(1, len(points)):
        num_el2.append([num_el[i], ((len(points) * i) // math.gcd(len(points), i))/i])

    print("Order of elements of a group of points: ", num_el2)

def user(a, b, F_len):
    points = gen_points(a, b, F_len)
    num_el = sum_all_points(a, points)

    return num_el_group(num_el, points)

print(user(a, b, F_len))
