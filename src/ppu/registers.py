class ppuregisters:
    def __init__(self):
         #PPUCTRL
        self.control = 0x00  #0x2000

        #PPUMASK
        self.mask = 0x00  #0x2001

        #PPUSTATUS
        self.status = 0x00  #0x2002

        #PPUSCROLL
        self.scroll = 0x00  #0x2005

        #PPUADDR
        self.address = 0x00  # 0x2006

        #PPUDATA
        self.data = 0x00  # 0x2007

# Register	Address	  Description
# PPUCTRL	0x2000	  Control register (Controls NMI, background/sprite rendering, and VRAM address increment)
# PPUMASK	0x2001	  Mask register (Controls background/sprite visibility, color emphasis, etc)
# PPUSTATUS	0x2002	  Status register (Contains flags like VBlank and sprite overflow)
# PPUSCROLL	0x2005	  Scroll register (Stores scroll values for background rendering)
# PPUADDR	0x2006	  Address register (Stores the current VRAM address)
# PPUDATA	0x2007	  Data register (Used to read/write VRAM data)

    # Internal state for scroll and address handling
        self.write_toggle = False  # toggle for PPUSCROLL and PPUADDR writes
        self.temp_address = 0x0000  # temporary address

    def read_status(self) -> int:
        value = self.status
        self.status &= 0x7F  # clear VBlank flag after reading
        self.write_toggle = False  # reset write toggle
        return value

    def write_control(self, value: int) -> None:
        self.control = value

    def write_mask(self, value: int) -> None:
        self.mask = value

    def write_scroll(self, value: int) -> None:
        if not self.write_toggle:
            # horizontal scroll
            self.scroll = (self.scroll & 0xFF00) | value
        else:
            # vertical scroll
            self.scroll = (self.scroll & 0x00FF) | (value << 8)
        self.write_toggle = not self.write_toggle

    def write_address(self, value: int) -> None:
        if not self.write_toggle:
            # high byte of address
            self.temp_address = (self.temp_address & 0x00FF) | (value << 8)
        else:
            # low byte of address
            self.temp_address = (self.temp_address & 0xFF00) | value
            self.address = self.temp_address
        self.write_toggle = not self.write_toggle

    def read_data(self, memory: 'ppumemory') -> int:
        value = memory.read_vram(self.address)
        self.address += 1 if (self.control & 0x04) == 0 else 32
        return value

    def write_data(self, value: int, memory: 'ppumemory') -> None:
        memory.write_vram(self.address, value)
        self.address += 1 if (self.control & 0x04) == 0 else 32 