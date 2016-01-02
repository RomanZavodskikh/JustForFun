import np

def f(x):
    return 1 if x >= 0 else -1

x = [];
w = [];

x.append( np.matrix((-1, 1, -1, 1)) )
x[0] = x[0].transpose()
x.append( np.matrix((1, -1, 1, 1)) )
x[1] = x[1].transpose()
x.append( np.matrix((-1, 1, -1, -1)) )
x[2] = x[2].transpose()

for i in range(len(x)):
    w.append( x[i]*x[i].transpose() )

W = w[0]
for i in range(1, len(w)):
    W = W + w[i] 

for i in range(len(W)):
        W[i].transpose()[i] = np.matrix([[0]])

border = 50

finished = False
times = 0
coll = []
print("Print 4 numbers: it'll be the vector to identificate")
for i in range(4):
    a = int(input())
    coll.append(a)

y = np.matrix(coll)
print("y ==",y)
y = y.transpose()

while not finished and times < border:

    y = W*y
    for i in range(4):
        y[i] = np.matrix((f(y[i])))

    for i in range(3):
        if bool ((y == x[i]).transpose().all(True)):
            finished = True

    print(times, y.transpose())

    times+=1

if finished:
    print(y)
else:
    print("Cannot identificate")
