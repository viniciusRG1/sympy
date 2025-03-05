import sympy as sp

x = sp.symbols('x')

x*x

sp.init_printing()

Lista_simbolos = ['y','x']

y,x = sp.symbols(Lista_simbolos)

f_x_y = x**2 + y**2 + x*y
f_x_y

resposta = f_x_y.subs(x,1).subs(y,2)
resposta

f_xy = (x+y)**2 + y**2 + 2*x*y + y**2
sp.simplify(f_xy)