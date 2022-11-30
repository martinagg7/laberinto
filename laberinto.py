
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
laberinto=[]
for i in range(5):
    fila=[]
    for j in range(5):
        print(i,j)
        tupla=(i,j)
        print(tupla[0])
        if tupla in muro:
            fila.append("x")
        else:
            fila.append(' ')
    laberinto.append(fila)
for i in range(5):
    print(laberinto[i])
