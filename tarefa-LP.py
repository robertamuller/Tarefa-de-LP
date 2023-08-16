import numpy as np 
a = 8
#1
um = np.random.randint(0,10,a)
dois = np.random.randint(0,10,a)

tres = um + dois

#2
tres = tres.reshape(2, int(a/2))
tres = tres * 1.0
tres = np.transpose(tres)

#3

quatro = np.random.randint(0, 10, a).reshape(2, int(a/2))
quatro = np.matmul(tres, quatro)

#4

quinto = np.random.randint(0,10,a)
sexto = np.random.randint(0,10,a)
igual = []
indices = []
diferentes = []

for i in range(0, a):
    if quinto[i] == sexto[i]:
        igual.append(quinto[i])
        indices.append(i)
    elif quinto[i] not in sexto:
        diferentes.append(quinto[i])
        
print(igual)
print(indices)
print(diferentes)

#5

sete = np.stack((quinto, sexto))
print(np.average(sete))
print(np.std(sete))
print(np.var(sete))
for i in range(0, 2):
    for j in range(0, 8):
        if sete[i][j] % 2 == 0:
            sete[i][j] = 1
        else:
            sete[i][j] = -1

#6

A = np.random.randint(0,10,a)
B = np.random.randint(0,10,a)

print(np.dot(A, B))

#7 

oito = np.random.randint(0, 10, 9).reshape(3,3)
eye_8 = np.eye(8)
det = np.linalg.det(oito)

if det != 0:
    inv = np.linalg.inv(oito)
    
    np.matmul(inv, oito)
    
    for i in range(0, 3):
        for j in range(0, 3):
            if i == j:
                if inv[i][i] >= 0.99 or inv[i][i] <= 1.01:
                    inv[i][i] = 1
                elif inv[i][j] >= -0.01 or inv[i][j] <= 0.01:
                    inv[i][j] = 0
                    
    if np.array_equal(eye_8, oito):
        print("é inversa")
