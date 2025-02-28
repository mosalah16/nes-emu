class ppumemory:
    def __init__(self) -> None:
        #initialize VRAM
        self.vram = [0x00] * 0x4000 #16384 Bytes
        
        #initialize palette RAM
        self.palette_ram = [0x00] * 0x20 #256 Bytes

        #initialize OAM ( Object Attribute Memory )
        self.oam = [0x00] * 0x100 # 32 Bytes

    def read_vram(self, address: int) -> int:
        address &= 0x3FFF  # Mask to 14 bits ( 2^14 = 16384 )
        return self.vram[address]
    
    def write_vram(self, address: int, value: int) -> None:
        address &= 0x3FFF  # Mask to 14 bits
        self.vram[address] = value

    def read_palette_ram(self, address: int ) -> int:
        address &= 0x1F  # Mask to 5 bits
        return self.palette_ram[address]
    
    def write_palette_ram(self, address: int, value: int) -> None:
        address &= 0x1F  # Mask to 5 bits
        self.palette_ram[address] = value

    def read_oam(self, address: int) -> int:
        address &= 0xFF  # Mask to 8 bits
        return self.oam[address]
    
    def write_oam(self, address: int, value: int) -> None:
        address &= 0xFF  # Mask to 8 bits
        self.oam[address] = value