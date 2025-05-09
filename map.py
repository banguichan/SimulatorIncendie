import pygame 
import sys
import random


pygame.init()
screen = pygame.display.set_mode([500, 500])
running = True

# Fill the background with white outside the loop
screen.fill((255, 255, 255))
jaune=(200,0,0)
vert=(40,160,55)
blue = (0, 0, 255)
marron=(200,10,35)

rows = 500
cols = 500

weights = [0.5, 0.1, 0.1, 0.3]
# Générer la grille
ma_grille = [random.choices([1, 2, 3, 4], weights=weights, k=cols) for _ in range(rows)]




# Afficher la grille modifiée
print(ma_grille)



for i in range(500):
    for j in range(500):
        square_x = i
        square_y = j
        square_size = 1
        couleur=ma_grille[i][j]
        if couleur==1:   
            pygame.draw.rect(screen, vert, (square_x, square_y, square_size, square_size))
        elif couleur==2:
            pygame.draw.rect(screen, blue, (square_x, square_y, square_size, square_size))
        elif couleur==4:
            pygame.draw.rect(screen, marron, (square_x, square_y, square_size, square_size))
        else:
            pygame.draw.rect(screen, jaune, (square_x, square_y, square_size, square_size))


while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()