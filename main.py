import pgzrun
import pygame
import coin


try:
    icon = pygame.image.load("pgz_data/icon.png")
    pygame.display.set_icon(icon)
except Exception as e:
    print(f"Failed to set icon: {e}")

pgzrun.go()
