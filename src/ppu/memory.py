class ppumemory:
    def __init__(self):
        #initialize VRAM
        self.vram = [0x00] * 0x4000
        
        #initialize palette RAM
        self.palette_ram = [0x00] * 0x20

        #initialize OAM ( Object Attribute Memory )
        self.oam = [0x00] * 0x100