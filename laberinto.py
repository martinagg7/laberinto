def laberintof():
    muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
    laberinto=[]
    for i in range(5):
        fila=[]
        for j in range(5):
            tupla=(i,j)
            if tupla in muro:
                fila.append("x")
            else:
                fila.append(' ')
        laberinto.append(fila)
    return laberinto
if __name__=="__main__":
    for i in range(5):
        print(laberintof()[i])