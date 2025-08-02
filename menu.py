import customtkinter as ctk
from panel import Panel, SliderPanel

class Menu(ctk.CTkTabview):
    def __init__(self, parent, rotation, zoom):
        super().__init__(parent)
        self.grid(row = 0 , column = 0, sticky = "news", padx = 10, pady = 10)

        # tabs
        self.add("Position")
        self.add("Color")
        self.add("Effects")
        self.add("Export")

        PositionFrame(self.tab("Position"), rotation, zoom)
        ColorFrame(self.tab("Color"))
        EffectFrame(self.tab("Effects"))
        ExportFrame(self.tab("Export"))


class PositionFrame(ctk.CTkFrame):
    def __init__(self, parent, rotation, zoom):
        super().__init__(parent, fg_color= "transparent")
        self.pack(expand = True, fill = "both")
        # (self)
        SliderPanel(self, "Rotation", rotation, 0, 360)
        SliderPanel(self, "Zoom", zoom, 0, 200)

class ColorFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color= "transparent")
        self.pack(expand = True, fill = "both")

class EffectFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color= "transparent")
        self.pack(expand = True, fill = "both")

class ExportFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color= "transparent")
        self.pack(expand = True, fill = "both")
