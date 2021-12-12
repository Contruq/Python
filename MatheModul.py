'''
Calculations
###AnyForm###
'''
def mult(x, y):
    return x * y

def div(x, y):
    return x / y

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def pi(x):
    return x * 3.141592653589793

'''Currently not in Use:
def radius(r, t):
    return r ** t
'''
def exp(x, y):
    return x ** y

def root(x):
    return x ** (0.5)

def disp(x):
    return x // exp(x,2)

def pythagoras(a, b, c, keyword):
    if keyword == "hypotenuse":
        return root(add(exp(a,2),exp(b,2)))
    if keyword == "cathetus":
        if a == 0:
            return root(sub(exp(c,2),exp(b,2)))
        if b == 0:
            return root(sub(exp(c,2),exp(a,2)))

'''
Americans:
'''

def celsius(f):
    return div(sub(f,32),1.8)

def fahrenheit(c):
    return add(mult(c,1.8),32)

'''
2D-Forms
'''
def dbg(a, b):
    return div(mult(a,b),2)

def circle(r, keyword):
    if keyword == "surface":
        return pi(exp(r,2))
    elif keyword == "perimeter":
        return pi(r*2)

def square(a, keyword):
    if keyword == "surface":
        return exp(a,2)
    elif keyword == "perimeter":
        return mult(a,4)

def rectangle(a, b, keyword):
    if keyword == "surface":
        return mult(a,b)
    elif keyword == "perimeter":
        return add(mult(a,2),mult(b,2))

def triangle(g, h, c, keyword):
    if keyword == "surface":
        return div(mult(g,h),2)
    elif keyword == "perimeter":
        return add(add(g,h),c)

def rhomboid(g, h, keyword):
    if keyword == "surface":
        return mult(g,h)
    elif keyword == "perimeter":
        return add(mult(g,2),(h,2))

def trapezoid(a, c, h, d, keyword):
    if keyword == "surface":
        return div(mult(add(a,c),h),2)
    elif keyword == "perimeter":
        return add(add(a,c),add(h,d))

def circledegr(ad):
    return ad / 360

def circular_sector(r, ad, keyword):
    if keyword == "surface":
        return mult(pi(exp(r,2)),circledegr(ad))
    elif keyword == "arc":
        return mult(pi(mult(r,2)),circledegr(ad))

def annulus(r1, r2):
    return sub(pi(exp(r1,2)),pi(exp(r2,2)))

'''
3D-Forms
'''
def Cube(a, keyword):
    if keyword == "volumina":
        return exp(a,3)
    elif keyword == "surface":
        return mult(6,exp(a,2))

def Cuboid(a, b, c, keyword):
    if keyword == "volumina":
        return mult(mult(a,b),c)
    elif keyword == "surface":
        return add(add(mult(mult(a,b),2),mult(mult(b,c),2)),mult(mult(c,a),2))

def triprism(g, h, hp, c, keyword):
    if keyword == "volumina":
        return mult(div(mult(g,h),2),hp)
    elif keyword == "shell":
        return mult(add(add(g,h),c),hp)
    elif keyword == "surface":
        return add(mult(div(mult(g,h),2),2),mult(add(add(g,h),c),hp))

def cylinder(r, h, keyword):
    if keyword == "volumina":
        return mult(pi(exp(r,2)),h)
    elif keyword == "shell":
        return mult(pi(mult(r,2)),h)
    elif keyword == "surface":
        return add(mult(2,pi(exp(r,2))),mult(pi(mult(r,2)),h))

def pyramid(a, b, h, s, keyword):
    if keyword == "volumina":
        if b == a:
            return div(mult(exp(a,2),h),3)
        else:
            return div(mult(mult(a,b),h),3)
    elif keyword == "shell":
        if b == a:
            return mult(mult(a,s),2)
        else:
            return add(mult(a,s),mult(b,s))
    elif keyword == "surface":
        if b == a:
            return add(exp(a,2),exp(div(mult(a,s),2),4))
        else:
            return add(mult(a,b),exp(div(mult(a,s),2),4))

def cone(r, h, s, keyword):
    if keyword == "volumina":
        return div(mult(pi(exp(r,2)),h),3)
    elif keyword == "shell":
        return pi(mult(r,s))
    elif keyword == "surface":
        return add(pi(exp(r,2)),pi(mult(r,s)))

def sphere(r, keyword):
    if keyword == "volumina":
        return div(mult(pi(exp(r,3)),4),3)
    elif keyword == "surface":
        return mult(pi(exp(r,2)),4)
