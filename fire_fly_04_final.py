####### FIRE FLY 03 FINAL

####### ERGASIA SYGXRONISMOS  PYGOLAMPIDWN
####### KATHIGITIS : ANTONIOU
####### FOITITES : GEORGOULIS - KOFTEROU

####### 2i YLOPOIISI ALGORITHMOU SYGXRONISMOU

####### MODELO SYGXRONISMOU STON PIO GRIGORO
####### PYGOLAMPIDES SE PINAKA
####### GEITONIA EPIROIS AKTINAS 1-2-3
####### THESI METAVALOMENI

#######  VIVLIOTHIKES   ###########

import random
import numpy as np
import matplotlib
import matplotlib.pylab as pyl
import matplotlib.pyplot as plt
import matplotlib.axes as axes
import matplotlib.animation as anim

####### VOITHITIKES

####### EYRESI GEITONIAS STON PINAKA 
def foo(A,i,j,r):
    return A[max(i-r,0):max(i+r+1,0),max(j-r,0):max(j+r+1,0)]

def update(i):
    return [plt.imshow(Z[i],cmap='plasma',vmin=0,vmax=1)] 

#######  DILWSEIS PARAMETRWN   ##############

N=int(input('Dwse diastasi plythismou pygolampidwn NXN : ')) # MEGETHOS
Rmin,Rmax = 100,300  # RANGE PAYSEWN

neighbor=int(input('Dwste emveleia radar 1,2,3 : '))

######  ARXIKOS PINAKAS YSTERISEWN

x=[]
for i in range(N):
    x_temp=[]
    for j in range(N):
        x_temp.append(np.random.randint(Rmin,Rmax))
    x.append(x_temp)

x=np.array(x)

###### KYLIOMENOS SYGXRONISMOS
count=0
SUM=[]

while True :
    count+=1
    m=[]
    for i in range(N):
        m_temp=[]
        for j in range(N):
            temp=foo(x,i,j,neighbor).min()  # pinakas geitonias 
            m_temp.append(temp)             # minimum geitonias
        m.append(m_temp)

    m=np.array(m)

    maxm=m.max()
    print(count,m.max()-m.min())

    
###### EISODOS SIMATOS

    S=N*[N*[(maxm+1)*[0]]] # 3d array
    S=np.array(S)

    for i in range(N):
        for j in range(N):
            S[i][j][m[i,j]]=1

##### TELIKO SIMA APO OLI TI DIADIKASIA

    if count>1 :    # an yparxei idi o SUM
        SUM.append(S.T)
    else :          # tin prwti fora pou den yparxei o SUM ton dimiourgei
        SUM.append(S.T)

###### ELEGXOS ISSOROPIAS

    if (m==m[0]).all() :
        print('Epilthe sygxronismos se '+str(count)+' vimata')
        break
    
    x=m
    np.random.shuffle(x.flat)
    
imcount=0

Z=[]
im=[]

for p in range(len(SUM)):
    SUM[p].tolist()
    for t in range(len(SUM[p])):
        Z.append(SUM[p][t].tolist())
        imcount+=1

Z=np.array(Z)

j=0

fig=plt.figure('Pygolampides 03')

ani=anim.FuncAnimation(fig,update,frames=np.array(list(range(imcount))),interval=1,blit=True,repeat=False)
    
plt.show()


    


