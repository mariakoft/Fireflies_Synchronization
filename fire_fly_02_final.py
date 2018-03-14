####### FIRE FLY 02 FINAL

####### ERGASIA SYGXRONISMOS  PYGOLAMPIDWN
####### KATHIGITIS : ANTONIOU
####### FOITITES : GEORGOULIS - KOFTEROU

####### 1i YLOPOIISI ALGORITHMOU SYGXRONISMOU

####### MODELO SYGXRONISMOU STON PIO GRIGORO
####### PYGOLAMPIDES SE SEIRA
####### GEITONIA EPIROIS AKTINAS 1
####### THESI METAVALLOMENI

####### SYMPERASMA :    OTAN I THESI TWN PYGOLAMPIDWN ALLAZEI TOTE
#######                 ERXONTAI PIO SYNTOMA SE SYGXRONISMO.....

#######  VIVLIOTHIKES   ###########

import random
import numpy as np
import matplotlib
import matplotlib.pylab as pyl
import matplotlib.pyplot as plt
import matplotlib.animation as anim

####### VOITHITIKES

def Square(j):
    return SUM[0:N,(N*j):((N*j)+N)]

def updatefig(*args):
    global j
    j+=1
    im.set_array(Square(j))
    return im

#######  DILWSEIS PARAMETRWN   ##############

SUM=None

N=int(input('Dwse plythismo pygolampidwn : ')) # MEGETHOS

Rmin,Rmax = 750,950  # RANGE PAYSEWN

x,y = input('Dwse fasma ekpompis me komma , default(Rmin=750,Rmax=950 : ').split(',')
if x: Rmin=int(x)
if y: Rmax=int(y)

######  ARXIKI LISTA YSTERISEWN

x=[]
for i in range(N):
    x.append(np.random.randint(Rmin,Rmax))


###### KYLIOMENOS SYGXRONISMOS

count=0

while True:

    m=[]
    count+=1
    for i in range(N):
        #gia kyliomeni elaxisti fasi ana 3 (FIT STON GRIGORO)

        # an lamvanei ypopsi kai ton eayto tou tote thelw MO x[i-1],x[i],x[i+1]
        # an den lamvanei ypopsi ton eayto tou tote thelw MO x[i-1],x[i+1]
        
        if i>0 and i<(N-1):
            m.append(min(x[i-1],x[i],x[i+1]))
        elif i==0:
            m.append(min(x[0],x[1]))
        else : m.append(min(x[-2],x[-1]))

    maxm=max(m)  #megisti kathysterisi
    print(count,max(m)-min(m))

    ###### PINAKAS SIMATOS


    #orismos pinaka apotelesmatos me 0 kai 1 
    #diastaseis N*(megisti kathisterisi + 1 gia ti monada)
    S=N*[(maxm+1)*[0]]


    #metatropi toy S apo lista se pinaka
    S=np.asarray(S)

    for i in range(N):
        S[i][m[i]]=1        
    # vazw tous assous sto telos tis ysterisis kathe fly

    #elegxw an issoroppise o pinakas
    #if (S==S[0]).all() :
    #    print('Epilthe issoropia')



    ###### TELIKO SIMA  APO OLI TI DIADIKASIA


    # Sygkentrwtiki enwsi pinakwn SUM+=S

    if count>1 :     #an yparxei idi o SUM
        SUM=np.concatenate((SUM.T,S.T)).T
    else :      #tin prwti fora pou den yparxei o SUM ton ftiaxnei me ta analoga megethi
        SUM=S
        #SUM=np.array(N*[maxm*[0]])
        #SUM=np.concatenate((SUM.T,S.T)).T

    #elegxw an issoropisan oi meses times
    if m==N*[m[0]] :
        print('Epilthe sygxronismos se '+str(count)+' vimata gia '+str(N)+' pygolampides \n kai range apo :'+str(Rmin)+' ews :'+str(Rmax)+'  ')
        plus=N-len(SUM[0])%N
        K=np.array(plus*[N*[0]])
        SUM=np.concatenate((SUM.T,K)).T
        break

    x=m
    random.shuffle(x)  #### ANAKATEMA TIS THESIS TOY KATHENOS

j=0

fig=plt.figure('Pygolampides 01')

ax = plt.axes(xlim=(0, N-1), ylim=(0, N-1))

Z=[]
im=[]

k=int(np.ceil(len(SUM[0])/N))
for j in range(k):
    Z.append(Square(j).tolist())
    im.append([plt.imshow(Z[j],cmap='plasma',vmin=0,vmax=1)])
 
ani=anim.ArtistAnimation(fig, im, interval=40, blit=True, repeat=False)

plt.show()







