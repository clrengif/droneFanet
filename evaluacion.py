# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 19:52:31 2022

@author: wzamb
"""
import math 
import random
import numpy as np
from os import remove
from ast import literal_eval
from tqdm import tqdm


mdipolo=[]
totaldipolo=[]
totaldipolo2=[]
totaldipolomutacion2=[]
totaldipolocruzamineto3=[]
m2dipolo=[]
coordenadas=[]
At=90
Np=2*math.pi
contador = 0
#rango0=input("ingrese el numero de coordenadas que desea generar: ")
#rango1=input("ingrese el rango en el que se generan las cooredenadas aleatorios: ")
#rango2=input(": ")
#rango3=input("ingrese la margen de error que genera el movimiento del dron: ")
#repeticiones=input("ingrese el numero de interaciones:")

rango0 = 30
rango1=1
rango2=500
rango3=10
repeticiones = 5000

rango0=int(rango0)
rango1=float(rango1) 
rango2=float(rango2) 
rango3=float(rango3) 
repeticiones=int(repeticiones)
# lista con los nombres de los archivos a limpiar


pbar = tqdm(total=repeticiones, ncols=50)
def creartxt():
 
	archivo=open('cordenadas.txt','a')
	archivo.close()  
#remove('cordenadas.txt')
for i in range(rango0):
    x11=(random.uniform(rango1,rango2))
    x22=(random.uniform(rango1,rango2))
    x33=(random.uniform(rango1,rango2))
    x44=(random.uniform(rango1,rango2))
    x55=(random.uniform(rango1,rango2))
    y11=(random.uniform(rango1,rango2))
    y22=(random.uniform(rango1,rango2))
    y33=(random.uniform(rango1,rango2))
    y44=(random.uniform(rango1,rango2))
    y55=(random.uniform(rango1,rango2))
    
    x111=x11-rango3
    x112=x11+rango3
    x221=x22-rango3
    x222=x22+rango3
    x331=x33-rango3
    x332=x33+rango3
    x441=x44-rango3
    x442=x44+rango3
    x551=x55-rango3
    x552=x55+rango3

    y111=y11-rango3
    y112=y11+rango3
    y221=y22-rango3
    y222=y22+rango3
    y331=y33-rango3
    y332=y33+rango3
    y441=y44-rango3
    y442=y44+rango3
    y551=y55-rango3
    y552=y55+rango3

     
    for x1 in range(1):
      x1= random.uniform(x111,x112)
      x2= random.uniform(x221,x222)
      x3= random.uniform(x331,x332)
      x4= random.uniform(x441,x442)
      x5= random.uniform(x551,x552)
      y1= random.uniform(y111,y112)
      y2= random.uniform(y221,y222)
      y3= random.uniform(y331,y332)
      y4= random.uniform(y441,y442)
      y5= random.uniform(y551,y552)
    
    
    def agregar_item():
        todo_descripcion1 =  str(x1)
        todo_descripcion2 =  str(x2)
        todo_descripcion3 =  str(x3)
        todo_descripcion4 =  str(x4)
        todo_descripcion5 =  str(x5)
        todo_descripcion6 =  str(y1)
        todo_descripcion7 =  str(y2)
        todo_descripcion8 =  str(y3)
        todo_descripcion9 =  str(y4)
        todo_descripcion10 =  str(y5)
        archivo=open('cordenadas.txt','a')
        archivo.write(todo_descripcion1)
        archivo.write("  ")
        archivo.write(todo_descripcion2)
        archivo.write("  ")
        archivo.write(todo_descripcion3)
        archivo.write("  ")
        archivo.write(todo_descripcion4)
        archivo.write("  ")
        archivo.write(todo_descripcion5)
        archivo.write("  ")
        archivo.write(todo_descripcion6)
        archivo.write("  ")
        archivo.write(todo_descripcion7)
        archivo.write("  ")
        archivo.write(todo_descripcion8)
        archivo.write("  ")
        archivo.write(todo_descripcion9)
        archivo.write("  ")
        archivo.write(todo_descripcion10)

        archivo.write("\n")
        archivo.close()
    creartxt()
    agregar_item()
    
    
m=[]
m1=[]
def creartxt():
      archivo=open('datos.txt','a')
      archivo.close()     
remove('datos.txt')
archivo=open("cordenadas.txt","r")

for i in range(rango0):
    Af=0
    mdipolo=[]
    line=archivo.readline()  
    m.extend([float(n) for n in line.split()])       
    #m1.append(m)
    x11=m[0]
    x22=m[1]
    x33=m[2]
    x44=m[3]
    x55=m[4]
    y11=m[5]
    y22=m[6]
    y33=m[7]
    y44=m[8]
    y55=m[9]
    m=[]
    
    
    while Af<=6.28319:
        
        Rx1=(Np*x11)*math.sin(At)*math.cos(Af)
        Rx2=(Np*x22)*math.sin(At)*math.cos(Af)
        Rx3=(Np*x33)*math.sin(At)*math.cos(Af)
        Rx4=(Np*x44)*math.sin(At)*math.cos(Af)
        Rx5=(Np*x55)*math.sin(At)*math.cos(Af)
        
        Ry1=(Np*y11)*math.sin(At)*math.sin(Af)
        Ry2=(Np*y22)*math.sin(At)*math.sin(Af)
        Ry3=(Np*y33)*math.sin(At)*math.sin(Af)
        Ry4=(Np*y44)*math.sin(At)*math.sin(Af)
        Ry5=(Np*y55)*math.sin(At)*math.sin(Af)
        
        Rxy1=Rx1+Ry1
        Rxy2=Rx2+Ry2
        Rxy3=Rx3+Ry3
        Rxy4=Rx4+Ry4
        Rxy5=Rx5+Ry5

        MJ1=math.cos(Rxy1)
        MJ2=math.cos(Rxy2)
        MJ3=math.cos(Rxy3)
        MJ4=math.cos(Rxy4)
        MJ5=math.cos(Rxy5)
       
        MJ11=math .sin(Rxy1)
        MJ22=math.sin(Rxy2)
        MJ33=math.sin(Rxy3)
        MJ44=math.sin(Rxy4)
        MJ55=math.sin(Rxy5)
       
        A=MJ1+MJ2+MJ3+MJ4+MJ5
        B=MJ11+MJ22+MJ33+MJ44+MJ55
        
        total=math.sqrt((A*A)+(B*B))
        T=np.absolute(total)
       
        antdi=((math.cos((math.pi/2)*math.cos(At)))/math.sin(At))
        D=np.absolute(antdi)
       
        dipolos=T*D
        mdipolo.append(dipolos)
        
         
        def agregar_item():
             todo_descripcion =  str(dipolos)
             archivo=open('datos.txt','a')
             archivo.write(todo_descripcion)
             archivo.write("\n")
             archivo.close()
        creartxt()
        agregar_item()
        
      
        
        Af +=0.025
        

    totaldipolo.append([mdipolo])
#print(totaldipolo[0])
def creartxt():
      archivo=open('segundonum.txt','a')
      archivo.close()     
remove('segundonum.txt')
for k in range(rango0):
    l=totaldipolo[k]
    p = str(l)[1:-1]
    p=literal_eval(p)
    z=sorted(p)[-2]
    
    def agregar_item():
        todo_descripcion =  str(z)
        archivo=open('segundonum.txt','a')
        archivo.write(todo_descripcion)
        archivo.write("\n")
        archivo.close()
    creartxt()
    agregar_item()

for i in range(rango0):
    with open("cordenadas.txt", "r") as archivo:
         lineas = archivo.readlines()
         indices_aleatorios = random.sample(range(len(lineas)), 2)
         
         linea1 = lineas[indices_aleatorios[0]].strip().split()
         linea2 = lineas[indices_aleatorios[1]].strip().split()

         a = [float(num) for num in linea1]
         b = [float(num) for num in linea2]
         #print(a) 
         #print(b)
         Mcruzamiento=[
                      [a[0],b[1],a[2],b[3],a[4],a[5],b[6],a[7],b[8],a[9]],
                      [b[0],a[1],b[2],a[3],b[4],b[5],a[6],b[7],a[8],b[9]],
                      [b[0],b[1],a[2],b[3],a[4],b[5],b[6],a[7],b[8],a[9]],
                      [a[0],a[1],b[2],a[3],b[4],a[5],a[6],b[7],a[8],b[9]],
                      [b[0],b[1],b[2],a[3],a[4],b[5],b[6],b[7],a[8],a[9]],
                      [a[0],a[1],a[2],b[3],b[4],a[5],a[6],a[7],b[8],b[9]],
                      [a[0],a[1],b[2],b[3],b[4],a[5],a[6],b[7],b[8],b[9]],
                      [b[0],b[1],a[2],a[3],a[4],b[5],b[6],a[7],a[8],a[9]],
                      [a[0],b[1],a[2],b[3],b[4],a[5],b[6],a[7],b[8],b[9]],
                      [b[0],a[1],b[2],a[3],a[4],b[5],a[6],b[7],a[8],a[9]]
                      ]
         cruzamiento =0
         C=[]
         k=[]
         def creartxt():
               archivo=open('seleccion2.txt','a')
               archivo.close()   
               archivo=open('seleccion3.txt','a')
               archivo.close() 
         def creartxt():
               archivo=open('cordenadas2.txt','a')
               archivo.close()     
         
         for i in range(1):
             Af=0
             m2dipolo=[]
             m3dipolo=[]
             j=random.random()
             l=random.random()
             if j>0.9:
                 break
             if (j>=0)and(j<=0.9): #Cruzamiento
                 cruzamineto =1
                 C=(random.choice(Mcruzamiento))
                 #print(C,"correcto, combinacion  ")  
             mutacion=0
             if (l>0.9)and(l<=1): #Mutacion
                    mutacion=1
                    Mmutacion=[
                            [C[0]+0.1,C[1],C[2],C[3],C[4],C[5],C[6],C[7],C[8],C[9]],
                            [C[0],C[1]+0.1,C[2],C[3],C[4],C[5],C[6],C[7],C[8],C[9]],
                            [C[0],C[1],C[2]+0.1,C[3],C[4],C[5],C[6],C[7],C[8],C[9]],
                            [C[0],C[1],C[2],C[3]+0.1,C[4],C[5],C[6],C[7],C[8],C[9]],
                            [C[0],C[1],C[2],C[3],C[4]+0.1,C[5],C[6],C[7],C[8],C[9]],
                            [C[0],C[1],C[2],C[3],C[4],C[5]+0.1,C[6],C[7],C[8],C[9]],
                            [C[0],C[1],C[2],C[3],C[4],C[5],C[6]+0.1,C[7],C[8],C[9]],
                            [C[0],C[1],C[2],C[3],C[4],C[5],C[6],C[7]+0.1,C[8],C[9]],
                            [C[0],C[1],C[2],C[3],C[4],C[5],C[6],C[7],C[8]+0.1,C[9]],
                            [C[0],C[1],C[2],C[3],C[4],C[5],C[6],C[7],C[8],C[9]+0.1],
                            [C[0]-0.1,C[1],C[2],C[3],C[4],C[5],C[6],C[7],C[8],C[9]],
                            [C[0],C[1]-0.1,C[2],C[3],C[4],C[5],C[6],C[7],C[8],C[9]],
                            [C[0],C[1],C[2]-0.1,C[3],C[4],C[5],C[6],C[7],C[8],C[9]],
                            [C[0],C[1],C[2],C[3]-0.1,C[4],C[5],C[6],C[7],C[8],C[9]],
                            [C[0],C[1],C[2],C[3],C[4]-0.1,C[5],C[6],C[7],C[8],C[9]],
                            [C[0],C[1],C[2],C[3],C[4],C[5]-0.1,C[6],C[7],C[8],C[9]],
                            [C[0],C[1],C[2],C[3],C[4],C[5],C[6]-0.1,C[7],C[8],C[9]],
                            [C[0],C[1],C[2],C[3],C[4],C[5],C[6],C[7]-0.1,C[8],C[9]],
                            [C[0],C[1],C[2],C[3],C[4],C[5],C[6],C[7],C[8]-0.1,C[9]],
                            [C[0],C[1],C[2],C[3],C[4],C[5],C[6],C[7],C[8],C[9]-0.1]
                            ] 
                    k=(random.choice(Mmutacion))
                    
                    if cruzamineto==1:
                        #print("mutacion")
                        x111=k[0]
                        x222=k[1]
                        x333=k[2]
                        x444=k[3]
                        x555=k[4]
                        y111=k[5]
                        y222=k[6]
                        y333=k[7]
                        y444=k[8]
                        y555=k[9]

                        while Af<=6.28319:
                            Rx1=(Np*x111)*math.sin(At)*math.cos(Af)
                            Rx2=(Np*x222)*math.sin(At)*math.cos(Af)
                            Rx3=(Np*x333)*math.sin(At)*math.cos(Af)
                            Rx4=(Np*x444)*math.sin(At)*math.cos(Af)
                            Rx5=(Np*x555)*math.sin(At)*math.cos(Af)
                            
                            Ry1=(Np*y111)*math.sin(At)*math.sin(Af)
                            Ry2=(Np*y222)*math.sin(At)*math.sin(Af)
                            Ry3=(Np*y333)*math.sin(At)*math.sin(Af)
                            Ry4=(Np*y444)*math.sin(At)*math.sin(Af)
                            Ry5=(Np*y555)*math.sin(At)*math.sin(Af)
                            
                            Rxy1=Rx1+Ry1
                            Rxy2=Rx2+Ry2
                            Rxy3=Rx3+Ry3
                            Rxy4=Rx4+Ry4
                            Rxy5=Rx5+Ry5

                            MJ1=math.cos(Rxy1)
                            MJ2=math.cos(Rxy2)
                            MJ3=math.cos(Rxy3)
                            MJ4=math.cos(Rxy4)
                            MJ5=math.cos(Rxy5)
                           
                            MJ11=math.sin(Rxy1)
                            MJ22=math.sin(Rxy2)
                            MJ33=math.sin(Rxy3)
                            MJ44=math.sin(Rxy4)
                            MJ55=math.sin(Rxy5)
                           
                            A=MJ1+MJ2+MJ3+MJ4+MJ5
                            B=MJ11+MJ22+MJ33+MJ44+MJ55
                            
                            total=math.sqrt((A*A)+(B*B))
                            T=np.absolute(total)
                           
                            antdi=((math.cos((math.pi/2)*math.cos(At)))/math.sin(At))
                            D=np.absolute(antdi)
                           
                            dipolos2=T*D
                            m2dipolo.append(dipolos2)
                            #print(m2dipolo)
                            def agregar_item():
                                 todo_descripcion =  str(dipolos2)
                                 archivo=open('seleccion2.txt','a')
                                 archivo.write(todo_descripcion)
                                 archivo.write("\n")
                                 archivo.close()
                            creartxt()
                            agregar_item()
                
                            Af +=0.025
                        totaldipolomutacion2.append([m2dipolo]) 
                        totaldipolo2.append([m2dipolo]) 
                        coordenadas.append([k])
                        k1 = " ".join(str(elemento) for elemento in k)
                        def agregar_item():
                             todo_descripcion =  str(k1)
                             archivo=open('cordenadas2.txt','a')
                             archivo.write(todo_descripcion)
                             archivo.write("\n")
                             archivo.close()
                        creartxt()
                        agregar_item() 
          
             if mutacion==0:
                 #print("cruzamiento")
                 x1111=C[0]
                 x2222=C[1]
                 x3333=C[2]
                 x4444=C[3]
                 x5555=C[4]
                 y1111=C[5]
                 y2222=C[6]
                 y3333=C[7]
                 y4444=C[8]
                 y5555=C[9] 

                 while Af<=6.28319:
                     Rx1=(Np*x1111)*math.sin(At)*math.cos(Af)
                     Rx2=(Np*x2222)*math.sin(At)*math.cos(Af)
                     Rx3=(Np*x3333)*math.sin(At)*math.cos(Af)
                     Rx4=(Np*x4444)*math.sin(At)*math.cos(Af)
                     Rx5=(Np*x5555)*math.sin(At)*math.cos(Af)
                     
                     Ry1=(Np*y1111)*math.sin(At)*math.sin(Af)
                     Ry2=(Np*y2222)*math.sin(At)*math.sin(Af)
                     Ry3=(Np*y3333)*math.sin(At)*math.sin(Af)
                     Ry4=(Np*y4444)*math.sin(At)*math.sin(Af)
                     Ry5=(Np*y5555)*math.sin(At)*math.sin(Af)
                     
                     Rxy1=Rx1+Ry1
                     Rxy2=Rx2+Ry2
                     Rxy3=Rx3+Ry3
                     Rxy4=Rx4+Ry4
                     Rxy5=Rx5+Ry5

                     MJ1=math.cos(Rxy1)
                     MJ2=math.cos(Rxy2)
                     MJ3=math.cos(Rxy3)
                     MJ4=math.cos(Rxy4)
                     MJ5=math.cos(Rxy5)
                    
                     MJ11=math.sin(Rxy1)
                     MJ22=math.sin(Rxy2)
                     MJ33=math.sin(Rxy3)
                     MJ44=math.sin(Rxy4)
                     MJ55=math.sin(Rxy5)
                    
                     A=MJ1+MJ2+MJ3+MJ4+MJ5
                     B=MJ11+MJ22+MJ33+MJ44+MJ55
                     
                     total=math.sqrt((A*A)+(B*B))
                     T=np.absolute(total)
                    
                     antdi=((math.cos((math.pi/2)*math.cos(At)))/math.sin(At))
                     D=np.absolute(antdi)
                    
                     dipolos3=T*D
                     m3dipolo.append(dipolos3)
                     #print(m2dipolo)
                     def agregar_item():
                          todo_descripcion =  str(dipolos3)
                          archivo=open('seleccion3.txt','a')
                          archivo.write(todo_descripcion)
                          archivo.write("\n")
                          archivo.close()
                     creartxt()
                     agregar_item()
         
                     Af +=0.025
                 totaldipolocruzamineto3.append([m3dipolo]) 
                 totaldipolo2.append([m3dipolo])  
                 coordenadas.append([C])
                 C1 = " ".join(str(elemento) for elemento in C)
                 def agregar_item():
                      todo_descripcion =  str(C1)
                      archivo=open('cordenadas2.txt','a')
                      archivo.write(todo_descripcion)
                      archivo.write("\n")
                      archivo.close()
                 creartxt()
                 agregar_item()
    
   
   
   
def creartxt():
      archivo=open('segundonum2.txt','a')
      archivo.close()     
remove('segundonum2.txt')
numlistas=(len(totaldipolo2))
for q in range(numlistas):
    w=totaldipolo2[q]
    a = str(w)[1:-1]
    a=literal_eval(a)
    s=sorted(a)[-2]
    
    def agregar_item():
        todo_descripcion =  str(s)
        archivo=open('segundonum2.txt','a')
        archivo.write(todo_descripcion)
        archivo.write("\n")
        archivo.close()
    creartxt()
    agregar_item()   
with open('segundonum.txt', 'r') as archivo1, open('cordenadas.txt', 'r') as archivo2, open('combinado1.txt', 'w') as combinado:
    while True:
        linea1 = archivo1.readline()
        linea2 = archivo2.readline()
        if not linea1 and not linea2:
            break
        combinado.write(linea1.strip()+" "+ linea2.strip() + '\n')
archivo1.close()
archivo2.close()
combinado.close()
with open('segundonum2.txt', 'r') as archivo1, open('cordenadas2.txt', 'r') as archivo2, open('combinado2.txt', 'w') as combinado:
    while True:
        linea1 = archivo1.readline()
        linea2 = archivo2.readline()
        if not linea1 and not linea2:
            break
        combinado.write(linea1.strip()+" "+ linea2.strip() + '\n')
archivo1.close()
archivo2.close()
combinado.close()
with open('combinado1.txt', 'r') as archivo1, open('combinado2.txt', 'r') as archivo2, open('combinado3.txt', 'w') as combinado:
    contenido1 = archivo1.read()
    combinado.write(contenido1)
    contenido2 = archivo2.read()
    combinado.write(contenido2)
archivo1.close()
archivo2.close()
combinado.close()
with open("combinado3.txt", "r") as archivo:
    lineas = archivo.readlines()
lineas_ordenadas = sorted(lineas, key=lambda x: float(x.split()[0]))
with open("datos_ordenados.txt", "w") as archivo_ordenado:
    archivo_ordenado.writelines(lineas_ordenadas)
with open('datos_ordenados.txt', 'r') as f:
    lineas = f.readlines()[:rango0]
with open('nuevo_archivo.txt','w') as f:
    for linea in lineas:
        f.write(linea)    


while contador < repeticiones:
    with open('nuevo_archivo.txt','r') as archivo,open('primeraslineas.txt','a')as f4:
        filas=archivo.readlines()
        f4.write(filas[0]+'\n')
        for i in range(rango0):
             with open('1234.txt', "r") as archivo:
                 lineas = archivo.readlines()
                 indices_aleatorios = random.sample(range(len(lineas)), 2)
             
                 linea1ciclo = lineas[indices_aleatorios[0]].strip().split()
                 linea2ciclo = lineas[indices_aleatorios[1]].strip().split()

                 a = [float(num) for num in linea1ciclo]
                 b = [float(num) for num in linea2ciclo]
                 #print(a) 
                 #print(b)
                 Mcruzamientociclo=[
                                   [a[1],b[2],a[3],b[4],a[5],a[6],b[7],a[8],b[9],a[10]],
                                   [b[1],a[2],b[3],a[4],b[5],b[6],a[7],b[8],a[9],b[10]],
                                   [b[1],b[2],a[3],b[4],a[5],b[6],b[7],a[8],b[9],a[10]],
                                   [a[1],a[2],b[3],a[4],b[5],a[6],a[7],b[8],a[9],b[10]],
                                   [b[1],b[2],b[3],a[4],a[5],b[6],b[7],b[8],a[9],a[10]],
                                   [a[1],a[2],a[3],b[4],b[5],a[6],a[7],a[8],b[9],b[10]],
                                   [a[1],a[2],b[3],b[4],b[5],a[6],a[7],b[8],b[9],b[10]],
                                   [b[1],b[2],a[3],a[4],a[5],b[6],b[7],a[8],a[9],a[10]],
                                   [a[1],b[2],a[3],b[4],b[5],a[6],b[7],a[8],b[9],b[10]],
                                   [b[1],a[2],b[3],a[4],a[5],b[6],a[7],b[8],a[9],a[10]]
                                   ]
                 cruzamiento =0
                 C=[]
                 k=[]
                 def creartxt():
                    archivo=open('seleccion2ciclo.txt','a')
                    archivo.close()   
                    archivo=open('seleccion3ciclo.txt','a')
                    archivo.close() 
                    archivo=open('cordenadas2ciclo.txt','a')
                    archivo.close()     
             
                 for i in range(1):
                     Af=0
                     m2dipolociclo=[]
                     m3dipolociclo=[]
                     J=random.random()
                     L=random.random()
                     if J>0.9:
                        break
                     if (J>=0)and(J<=0.9): #Cruzamiento
                           cruzaminetociclo =1
                           C=(random.choice(Mcruzamientociclo))
                     #print(C,"correcto, combinacion  ")  
                     mutacionciclo=0
                     if (L>0.9)and(L<=1): #Mutacion
                          mutacionciclo=1
                          Mmutacionciclo=[
                                         [C[0]+0.1,C[1],C[2],C[3],C[4],C[5],C[6],C[7],C[8],C[9]],
                                         [C[0],C[1]+0.1,C[2],C[3],C[4],C[5],C[6],C[7],C[8],C[9]],
                                         [C[0],C[1],C[2]+0.1,C[3],C[4],C[5],C[6],C[7],C[8],C[9]],
                                         [C[0],C[1],C[2],C[3]+0.1,C[4],C[5],C[6],C[7],C[8],C[9]],
                                         [C[0],C[1],C[2],C[3],C[4]+0.1,C[5],C[6],C[7],C[8],C[9]],
                                         [C[0],C[1],C[2],C[3],C[4],C[5]+0.1,C[6],C[7],C[8],C[9]],
                                         [C[0],C[1],C[2],C[3],C[4],C[5],C[6]+0.1,C[7],C[8],C[9]],
                                         [C[0],C[1],C[2],C[3],C[4],C[5],C[6],C[7]+0.1,C[8],C[9]],
                                         [C[0],C[1],C[2],C[3],C[4],C[5],C[6],C[7],C[8]+0.1,C[9]],
                                         [C[0],C[1],C[2],C[3],C[4],C[5],C[6],C[7],C[8],C[9]+0.1],
                                         [C[0]-0.1,C[1],C[2],C[3],C[4],C[5],C[6],C[7],C[8],C[9]],
                                         [C[0],C[1]-0.1,C[2],C[3],C[4],C[5],C[6],C[7],C[8],C[9]],
                                         [C[0],C[1],C[2]-0.1,C[3],C[4],C[5],C[6],C[7],C[8],C[9]],
                                         [C[0],C[1],C[2],C[3]-0.1,C[4],C[5],C[6],C[7],C[8],C[9]],
                                         [C[0],C[1],C[2],C[3],C[4]-0.1,C[5],C[6],C[7],C[8],C[9]],
                                         [C[0],C[1],C[2],C[3],C[4],C[5]-0.1,C[6],C[7],C[8],C[9]],
                                         [C[0],C[1],C[2],C[3],C[4],C[5],C[6]-0.1,C[7],C[8],C[9]],
                                         [C[0],C[1],C[2],C[3],C[4],C[5],C[6],C[7]-0.1,C[8],C[9]],
                                         [C[0],C[1],C[2],C[3],C[4],C[5],C[6],C[7],C[8]-0.1,C[9]],
                                         [C[0],C[1],C[2],C[3],C[4],C[5],C[6],C[7],C[8],C[9]-0.1]
                                         ] 
                          k=(random.choice(Mmutacionciclo))
                        
                          if cruzaminetociclo==1:
                               #print("mutacion_ciclo")
                               x111=k[0]
                               x222=k[1]
                               x333=k[2]
                               x444=k[3]
                               x555=k[4]
                               y111=k[5]
                               y222=k[6]
                               y333=k[7]
                               y444=k[8]
                               y555=k[9]

                               while Af<=6.28319:
                                    Rx1=(Np*x111)*math.sin(At)*math.cos(Af)
                                    Rx2=(Np*x222)*math.sin(At)*math.cos(Af)
                                    Rx3=(Np*x333)*math.sin(At)*math.cos(Af)
                                    Rx4=(Np*x444)*math.sin(At)*math.cos(Af)
                                    Rx5=(Np*x555)*math.sin(At)*math.cos(Af)
                                
                                    Ry1=(Np*y111)*math.sin(At)*math.sin(Af)
                                    Ry2=(Np*y222)*math.sin(At)*math.sin(Af)
                                    Ry3=(Np*y333)*math.sin(At)*math.sin(Af)
                                    Ry4=(Np*y444)*math.sin(At)*math.sin(Af)
                                    Ry5=(Np*y555)*math.sin(At)*math.sin(Af)
                                
                                    Rxy1=Rx1+Ry1
                                    Rxy2=Rx2+Ry2
                                    Rxy3=Rx3+Ry3
                                    Rxy4=Rx4+Ry4
                                    Rxy5=Rx5+Ry5

                                    MJ1=math.cos(Rxy1)
                                    MJ2=math.cos(Rxy2)
                                    MJ3=math.cos(Rxy3)
                                    MJ4=math.cos(Rxy4)
                                    MJ5=math.cos(Rxy5)
                               
                                    MJ11=math.sin(Rxy1)
                                    MJ22=math.sin(Rxy2)
                                    MJ33=math.sin(Rxy3)
                                    MJ44=math.sin(Rxy4)
                                    MJ55=math.sin(Rxy5)
                               
                                    A=MJ1+MJ2+MJ3+MJ4+MJ5
                                    B=MJ11+MJ22+MJ33+MJ44+MJ55
                                
                                    total=math.sqrt((A*A)+(B*B))
                                    T=np.absolute(total)
                               
                                    antdi=((math.cos((math.pi/2)*math.cos(At)))/math.sin(At))
                                    D=np.absolute(antdi)
                               
                                    dipolos2=T*D
                                    m2dipolo.append(dipolos2)
                                #print(m2dipolo)
                                    def agregar_item():
                                        todo_descripcion =  str(dipolos2)
                                        archivo=open('seleccion2ciclo.txt','a')
                                        archivo.write(todo_descripcion)
                                        archivo.write("\n")
                                        archivo.close()
                                    creartxt()
                                    agregar_item()
                    
                                    Af +=0.025
                               totaldipolomutacion2.append([m2dipolo]) 
                               totaldipolo2.append([m2dipolo]) 
                               coordenadas.append([k])
                               k1 = " ".join(str(elemento) for elemento in k)
                               def agregar_item():
                                    todo_descripcion =  str(k1)
                                    archivo=open('cordenadas2ciclo.txt','a')
                                    archivo.write(todo_descripcion)
                                    archivo.write("\n")
                                    archivo.close()
                               creartxt()
                               agregar_item() 
              
                          if mutacionciclo==0:
                              #print("cruzamiento_ciclo")
                              x1111=C[0]
                              x2222=C[1]
                              x3333=C[2]
                              x4444=C[3]
                              x5555=C[4]
                              y1111=C[5]
                              y2222=C[6]
                              y3333=C[7]
                              y4444=C[8]
                              y5555=C[9] 

                              while Af<=6.28319:
                                   Rx1=(Np*x1111)*math.sin(At)*math.cos(Af)
                                   Rx2=(Np*x2222)*math.sin(At)*math.cos(Af)
                                   Rx3=(Np*x3333)*math.sin(At)*math.cos(Af)
                                   Rx4=(Np*x4444)*math.sin(At)*math.cos(Af)
                                   Rx5=(Np*x5555)*math.sin(At)*math.cos(Af)
                         
                                   Ry1=(Np*y1111)*math.sin(At)*math.sin(Af)
                                   Ry2=(Np*y2222)*math.sin(At)*math.sin(Af)
                                   Ry3=(Np*y3333)*math.sin(At)*math.sin(Af)
                                   Ry4=(Np*y4444)*math.sin(At)*math.sin(Af)
                                   Ry5=(Np*y5555)*math.sin(At)*math.sin(Af)
                         
                                   Rxy1=Rx1+Ry1
                                   Rxy2=Rx2+Ry2
                                   Rxy3=Rx3+Ry3
                                   Rxy4=Rx4+Ry4
                                   Rxy5=Rx5+Ry5

                                   MJ1=math.cos(Rxy1)
                                   MJ2=math.cos(Rxy2)
                                   MJ3=math.cos(Rxy3)
                                   MJ4=math.cos(Rxy4)
                                   MJ5=math.cos(Rxy5)
                        
                                   MJ11=math.sin(Rxy1)
                                   MJ22=math.sin(Rxy2)
                                   MJ33=math.sin(Rxy3)
                                   MJ44=math.sin(Rxy4)
                                   MJ55=math.sin(Rxy5)
                        
                                   A=MJ1+MJ2+MJ3+MJ4+MJ5
                                   B=MJ11+MJ22+MJ33+MJ44+MJ55
                         
                                   total=math.sqrt((A*A)+(B*B))
                                   T=np.absolute(total)
                        
                                   antdi=((math.cos((math.pi/2)*math.cos(At)))/math.sin(At))
                                   D=np.absolute(antdi)
                        
                                   dipolos3=T*D
                                   m3dipolociclo.append(dipolos3)
                         #print(m2dipolo)
                                   def agregar_item():
                                       todo_descripcion =  str(dipolos3)
                                       archivo=open('seleccion3ciclo.txt','a')
                                       archivo.write(todo_descripcion)
                                       archivo.write("\n")
                                       archivo.close()
                                   creartxt()
                                   agregar_item()
             
                                   Af +=0.025
                              totaldipolocruzamineto3.append([m3dipolociclo]) 
                              totaldipolo2.append([m3dipolociclo])  
                              coordenadas.append([C])
                              C1 = " ".join(str(elemento) for elemento in C)
                              def agregar_item():
                                  todo_descripcion =  str(C1)
                                  archivo=open('cordenadas2ciclo.txt','a')
                                  archivo.write(todo_descripcion)
                                  archivo.write("\n")
                                  archivo.close()
                              creartxt()
                              agregar_item()
        
       
       
       
    def creartxt():
          archivo=open('segundonum2ciclo.txt','a')
          archivo.close()     
    #remove('segundonum2ciclo.txt')
    numlistas=(len(totaldipolo2))
    for q in range(numlistas):
        w=totaldipolo2[q]
        a = str(w)[1:-1]
        a=literal_eval(a)
        s=sorted(a)[-2]
        def agregar_item():
           todo_descripcion =  str(s)
           archivo=open('segundonum2ciclo.txt','a')
           archivo.write(todo_descripcion)
           archivo.write("\n")
           archivo.close()
        creartxt()
        agregar_item()   
    with open('segundonum2ciclo.txt', 'r') as f1, open('cordenadas2ciclo.txt', 'r') as f2, open('combinado1.txt', 'w') as f3:
        for linea1, linea2 in zip(f1, f2):
            f3.write(linea1.strip() + ' ' + linea2.strip() + '\n')
    with open('nuevo_archivo.txt', 'r') as f1, open('combinado1.txt', 'r') as f2:
         contenido1 = f1.read()
         contenido2 = f2.read()
    with open('combinado3.txt', 'w') as nuevo_archivo:
         nuevo_archivo.write(contenido1)
         nuevo_archivo.write(contenido2)
    with open("combinado3.txt","r") as archivo:
        lineas = archivo.readlines()
        lineas_ordenadas = sorted(lineas, key=lambda x: float(x.split()[0]))
    with open("datos_ordenados.txt","w") as archivo_ordenado:
        archivo_ordenado.writelines(lineas_ordenadas)
    with open('datos_ordenados.txt','r') as f:
        lineas = f.readlines()[:rango0]
    with open('nuevo_archivo.txt','w') as f:
        for linea in lineas:
             f.write(linea)    
    
        
        
    contador += 1
    pbar.update(1)
pbar.close()
print("Tarea completa!")
