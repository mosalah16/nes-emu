from memory import ppumemory
from registers import ppuregisters
import pygame

class ppu:
    def __init__(self) -> None:
        self.memory = ppumemory()
        self.registers = ppuregisters()

        # timing
        self.scanline = 0 # 0 to 261 
        self.cycle = 0 # 0 to 340

        # framebuffer
        self.framebuffer = [[0 for _ in range(256)] for _ in range(240)]

    
    ### figuring out how to render with chatgpt
    def render_frame(self):
    
        # Fill the framebuffer with a checkerboard pattern
        for y in range(240):
            for x in range(256):
                # Alternate between black and white pixels
                color = 255 if (x // 8 + y // 8) % 2 == 0 else 0
                self.framebuffer[y][x] = color

        # Initialize Pygame
        pygame.init()
        screen = pygame.display.set_mode((256, 240))
        pygame.display.set_caption("NES PPU Test Renderer")

        # Convert the framebuffer to a Pygame surface
        surface = pygame.Surface((256, 240))
        for y in range(240):
            for x in range(256):
                color = self.framebuffer[y][x]
                surface.set_at((x, y), (color, color, color))  # Grayscale color

        # Display the surface
        screen.blit(surface, (0, 0))
        pygame.display.flip()

        # Wait for the user to close the window
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()