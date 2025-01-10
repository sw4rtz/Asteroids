import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.get_init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = (0, 0, 0)
    time_clock = pygame.time.Clock()
    dt = 0

    updatable  = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers  = (updatable)

    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    
    asteroidFieldObj = AsteroidField()

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for updatables in updatable:
            updatables.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collision_detection(player):
                print("Game over!")
                return
        
        screen.fill(black)
        for drawables in drawable:
            drawables.draw(screen)
        
        pygame.display.flip()
        
        dt = time_clock.tick(60) / 1000


if __name__ == "__main__":
    main()