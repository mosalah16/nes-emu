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

#Register	Address	  Description
#PPUCTRL	0x2000	  Control register (Controls NMI, background/sprite rendering, and VRAM address increment)
#PPUMASK	0x2001	  Mask register (Controls background/sprite visibility, color emphasis, etc)
#PPUSTATUS	0x2002	  Status register (Contains flags like VBlank and sprite overflow)
#PPUSCROLL	0x2005	  Scroll register (Stores scroll values for background rendering)
#PPUADDR	0x2006	  Address register (Stores the current VRAM address)
#PPUDATA	0x2007	  Data register (Used to read/write VRAM data)