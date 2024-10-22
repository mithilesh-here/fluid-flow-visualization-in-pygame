# -*- coding: utf-8 -*-
"""boundary.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_KWaC6Rk6lsk1jFAWYFrhMke-9YIeqgl
"""

#boundary.py
import pygame

class Boundary:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def handle_collisions(self, particle):
        if self.rect.colliderect(particle.position):
            particle.velocity *= -1  # Simple reflection for now