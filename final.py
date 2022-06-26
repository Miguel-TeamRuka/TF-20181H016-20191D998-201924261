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