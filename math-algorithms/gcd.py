#!/bin/python

import sys

option = False
option_2 = False
is_swapped = False

def swap(a, b):
    return b, a

def gcd(a, b, reminders, quotients):
    # if(b > a):
    #     a, b = swap(a, b)
    
    if(b == 0):
        return a

    q = a // b
    r = a - (q * b)
    reminders.append(r)
    quotients.append(q)

    if(option):
        print(f'{a} = {q}({b}) + {r}')
    
    if(r != 0):
        a = b
        b = r
        return gcd(a, b, reminders, quotients)
    else:
        return b, reminders, quotients

def extended_gcd(r, q, s1, s2, t1, t2, start):
    s3 = s1 - (q[start] * s2)
    t3 = t1 - (q[start] * t2)

    if(option and r[start] > 0):
        print(f'{s1} - ({q[start]} * {s2}) = {s3}', end="")
        print(f'     |     {t1} - ({q[start]} * {t2}) = {t3}')
    s1 = s2
    s2 = s3
    t1 = t2
    t2 = t3


    if(r[start] != 0):
        start = start + 1
        return extended_gcd(r, q, s1, s2, t1, t2, start)
    else:
        if(is_swapped):
            return t1, s1
        else:
            return s1, t1

def diophantine_equation(a, b, gcd, x0, y0, diophantine_num):
    if(diophantine_num % gcd != 0):
        return f'Since this gcd = {gcd} does not devide {diophantine_num} --> There are no solutions'
    else:
        print(f'Particular Solution: {a}({x0}) + {b}({y0}) = {diophantine_num}')
        print("x = x0 + k(b/d)")
        print("y = y0 - k(a/d)")
        return f'x = {x0} + {b//gcd}k    |   y = {y0} - {a//gcd}k'
        

if "__main__" == __name__:
    if(len(sys.argv) < 3 or len(sys.argv) > 6):
        print("Usage: 2 arguments minimun, a and b.")
        print("Type -e or --equations to see all equations")
        print("Type -d or --diophantine to find the diophantine")
        print("Example ./gcd.py 191 91-e -d 812")
        exit(-1)

    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[2])
    temp = 3
    if(arg2 > arg1):
        is_swapped = True
        arg1, arg2 = swap(arg1, arg2)

    if("-e" in sys.argv or "--equations" in sys.argv):
        option = True
        temp += 1

    if("-d" in sys.argv or "--diophantine" in sys.argv):
        option_2 = True
        aux = sys.argv[temp]
        diophantine_idx = sys.argv.index(aux) + 1
        diophantine_num = int(sys.argv[diophantine_idx])

    reminders = []
    quotients = []
    mygcd, reminders, quotients = gcd(arg1, arg2, reminders, quotients)
    print("---------------------------------------------------------------------")
    print(f'gcc({arg1}, {arg2}) = {mygcd}')
    if(mygcd == 1): print(f'{arg1} and {arg2} are relatively prime')
    print("---------------------------------------------------------------------")
    x, y = extended_gcd(reminders, quotients, 1, 0, 0, 1, 0)
    if(is_swapped): arg1, arg2 = swap(arg1, arg2)
    print("---------------------------------------------------------------------")
    print(f'gcc({arg1}, {arg2}) = {arg1}({x}) + {arg2}({y}) -> x = {x}, y = {y}')
    print("---------------------------------------------------------------------")
    if(option_2 == True):
        solution = diophantine_equation(arg1, arg2, mygcd, x, y, diophantine_num)
        print(solution)

