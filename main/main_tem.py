a = float(input("Enter the coefficient A: "))
b = float(input("Enter the coefficient B: "))
c = float(input("Enter the coefficient C: "))
d = float(input("Enter the coefficient D: "))
x = float(input("Enter a value for x: "))
func  = (a*x**3 + b*x**2 + c*x + d)

a = 2
b = 3
c = -11
d = -6
x = -2
h = 0.1

#part a
ans = (a*x**3 + b*x**2 + c*x + d)
print("f(%1.1f) is %2.1f" % (x, ans)) # evaluate function at x value

#part b, evaluate the derivative of the function analytically


#part c, evaluate the derivative of the function numerically
def func(val):
    return a*val**3 + b*val**2 + c*val + d

h = 0.1
funcPlusH = (a*(x+h)**3 + b*(x+h)**2 + c*(x+h) + d)
tol = 10**-6

dif = func(x+h) - func(x)
while dif/h > tol:
    h = h/2
    dif = func(x + h) - func(x)
    print ("dif", dif, " h: ", h)

print("f(%1.1f) analytically is %1.6f" % (x, dif/h))
