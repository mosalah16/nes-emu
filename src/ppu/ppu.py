from memory import ppumemory
from registers import ppuregisters
import pygame

class ppu:
    def __init__(self):
        self.memory = ppumemory()
        self.registers = ppuregisters()
        self.scanline = 0 # 0 to 261 
        self.cycle = 0 # 0 to 340