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

sp.init_printing()
a = sp.Matrix([[1,2,3],[4,5,6]])
a.shape

B = sp.Matrix([[1,2,3]]).T
B
C = sp.Matrix([[1],[2],[3]])
C

I = sp.zeros(3)
N = sp.ones(3)
P = sp.eye(3)
I
N
P

Lista_E = [7,8,9]
E = sp.diag(Lista_E,unpack=True)
I*E

(I)**(-1)

E.det()

sp.cos(0)

sp.pi

x,y = sp.symbols(['x','y'])
f_x = sp.sin(x)

dfdx = sp.diff(f_x,x)
dfdx2 = sp.diff(f_x,x,x)
dfdx2

f_x_y = x**2 + y**2 - 100
dfdy = sp.diff(f_x_y,y)
dfdy

f_x2 = sp.sin(x)**2

int_f_x2 = sp.integrate(f_x2,x)
int_f_x2

C1 = sp.symbols('C1')
f_x2 = sp.sin(x)**2
int_f_x2 = sp.integrate(f_x2,x)
int_f_x2 += C1
int_f_x2