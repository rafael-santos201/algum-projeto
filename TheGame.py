import pygame


#Objetos 
class Celulas():
    def __init__(self, life):
        self.life = True
    
    def Die(self):
        self.life = False; 

class Tabuleiro():
    def __init__(self):
        self.Matriz = [ [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0] ]
                
    
    def AdicionarCelula(self, initX, initY, Celula:Celulas):
        self.Matriz[initX][initY] = Celula
    

    def Rodada(Celula: Celulas, Redor: int):
        if Redor >= 3 and Redor <= 4:
            print("Viva")
        else:
            Celula.Die()
            print("Morta")

#Configuração da parte visual
x = 300
y = 500

janela = pygame.display.set_mode((x,y)) 
pygame.display.set_caption("The Game Of Life")


janela_aberta = True

while janela_aberta:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            janela_aberta = False
        else:
            pygame.draw.circle(janela,(124,255,134),(200,100),300) #teste visual, Dividir tela em matriz
            pygame.display.update()
            Jogo = Tabuleiro()
            a = Celulas(True)
            b = Celulas(True)
            Jogo.AdicionarCelula(1,1,a)
            Jogo.AdicionarCelula(1,2,b)


pygame.quit()