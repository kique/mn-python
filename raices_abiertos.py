def f(x):
    return 3*x**2 - 2*x - 100

def biseccion(xi, xf, es, imax):
    xr = xi
    iter = 0
    ea = 100
    while ea >= es and iter <= imax:
        xrold = xr
        xr = (xi + xf) / 2.0
        #print xr
        iter = iter + 1

        if xr != 0:
            ea = abs(((xr - xrold)/xr)*100)

        test = f(xi) * f(xr)

        if test < 0:
            xf = xr

        elif test > 0:
            xi = xr

        else:
            ea = 0

    return xr

print "Dar el valor de xi: "
xi = float(raw_input())
print "Dar el valor de xf: "
xf = float(raw_input())
print "Dar el valor de es: "
es = float(raw_input())
print "Dar el valor de maxit: "
imax =  input()

print "La raiz es: ", biseccion(xi, xf, es, imax)



