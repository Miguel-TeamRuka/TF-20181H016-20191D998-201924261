from importlib.resources import path
import random
import numpy
from numpy import random as rd
from csv import reader
import math as mth
import decimal
import heapq as hq
import re
from perlin_noise import PerlinNoise
from datetime import datetime
import matplotlib.pyplot as plt

def HorizontalTXT():
    hor=[]
    with open('Horizontal.txt', 'r') as my_file:
     file_csv = reader(my_file)
     head = next(file_csv)
     if head is not None:
        for i in file_csv:
            v4,v5,v6,v7=i
            hor.append((v4,int(v5),int(v6),int(v7)))
    return hor
    #print(hor)

def VerticalTXT():
    ver=[]
    with open('Vertical.txt', 'r') as my_file:
     file_csv = reader(my_file)
     head = next(file_csv)
     if head is not None:
        for i in file_csv:
            v4,v5,v6,v7=i
            ver.append((v4,int(v5),int(v6),int(v7)))
    return ver
    #print(ver)

def Matriz(hor,ver):
    b=rd.randint(-1,0,(len(hor),len(ver)))
    return b

def GenerarNodos(hor,ver,b):
    nodeCount=0
    nodes=[]

    for i in range(len(hor)):
        n1,x1,y1,c1=hor[i]
        for j in range(len(ver)):
            n2,x2,y2,c2=ver[j]
            if x2>=x1 and x2<=x1+c1 and y1>=y2 and y1<=y2+c2:
                b[i][j]=nodeCount

                auxlat=(360*y1/1000)/39942.3024
                lat=41.997248-auxlat

                paracos=(3.141592/180)*lat
                auxlongit=(360*x2/1000)/(40074.2496*mth.cos(paracos))
                longit=-87.728917+auxlongit

                nodes.append((nodeCount,n1,n2,round(lat,6),round(longit,6)))
                nodeCount=nodeCount+1
    
    return nodes

def EscribirNodos(nodes):
  with open('Nodos.txt', 'w') as f:
   f.write("Nodo,Calle Horizontal,Calle Vertical,Latitud,Longitud"+'\n')
   for count,n in enumerate(nodes):
    if count<len(nodes)-1:
     f.write(str(n[0])+","+n[1]+","+n[2]+","+str(n[3])+","+str(n[4])+'\n')
    else:
      f.write(str(n[0])+","+n[1]+","+n[2]+","+str(n[3])+","+str(n[4]))

def LeerNodos():
  myNodos=[]
  with open('Nodos.txt', 'r') as my_file:
    file_csv = reader(my_file)
    head = next(file_csv)
    if head is not None:
        for i in file_csv:
            nodo,c1,c2,lat,lon=i
            myNodos.append((int(nodo),c1,c2,lat,lon))
  return myNodos
  #for i in myNodos:
   #print(f"El nodo {i[0]} es la interseccion de las calles {i[1]} y {i[2]}")

def leerNodosLatLon():
    myNodos=[]
    with open('Nodos.txt', 'r') as my_file:
        file_csv = reader(my_file)
        head = next(file_csv)
        if head is not None:
                for i in file_csv:
                    nodo,c1,c2,lat,lon=i
                    myNodos.append((float(lat),float(lon)))
    return myNodos

def Radianes(c):
  return (mth.pi/180)*c

def haversine(lat1,lon1,lat2,lon2):
  dlat=Radianes(lat2)-Radianes(lat1)
  dlon=Radianes(lon2)-Radianes(lon1)
  
  
  a = mth.sin(dlat/2)**2 + mth.cos(Radianes(lat1)) * mth.cos(Radianes(lat2)) * mth.sin(dlon/2)**2
  c = 2 * mth.asin(mth.sqrt(a))
  r = 6371

  return round(c * r, 3)

def distancia(origen,destino,nodes):
  nodeO=nodes[origen]
  nodeD=nodes[destino]
  d=haversine(nodeO[3],nodeO[4],nodeD[3],nodeD[4])
  
  return d

def GenerarPerlinNoise():
    noise1 = PerlinNoise(octaves=2)
    noise2 = PerlinNoise(octaves=4)
    noise3 = PerlinNoise(octaves=8)
    noise4 = PerlinNoise(octaves=12)

    xpix, ypix = 51,41
    pic = []
    for i in range(xpix):
        row = []
        for j in range(ypix):
            noise_val = noise1([i/xpix, j/ypix])
            noise_val += 0.100 * noise2([i/xpix, j/ypix])
            noise_val += 0.070 * noise3([i/xpix, j/ypix])
            noise_val += 0.035 * noise4([i/xpix, j/ypix])
            row.append(noise_val)
      
        pic.append(row)

    #plt.imshow(pic, cmap='gray')
    #plt.show()
    #print(pic)
    return pic

def reglas(m,n,pic):
  if pic[m][n]>=-1 and pic[m][n]<-0.5:
    return random.randint(3250,3800)
    
  if pic[m][n]>=-0.5 and pic[m][n]<-0.2:
    return random.randint(2100,2800)
   
  if pic[m][n]>=-0.2 and pic[m][n]<0.2:
    return random.randint(1000,1650)
    
  if pic[m][n]>=0.2 and pic[m][n]<0.5:
    return random.randint(450,790)
    
  if pic[m][n]>=0.5 and pic[m][n]<=1:
    return random.randint(80,190)


def returnHour(m,n,pic):
    now = datetime.now()
    if now.hour>=0 and now.hour<7:
        if pic[m][n]>=-1 and pic[m][n]<-0.5:
         return float(decimal.Decimal(random.randrange(25, 39))/100)
    
        if pic[m][n]>=-0.5 and pic[m][n]<-0.2:
          return float(decimal.Decimal(random.randrange(30,38))/100)
    
        if pic[m][n]>=-0.2 and pic[m][n]<0.2:
         return float(decimal.Decimal(random.randrange(58,68))/100)
    
        if pic[m][n]>=0.2 and pic[m][n]<0.5:
          return float(decimal.Decimal(random.randrange(90,100))/100)
    
        if pic[m][n]>=0.5 and pic[m][n]<=1:
          return float(decimal.Decimal(random.randrange(92,105))/100)
      
    
    if now.hour>=7 and now.hour<10:
      if pic[m][n]>=-1 and pic[m][n]<-0.5:
         return float(decimal.Decimal(random.randrange(105, 122))/100)
    
      if pic[m][n]>=-0.5 and pic[m][n]<-0.2:
          return float(decimal.Decimal(random.randrange(105,125))/100)
    
      if pic[m][n]>=-0.2 and pic[m][n]<0.2:
         return float(decimal.Decimal(random.randrange(125,138))/100)
    
      if pic[m][n]>=0.2 and pic[m][n]<0.5:
          return float(decimal.Decimal(random.randrange(111,125))/100)
    
      if pic[m][n]>=0.5 and pic[m][n]<=1:
          return float(decimal.Decimal(random.randrange(980,102))/100)
    

    if now.hour >=10 and now.hour<18: 
      if pic[m][n]>=-1 and pic[m][n]<-0.5:
         return float(decimal.Decimal(random.randrange(55, 60))/100)
    
      if pic[m][n]>=-0.5 and pic[m][n]<-0.2:
          return float(decimal.Decimal(random.randrange(58,65))/100)
    
      if pic[m][n]>=-0.2 and pic[m][n]<0.2:
         return float(decimal.Decimal(random.randrange(88,92))/100)
    
      if pic[m][n]>=0.2 and pic[m][n]<0.5:
          return float(decimal.Decimal(random.randrange(86,90))/100)
    
      if pic[m][n]>=0.5 and pic[m][n]<=1:
          return float(decimal.Decimal(random.randrange(80,86))/100)
    

    if now.hour >=18 and now.hour<22:   
      if pic[m][n]>=-1 and pic[m][n]<-0.5:
         return float(decimal.Decimal(random.randrange(105, 112))/100)
    
      if pic[m][n]>=-0.5 and pic[m][n]<-0.2:
          return float(decimal.Decimal(random.randrange(105,125))/100)
    
      if pic[m][n]>=-0.2 and pic[m][n]<0.2:
         return float(decimal.Decimal(random.randrange(125,138))/100)
    
      if pic[m][n]>=0.2 and pic[m][n]<0.5:
          return float(decimal.Decimal(random.randrange(116,125))/100)
    
      if pic[m][n]>=0.5 and pic[m][n]<=1:
          return float(decimal.Decimal(random.randrange(100,125))/100)
    
    if now.hour >=22 and now.hour<=23:
      if pic[m][n]>=-1 and pic[m][n]<-0.5:
         return float(decimal.Decimal(random.randrange(100, 105))/100)
    
      if pic[m][n]>=-0.5 and pic[m][n]<-0.2:
          return float(decimal.Decimal(random.randrange(98,102))/100)
    
      if pic[m][n]>=-0.2 and pic[m][n]<0.2:
         return float(decimal.Decimal(random.randrange(95,98))/100)
    
      if pic[m][n]>=0.2 and pic[m][n]<0.5:
          return float(decimal.Decimal(random.randrange(90,95))/100)
    
      if pic[m][n]>=0.5 and pic[m][n]<=1:
          return float(decimal.Decimal(random.randrange(85,92))/100)
    
    
    return 1
def calcularPeso(aux,distancia):
  #return velocidad*(nroAutos/distancia)*0.1
  #return velocidad*nroAutos*distancia*0.1
  #return 10*nroAutos*distancia/velocidad
  #return 10*nroAutos*distancia
  return aux

def pesoFinal(origin,neighbort,picI,picJ,nodes,perlin):
  distanciaValor = distancia(origin,neighbort,nodes)
  aux =reglas(picI,picJ,perlin)
  hour=returnHour(picI,picJ,perlin)
  return round(calcularPeso(aux,distanciaValor)*hour,2)


def GenerarAristas(hor,ver,b,nodes,perlin):
  listAd=[]
  auxiliar=[]
  for i in range(len(hor)):
    for j in range(len(ver)):
      if b[i][j]!=-1:
        if j<len(ver)-1: #final de una fila
          if b[i][j+1]!=-1:
            right=b[i][j+1]
            origin=b[i][j]
            peso= pesoFinal(origin,right,i,j+1,nodes,perlin)
            auxiliar.append((right,peso))
          if b[i][j+1]==-1:
            index=1
            if j+index<len(ver)-1:
              while b[i][j+index]==-1 and j+index<len(ver)-1 :
                index=index+1
              if b[i][j+index]!=-1:
                  right=b[i][j+index]
                  origin=b[i][j]
                  peso= pesoFinal(origin,right,i,j+index,nodes,perlin)
                  auxiliar.append((right,peso))
                  index=0
        if j>0: #inicio de una fila
          if b[i][j-1]!=-1:
            left=b[i][j-1]
            origin=b[i][j]
            peso= pesoFinal(origin,left,i,j-1,nodes,perlin)
            auxiliar.append((left,peso))
          if b[i][j-1]==-1:
            index=1
            if j-index>0:
              while b[i][j-index]==-1 and j-index>0 :
                index=index+1
              if b[i][j-index]!=-1:
                left=b[i][j-index]
                origin=b[i][j]
                peso= pesoFinal(origin,left,i,j-index,nodes,perlin)
                auxiliar.append((left,peso))
                index=0
        if i<len(hor)-1: #final de una columna
          if b[i+1][j]!=-1:
            bottom=b[i+1][j]
            origin=b[i][j]
            peso= pesoFinal(origin,bottom,i+1,j,nodes,perlin)
            auxiliar.append((bottom,peso))
          else:
            index=1
            if i+index<len(hor)-1:
              while b[i+index][j]==-1 and i+index<len(hor)-1 :
               #print(index)
                index=index+1
              if b[i+index][j]!=-1:
                bottom=b[i+index][j]
                origin=b[i][j]
                peso= pesoFinal(origin,bottom,i+index,j,nodes,perlin)
                auxiliar.append((bottom,peso))
                index=0
        if i>0: #inicio de una columna
          if b[i-1][j]!=-1:
            top=b[i-1][j]
            origin=b[i][j]
            peso= pesoFinal(origin,top,i-1,j,nodes,perlin)
            auxiliar.append((top,peso))
          else:
            index=1
            if i-index>0:
              while b[i-index][j]==-1 and i-index>0 :
                #print(index)
                index=index+1
              if b[i-index][j]!=-1:
                top=b[i-index][j]
                origin=b[i][j]
                peso= pesoFinal(origin,top,i-index,j,nodes,perlin)
                auxiliar.append((top,peso))
                index=0
        listAd.append(auxiliar)
        auxiliar=[]
  for l in listAd:
    print(l)
  return listAd
  #print(listAd)
  #for l in listAd:
  #  print(l)

def EscribirListaAd(listAd):
    c=0
    with open('ListaAdyacencia.txt', 'w') as f:
        for i in range(len(listAd)):
            for j in listAd[i]:
                if(c==len(listAd[i])-1):
                    f.write(re.sub(r'[\(\,)]','',str(j)))
                else:
                    f.write(re.sub(r'[\(\,)]','',str(j)+" "))
                c=c+1
            c=0
            if i<len(listAd)-1:
                f.write('\n')
def LeerListaAd():
    #generarListaAd()
    with open("ListaAdyacencia.txt") as f:
        Gr = []
        for line in f:
            nums=[]
    
            for count,x in enumerate(line.split()):
                if count%2==0:
                    nums.append(int(x))
                else:
                    nums.append(float(x))
            Gr.append([])

            for i in range(0, len(nums), 2):
                Gr[-1].append((int(nums[i]), int(nums[i+1])))

   # nums = [float(x) for x in line.split()]
   # G.append([])
   # for i in range(0, len(nums), 2):
   #   G[-1].append((nums[i], nums[i+1]))
   # for x in Gr:
   #     print(x)
    return Gr
    #for x in Gr:
    #    print(x)

def generarListaAd():
    CallesHor=[]
    CallesVer=[]
    Nodos=[]
    Perlin=[]
    ListaAd=[]

    CallesHor=HorizontalTXT()
    CallesVer=VerticalTXT()
    Matrix=Matriz(CallesHor,CallesVer)
    Nodos=GenerarNodos(CallesHor,CallesVer,Matrix)
    print(Matrix)
    Perlin=GenerarPerlinNoise()
    print("a")
    EscribirNodos(Nodos)
    print("b")
    ListaAd=GenerarAristas(CallesHor,CallesVer,Matrix,Nodos,Perlin)
    print("c")
    EscribirListaAd(ListaAd)

def dijkstraList(G, s,indices):
  n = len(G)
  visited = [False]*n
  path = [-1]*n
  cost = [mth.inf]*n

  cost[s] = 0
  pqueue = [(0, s)]
  while pqueue:
    g, u = hq.heappop(pqueue)
    if not visited[u]:
      visited[u] = True
      if indices[u]!=-1:
       for v, w in G[u]:
        if not visited[v]:
          f = g + w
          if f < cost[v]:
            cost[v] = f
            path[v] = u
            hq.heappush(pqueue, (f, v))

  return path, cost

def route(ini,fin,path):
  ruta=[]
  aux=fin
  ruta.append(aux)
  c=ini
  while ini!=aux:
   p=path[aux]
   aux=p
   if(p!=ini):
    ruta.append(aux)
  ruta.append(ini)
  return ruta

def routeShort(inicio,fin,graf,indice):
  path, cost = dijkstraList(graf,inicio,indice)
  #print(path)
  #print(path[fin])
  #print(cost)
  aux=route(inicio,fin,path)
  return aux,cost[fin],path

def secondAndThird(array,ini,fin,pesos,grapf,indices):
  pathReturn2=[]
  wReturn2=[]
  pathReturn3=[]
  wReturn3=[]
  way2=[]
  wTotal2=[]
  queue=[]
  for count,i in enumerate(array):
    des=i
    if len(queue)>0 and indices[queue[count-1]]==-1:
      indices[queue[count-1]]=0
    queue.append(des)
    indices[des]=-1

    way2,wTotal2=dijkstraList(grapf,ini,indices)
    if count==0:
      if wTotal2[fin]<pesos[1] and wTotal2[fin]>pesos[0]:
        pesos[1]=wTotal2[fin]
        pathReturn2=way2
        wReturn2=wTotal2
    if count>0:
      if wTotal2[fin]<pesos[1] and wTotal2[fin]>pesos[0]:
        pesos[1]=wTotal2[fin]
        pathReturn2=way2
        wReturn2=wTotal2
      if wTotal2[fin]<pesos[2] and  wTotal2[fin]>pesos[1]:
        pesos[2]=wTotal2[fin]
        pathReturn3=way2
        wReturn3=wTotal2
  return wReturn2[fin],pathReturn2,wReturn3[fin],pathReturn3

def returnPath(path):
    aux=[]
    for i in range(len(path)):
        if i!=0 and i!=len(path)-1:
            aux.append(path[i])
    return aux

def route2Shortest(G,s,t):
  pesos=[100000000,100000000,1000000000]
  indices=[0]*len(G)
  indices[0]=0
  path1=[]
  aux1=[]
  w1=0

  path2=[]
  aux2=[]
  w2=0

  path3=[]
  aux3=[]
  w3=0

  aux1,w1,path1=routeShort(s,t,G,indices)
  pesos[0]=w1
  indices=[0]*len(G)
  aux1=returnPath(path1)

  w2,path2,w3,path3=secondAndThird(aux1,s,t,pesos,G,indices)
  print(w1,w2,w3)
  
  return path1,path2,path3