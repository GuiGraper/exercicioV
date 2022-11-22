#Desenvolva os algoritmos de substituição de páginas FIFO, LFU LRU e NRU.

name = "exercicioV"
version = "0.1.0"
description = "Exercicio sobre os algoritmos FIFO, LFU, LRU E NRU"
authors = ["Guilherme Graper, Mateus Sauerbeck"]

f = [[1,12,10,20,1,1],[2,10,1,12,1,0],[3,11,2,21,1,0], [4,12,0,22,1,0]]


print(' Algoritmo FIFO\n')
#fifo na linha 14 e colocar o range pra prh carga
min = f[0][1]
s  = 0
for i in range(len(f)):
  j = f[i][1]
  if j < min:
    min = j
    s = f[i][0]
  i = i + 1


  #for i in range(len(f)):
#  j = f[1]
# if j < min:
#   min = j
# i = i + 1

# rascunho do range
print('O tempo da carga é:', min)
print('Frames Alocados:', s, '\n\n')

print(' ')
print(' Algoritmo LFU\n')

max = f[0][1]
p  = 0
for q in range(len(f)): #for q in range(len(   )):
  u = f[q][2]
  
  if u < max:
    max = u

   #p = f[1][q]

    p = f[q][0] #=q[0]
  q = q + 1
print('A quantidade de referencia é:', max)
print('Frames Alocados:', p, '\n\n')

print(' ')
print(' Algoritmo LRU\n')

m = f[0][1]
t  = 0
for h in range(len(f)):
  o = f[h][3]
  
  if o > m:
    m = o
    t = f[h][0]
  h = h + 1
print('O tempo da ultima referência é:', m)
print('Frames Alocados: ', t, '\n\n')

print(' ')
print(' Algoritmo NRU\n')

g = f[0][1]
l  = 0
for a in range(len(f)):
  v = f[a][4]
  n = f[a][5]
  
  if v == 0 and n == 0:
    l = f[a][0]
    break
  a = a + 1
  
for a in range(len(f)):
  v = f[a][4]
  n = f[a][5]
  
  if v == 1 and n == 0:
    l = f[a][0]
    break
  a = a + 1
print('BR:', v,'BM:', n ) #o br vai puxado
print('Frames Alocados:', l, '\n\n')




