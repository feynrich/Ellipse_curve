from symbol import classdef
from django.urls import clear_script_prefix
import numpy as np
import math

F_len = int(input())
F = []

a = int(input())
b = int(input())

while np.mod((-4*a**3 - 27*b**2), F_len) == 0:
    print("Чееел")

    a = int(input())
    b = int(input())

def int_x3_y3(chisl1, point):
    chisl2 = chisl1
    while not str(chisl1/(2*point[1])**2).isnumeric():
        chisl1 += F_len
        chisl2 -= F_len
        if str(chisl2/(2*point[1])**2).isnumeric():
            return chisl2/(2*point[1])
        return chisl1/(2*point[1])

def int2_x3_y3(chisl1, point1, point2):
    chisl2 = chisl1
    if chisl1 == 0:
        return chisl1/(point2[0] - point1[0])
    while not str(chisl1/(point2[0] - point1[0])).isnumeric():
        chisl1 += F_len
        chisl2 -= F_len
        if str(chisl2/(point2[0] - point1[0])).isnumeric():
            return chisl2/(point2[0] - point1[0])
    return chisl1/(point2[0] - point1[0])

def gen_points(a, b, F_len):

    extra_sqr = {}

    for i in range (-(F_len-1)//2, ((F_len-1)//2)+1):
        if i >= 0:
            extra_sqr[((i**2)%F_len)] = i
        F.append(i)

    points = [0]

    for j in F:
        y = np.mod(j**3 + a*j + b, F_len)

        if int(y) in extra_sqr:
            points.append([j, -extra_sqr[int(y)]])
            points.append([j, int(extra_sqr[int(y)])])
    
    return points

def sum_same(point, a, points):
    #x_3 = ((3*(point[0]**2) + a)/(2*point[1]))**2 - 2*point[0]
    chisl = ((3*(point[0]**2) + a))
    print(int_x3_y3(chisl, point))
        
    x_3 = int((int_x3_y3(chisl, point)**2 - 2*point[0])%F_len)
    y_3 = int((int_x3_y3(chisl, point)*(point[0] - x_3) - point[1])%F_len)
    print(y_3)
    if [x_3, y_3] not in points:
        y_3 -= F_len
    return [x_3, y_3]

def sum_diff(point2, point1, points):
    chisl = (point2[1] - point1[1])
    print(chisl)
    x_3 = int2_x3_y3(chisl, point1, point2)**2 - point1[0] - point2[0]
    y_3 = int2_x3_y3(chisl, point1, point2)*(point1[0] - x_3) - point1[1]

    if [x_3, y_3] not in points:
        y_3 -= F_len

    return [x_3, y_3]
print(sum_diff([3, -1], [-3, -1], gen_points(a, b, F_len)))
#def analys_group(points):

def sum_all_points(point, a):
    P = sum_same(point, a, gen_points(a, b, F_len))
    count = 0
    while P != [0, 0]:
        P = sum_diff(P, point, gen_points(a, b, F_len))
        print(P)
        count += 1
    return count

print(sum_all_points([-3, 1], a))
