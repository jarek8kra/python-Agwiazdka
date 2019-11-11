import math
n = 20
a = [["|"] * n for i in range(n)]
pa=5 #  wartość dla przeszkody
a[3][2]=pa# ręcznie wypisane przeszkody
a[3][3]=pa
a[3][4]=pa
a[3][5]=pa

a[6][8]=pa
a[7][8]=pa
a[8][8]=pa
a[9][8]=pa
a[10][8]=pa
a[11][8]=pa
a[12][8]=pa
a[13][8]=pa

a[7][10]=pa
a[8][10]=pa
a[9][10]=pa
a[10][10]=pa
a[11][10]=pa
a[12][10]=pa

a[16][12]=pa
a[17][12]=pa
a[18][12]=pa
a[19][12]=pa

a[16][16]=pa
a[16][17]=pa
a[16][18]=pa
a[16][19]=pa
# wypisanie siatki zerowej z przeszkodami
print("Grid + przeszkody:")
print("Oznaczenie: "+"Przeszkody - 5 | "+ "Początek - punkt(0,0) | "+" Koniec - punkt(19,19) | ")
for row in a:
    print(' '.join([str(elem) for elem in row]))
print("-----------------------------------------------------")

h = [[0] * n for i in range(n)]


t=33.3
p=88.8 # wartość dla przeszkody
h[0][0]=t # początek
h[19][19]=t # koniec
h[3][2]=p
h[3][3]=p
h[3][4]=p
h[3][5]=p


h[6][8]=p
h[7][8]=p
h[8][8]=p
h[9][8]=p
h[10][8]=p
h[11][8]=p
h[12][8]=p
h[13][8]=p

h[7][10]=p
h[8][10]=p
h[9][10]=p
h[10][10]=p
h[11][10]=p
h[12][10]=p

h[16][12]=p
h[17][12]=p
h[18][12]=p
h[19][12]=p


h[16][16]=p
h[16][17]=p
h[16][18]=p
h[16][19]=p


x=1 #do działania pętli while
z=1 # poziom zaokrąglania wyników
d=40 # wartość dodana dla wyrównania siatki(dlatego daje wszędzie wyniki dwycyfrowe)
#ustawienie d=0 daje własciwe wyniki pierwiastków
while x <999:    
    for i in range(n):
        for j in range(n):
             if i<19 and j <19 and i>=0 and j>=0 :
                if h[i+1][j]!=p and h[i+1][j]==0:# dolna
                    h[i+1][j]=x+(round(math.sqrt(math.pow((i+1)-19,2)+math.pow(j-19,2)),z))+d
                if h[i][j-1]!=p and h[i][j-1]==0 and j>=1:# lewa
                    h[i][j-1]=x+(round(math.sqrt(math.pow(i-19,2)+math.pow((j-1)-19,2)),z))+d
                if h[i-1][j]!=p and h[i-1][j]==0 and i>=1:# górna
                    h[i-1][j]=x+(round(math.sqrt(math.pow((i+1)-19,2)+math.pow(j-19,2)),z))+d
                if h[i][j+1]!=p and h[i][j+1]==0:# prawa
                    h[i][j+1]=x+(round(math.sqrt(math.pow(i-19,2)+math.pow((j+1)-19,2)),z))+d
    x+=1

# wypisanie grid z heurystyką(wyniki zwiększone o zmienną d)
print("Heurystyka + przeszkody:")
print("Oznaczenie: "+" początek - punkt (0,0) |  koniec - punkt (19,19) | "+"88.8 - przeszkody")
for row in h:
    print(' '.join([str(elem) for elem in row]))

print("-----------------------------------------------------")

#tworzenie gridu b i wyznaczanie drogi
b=h 

g=1
min=0
while g <999:    
    for i in range(n):
        for j in range(n):
             if i<19 and j<19 and i>=0 and j>=0 and b[i][j]==33.3:
                if b[i+1][j]<b[i][j+1]:# spr.czy dolna mniejsza od prawej
                    if b[i+1][j]!=p:
                        b[i+1][j]=33.3
                if b[i][j+1]<b[i+1][j]:#spr. czy prawa mniejsza od dolnej
                    if b[i][j+1]!=p:
                        b[i][j+1]=33.3
                if b[i][j+1]==b[i+1][j]:# spr. czy równe
                    if b[i+1][j]!=p:
                        b[i+1][j]=33.3     # wtedy dolna do zmiany
    g+=1


 #wypisanie b( gridu heurystyka+droga)
#for row in b:
#    print(' '.join([str(elem) for elem in row]))

#print("-----------------------------------------------------")






#grid r utworzony dla uzyskania przejrzystego wyniku, zastąpienie heurystyki znakiem |
r=b
y=1
while y <999:    
    for i in range(n):
        for j in range(n):
            if i<=19 and j <=19 and i>=0 and j>=0 :
                 if r[i][j]==88.8:
                     r[i][j]=5 # przeszkoda
                 elif r[i][j]==33.3:
                     r[i][j]=3 # droga
                 elif r[i][j]!=88.8 and r[i][j]!=33.3 and r[i][j]!=5 and r[i][j]!=3:
                     r[i][j]="|"# wolna przestrzeń
    y+=1
 #wypisanie r
for row in r:
    print(' '.join([str(elem) for elem in row]))

print("-----------------------------------------------------")









