# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este archivo temporal se encuentra aquí:
/home/ahpukh/.spyder2/.temp.py
"""

def f(ecu,x):
    return eval(ecu)

def biseccion(xi, xf, es, imax,ecu):
    xr = xi
    i = 0
    ea = 100
    while ea >= es and i <= imax:
        xrold = xr
        xr = (xi + xf) / 2.0
        #print xr
        i = i + 1

        if xr != 0:
            ea = abs(((xr - xrold)/xr)*100)

        test = f(ecu,xi) * f(ecu,xr)

        if test < 0:
            xf = xr

        elif test > 0:
            xi = xr

        else:
            ea = 0
        print '{:3d} {:12.6} {:12.6} {:12.6} {:12.6}'.format(i,xi,xf,xr,ea)

    return xr

print "Introduzca la ecuación: "
ecu = str(raw_input())
print "Dar el valor de xi: "
xi = float(raw_input())
print "Dar el valor de xf: "
xf = float(raw_input())
print "Dar el valor de es: "
es = float(raw_input())
print "Dar el valor de maxit: "
imax =  input()

raiz = biseccion(xi, xf, es, imax,ecu)

print "La raiz es: ", raiz