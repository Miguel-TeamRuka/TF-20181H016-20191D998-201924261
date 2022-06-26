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

def calcularPeso(nroAutos,velocidad,distancia):
  return velocidad*(nroAutos/distancia)

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
    return pic

def reglas(m,n,pic):
  if pic[m][n]>=-1 and pic[m][n]<-0.5:
    return random.randint(47, 52),random.randint(10,20)
    #return 30,12
  if pic[m][n]>=-0.5 and pic[m][n]<-0.2:
    return random.randint(41,46),random.randint(21,28)
    #return 26,20
  if pic[m][n]>=-0.2 and pic[m][n]<0.2:
    return random.randint(31,40),random.randint(29, 34)
    #return 20,32
  if pic[m][n]>=0.2 and pic[m][n]<0.5:
    return random.randint(21,30),random.randint(34,39)
    #return 16,36
  if pic[m][n]>=0.5 and pic[m][n]<=1:
    return random.randint(10, 20),random.randint(40,45)
    #return 10,40
#print(pic[5][26])
#print(reglas(5,26))
#print(pic[39][26])
#print(reglas(39,26))

def returnCoefHour():
  now = datetime.now()
  
  if now.hour>=0 and now.hour<7:
    return float(decimal.Decimal(random.randrange(60, 80))/100)
    #return 0.5
  if now.hour>=7 and now.hour<10:
    return float(decimal.Decimal(random.randrange(120, 140))/100)
    #return 1.2
  if now.hour >=10 and now.hour<18: 
    return float(decimal.Decimal(random.randrange(100, 110))/100)
    #return 1
  if now.hour >=18 and now.hour<22:   
    return float(decimal.Decimal(random.randrange(140, 160))/100)
    #return 1.25
  if now.hour >=22 and now.hour<0:
    return float(decimal.Decimal(random.randrange(80, 95))/100)
    #return 0.9
  if now.hour==22:
    return float(decimal.Decimal(random.randrange(80, 95))/100)
    #return 0.9
  return 1

def pesoFinal(origin,neighbort,picI,picJ,nodes,perlin):
  distanciaValor = distancia(origin,neighbort,nodes)
  nroAutos,velocidad =reglas(picI,picJ,perlin)
  return round(calcularPeso(nroAutos,velocidad,distanciaValor)*returnCoefHour(),2)


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
            #nodeO=nodes[origin]
            #nodeD=nodes[right]
            #d=haversine(nodeO[3],nodeO[4],nodeD[3],nodeD[4])
            #peso=distancia(origin,right)
            peso= pesoFinal(origin,right,i,j+1,nodes,perlin)
            auxiliar.append((right,peso))
      if j>0: #inicio de una fila
          if b[i][j-1]!=-1:
            left=b[i][j-1]
            origin=b[i][j]
            #nodeO=nodes[origin]
            #nodeD=nodes[left]
            #d=haversine(nodeO[3],nodeO[4],nodeD[3],nodeD[4])
            #peso=distancia(origin,left)
            peso= pesoFinal(origin,left,i,j-1,nodes,perlin)
            auxiliar.append((left,peso))
      if i<len(hor)-1: #final de una columna
          if b[i+1][j]!=-1:
            bottom=b[i+1][j]
            origin=b[i][j]
            #nodeO=nodes[origin]
            #nodeD=nodes[bottom]
            #d=haversine(nodeO[3],nodeO[4],nodeD[3],nodeD[4])
            #peso=distancia(origin,bottom)
            peso= pesoFinal(origin,bottom,i+1,j,nodes,perlin)
            auxiliar.append((bottom,peso))
      if i>0: #inicio de una columna
          if b[i-1][j]!=-1:
            top=b[i-1][j]
            origin=b[i][j]
            #nodeO=nodes[origin]
            #nodeD=nodes[top]
            #d=haversine(nodeO[3],nodeO[4],nodeD[3],nodeD[4])
            #peso=distancia(origin,top)
            peso= pesoFinal(origin,top,i-1,j,nodes,perlin)
            auxiliar.append((top,peso))
      listAd.append(auxiliar)
      auxiliar=[]

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
                    #f.write(str(j))
                    f.write(re.sub(r'[\(\,)]','',str(j)))
                else:
                    #f.write(str(j)+" ")
                    f.write(re.sub(r'[\(\,)]','',str(j)+" "))
                c=c+1
            c=0
            if i<len(listAd)-1:
                f.write('\n')
def LeerListaAd():
    generarListaAd()
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
                Gr[-1].append((nums[i], nums[i+1]))

   # nums = [float(x) for x in line.split()]
   # G.append([])
   # for i in range(0, len(nums), 2):
   #   G[-1].append((nums[i], nums[i+1]))
   # for x in Gr:
   #     print(x)
    return Gr
    #for x in Gr:
    #    print(x)