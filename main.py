import pygame
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="lolomax",
    database="store"
)

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tableau de bord de gestion des stocks")

data = pd.DataFrame({
    'Nom': ['Diamant', 'Saphir', 'Rubis'],
    'Quantité': [10, 15, 8],
    'Prix': [5000, 3000, 2500]
})

font = pygame.font.Font(None, 32)

def draw_text(text, color, x, y):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

def add_product():
    #  ajouter un produit à la base de données
    pass

def delete_product():
    #  supprimer un produit de la base de données
    pass

def edit_product():
    # modifier un produit dans la base de données
    pass

# Boucle principale
running = True

while running:
    screen.fill(WHITE)
    draw_text("Tableau de bord de gestion des stocks", BLACK, 20, 20)

    draw_text("Liste des produits en stock :", BLACK, 20, 60)
    for i, row in data.iterrows():
        draw_text(f"{row['Nom']}: Quantité - {row['Quantité']}, Prix - {row['Prix']}", BLACK, 20, 100 + i * 40)

    #  les boutons
    pygame.draw.rect(screen, GRAY, (20, 350, 150, 50))  # Bouton Ajouter
    draw_text("Ajouter", BLACK, 40, 360)

    pygame.draw.rect(screen, GRAY, (200, 350, 150, 50))  # Bouton Supprimer
    draw_text("Supprimer", BLACK, 220, 360)

    pygame.draw.rect(screen, GRAY, (380, 350, 150, 50))  # Bouton Modifier
    draw_text("Modifier", BLACK, 400, 360)

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #  la souris
            x, y = pygame.mouse.get_pos()
            #  les boutons ont été cliquer
            if 20 <= x <= 170 and 350 <= y <= 400: 
                add_product()
            elif 200 <= x <= 350 and 350 <= y <= 400:  
                delete_product()
            elif 380 <= x <= 530 and 350 <= y <= 400: 
                edit_product()

    pygame.display.flip()

conn.close()
pygame.quit()