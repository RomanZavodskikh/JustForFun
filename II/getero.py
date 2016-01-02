import np

def f(x):
    return -1 if x <= 0 else 1

x = [];
x.append( 0 )
x.append ( np.matrix((1, -1, 1, -1)) )
x.append ( np.matrix((-1, 1, -1, 1)) )
x.append ( np.matrix((1, 1, 1, -1)) )
x.append ( np.matrix((-1, -1, 1, -1)) )


l = []
print("Print 4 numbers: it'll be the vector:")
for i in range(4):
    a = int( input() )
    l.append(a)

x_star = np.matrix(l)

y = []
y.append( 0 )
y.append ( np.matrix((-1, -1, 1)) )
y.append ( np.matrix((-1, 1, -1)) )
y.append ( np.matrix((-1, 1, 1)) )
y.append ( np.matrix((1, -1, -1)) )

W = y[1].transpose()*x[1]
for i in range(2, 5):
    w = y[i].transpose()*x[i]
    W = W + w;

print(W)

x_star = W * x_star.transpose()
print(x_star)

for i in range(len(x_star)):
    x_star[i] = f(x_star[i])

print(x_star)

num = 0
for i in range(len(x_star)):
    num *= 2;
    if x_star[i] == 1:
        num += 1;

print("This vector", np.matrix(l), "associates with number", num)
