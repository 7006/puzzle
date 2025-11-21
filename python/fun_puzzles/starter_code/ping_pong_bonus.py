import pygame
import sys
import math
import random

# Note: this starter code has been left vague and is more designed to give you
# an idea of how you could structure your own code... Although feel free to use
# it as starter code too!

pygame.init()


class StaticColour:
    pass


class ChangingColour:
    pass


class ColourPicker:
    pass


class Ball:
    pass


class Paddle:
    pass


class PingPong:

    # Set your constants here
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    FPS = 60
    # ...

    def __init__(self):
        # Create a window
        self.screen = pygame.display.set_mode(
            (PingPong.SCREEN_WIDTH, PingPong.SCREEN_HEIGHT),
            flags=pygame.SCALED,
            vsync=1,
        )
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Two-Player Ping Pong")

        pass

    def play(self):

        # Main game loop
        while True:

            # Handle any raised events
            for event in pygame.event.get():
                self.handle_event(event)

            pass

            # Update the screen
            self.draw()

    def draw(self):
        pass

        # Update the display
        pygame.display.update()
        self.clock.tick(PingPong.FPS)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        pass


if __name__ == "__main__":
    PingPong().play()
