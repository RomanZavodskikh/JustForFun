import np
import random

inf = float("inf")

L = np.matrix( 
((inf, 38, 74, 59, 45),
(38, inf, 46, 61, 72),
(74, 46, inf, 49, 85),
(59, 61, 49, inf, 42),
(45, 72, 85, 42, inf)) )

tau = np.matrix(
((1, 1, 1, 1, 1),
 (1, 1, 1, 1, 1),
 (1, 1, 1, 1, 1),
 (1, 1, 1, 1, 1),
 (1, 1, 1, 1, 1)) )

print ("L = ")
print (L)
print ("tau = ")
print (tau)

eta = np.matrix(L)

for i in range(5):
    for j in range(5):
        eta[i].transpose()[j] = np.matrix(1/eta[i].transpose()[j])

P = np.matrix(L)
for i in range(5):
    sum = 0
    for k in range(5):
        sum += eta[i].transpose()[k] * tau[i].transpose()[k]
    for j in range(5):
        P[i].transpose()[j] = np.matrix(100*eta[i].transpose()[j] * tau[i].\
        transpose()[j]/sum)

print("P = ")
print(P)

need_to_go = np.matrix((False, True, True, True, True));
cur_place = 0
length = 0
random.seed()

print(cur_place+1, end="")
finished = False
while not finished:
    num = random.randint(1, 100)
    for k in range(5):
        num -= P[cur_place].transpose()[k]
        if num <= 0:
            if need_to_go.transpose()[k]:
                step = L[cur_place].transpose()[k]
                length += step
                cur_place = k
                print(" -", step ,"--> ", k+1, end="")
                need_to_go.transpose()[k] = False
                if not need_to_go.any():
                    finished = True

print("")
print("length=", length)
