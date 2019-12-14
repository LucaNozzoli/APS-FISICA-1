import pygame
import random
import math


pygame.init()

RAIO = 32
MASSA = 1.0

N =  10#int(input("DIGITE O NUMERO DE BOLAS:"))
width = 800#int(input(("DIGITE A LARGURA DA JANELA")))
height = 600#int(input("DIGITE A ALTURA DA JANELA"))

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("APS BARRETO")

playerImg = pygame.image.load('bola.png')


x = [0]
y = [0]

while len(x) < N:
    aux = random.randint(64, width-64)
    for i in range(0, len(x)):
        if aux-x[i] >= 64 and aux not in x:
            x.append(aux)

while len(y) < N:
    aux = random.randint(64, height-64)
    for i in range(0, len(y)):
        if aux-y[i] >= 64 and aux not in y:
            y.append(aux)

print(x)
print(y)

vx = list(range(0, N))
vy = list(range(0, N))

for i in range(0, N):
    vx[i] = random.uniform(0.1, 1)
    vy[i] = random.uniform(0.1, 1)

cmx = list(range(0, N))
cmy = list(range(0, N))

def atualizacm():
    for i in range(0, N):
        cmx[i] = x[i] + 32
        cmy[i] = y[i] + 32


def player():
    for i in range(0, N):
        playerX = x[i]
        playerY = y[i]
        screen.blit(playerImg, (playerX, playerY))

def eixodecolisao(i, j):
    colisaox = cmx[i] - cmx[j]
    colisaoy = cmy[i] - cmy[j]
    colisao = pow(colisaox, 2.0) + pow(colisaoy, 2.0)

    vx1proj = ((vx[i] * colisaox) + (vy[i] * colisaoy)) * (colisaox/colisao)
    vy1proj = ((vx[i] * colisaox) + (vy[i] * colisaoy)) * (colisaoy/colisao)
    vx2proj = ((vx[j] * colisaox) + (vy[j] * colisaoy)) * (colisaox/colisao)
    vy2proj = ((vx[j] * colisaox) + (vy[j] * colisaoy)) * (colisaoy/colisao)

    vx[i] -= vx1proj - vx2proj
    vy[i] -= vy1proj - vy2proj
    vx[j] -= vx2proj - vx1proj
    vy[j] -= vy2proj - vy1proj

    if colisaox != 0 and colisaoy !=0:
        x[i] += colisaox / abs(colisaox)
        y[i] += colisaoy / abs(colisaoy)

        x[j] -= colisaox / abs(colisaox)
        y[j] -= colisaoy / abs(colisaoy)

def atualizaposicao():
    for i in range(0, N):
        x[i] += vx[i]
        y[i] += vy[i]

def velocidade():
    for i in range(0, N):
        for j in range(i+1,N):
            x = cmx[i] - cmx[j]
            y = cmy[i] - cmy[j]
            dist_centros = pow(x, 2.0) + pow(y, 2.0)

            if dist_centros <= (pow(RAIO, 2.0)*4):
                eixodecolisao(i, j)

def colisaoparede():
    for i in range(0, N):
        if x[i]+64 >= width:
            vx[i] *= -1
        elif x[i] <=0:
            vx[i] *= -1
        if y[i]+64 >= height:
            vy[i] *= -1
        elif y[i] <=0:
            vy[i] *= -1

def constantes():
    momentolin = 0
    energiak = 0
    for i in range(0, N):
        V = pow(vx[i], 2.0) + pow(vy[i], 2.0) #v^2
        energiak = energiak + ((MASSA * V)/2.0)
        momentolin = momentolin + (MASSA * math.sqrt(V) )
    print(f"ENERGIA CINETICA ={energiak}")
    print(f"MOMENTO LINEAR ={momentolin}")






running = True
while running:
    screen.fill((80, 255, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    atualizacm()

    player()

    atualizaposicao()

    colisaoparede()

    velocidade()



    constantes()

    #pygame.time.delay(100)

    pygame.display.update()