import customtkinter as ctk
from panel import Panel, SliderPanel, SegmentedPanel, SwitchPanel, DropDown, RevertButton, FileNamePanel
from settings import *

class Menu(ctk.CTkTabview):
    def __init__(self, parent, pos_vars, color_vars, effect_vars):
        super().__init__(parent)
        self.grid(row = 0 , column = 0, sticky = "news", padx = 10, pady = 10)

        # tabs
        self.add("Position")
        self.add("Color")
        self.add("Effects")
        self.add("Export")

        PositionFrame(self.tab("Position"), pos_vars)
        ColorFrame(self.tab("Color"), color_vars)
        EffectFrame(self.tab("Effects"), effect_vars)
        ExportFrame(self.tab("Export"))

class PositionFrame(ctk.CTkFrame):
    def __init__(self, parent, pos_vars):
        super().__init__(parent, fg_color= "transparent")
        self.pack(expand = True, fill = "both")
        # (self)
        SliderPanel(self, "Rotation", pos_vars['rotate'], 0, 360)
        SliderPanel(self, "Zoom", pos_vars['zoom'], 0, 200)
        SegmentedPanel(self, "Flip", pos_vars['flip'], FLIP_OPTIONS)
        RevertButton(self, 
                     (pos_vars["rotate"], ROTATE_DEFAULT),
                     (pos_vars["zoom"], ZOOM_DEFAULT),
                     (pos_vars["flip"], FLIP_OPTIONS[0])
                    )

class ColorFrame(ctk.CTkFrame):
    def __init__(self, parent, color_vars):
        super().__init__(parent, fg_color= "transparent")
        self.pack(expand = True, fill = "both")

        SwitchPanel(self, (color_vars["grayscale"], "B/W"), (color_vars["invert"], "Invert"))
        SliderPanel(self, "Brightness", color_vars['brightness'], 0, 10)
        SliderPanel(self, "Vibrance", color_vars['vibrance'], 0, 10)
        RevertButton(self, 
                     (color_vars["grayscale"], GRAYSCALE_DEFAULT),
                     (color_vars["brightness"], BRIGHTNESS_DEFAULT),
                     (color_vars["vibrance"], VIBRANCE_DEFAULT),
                     (color_vars["invert"], INVERT_DEFAULT),
                    )

class EffectFrame(ctk.CTkFrame):
    def __init__(self, parent, effect_vars):
        super().__init__(parent, fg_color= "transparent")
        self.pack(expand = True, fill = "both")

        DropDown(self, effect_vars["effect"], EFFECT_OPTIONS)
        SliderPanel(self, "Blur", effect_vars['blur'], 0, 10)
        SliderPanel(self, "Contrast", effect_vars['contrast'], 0, 10)
        RevertButton(self, 
                     (effect_vars["blur"], BLUR_DEFAULT),
                     (effect_vars["contrast"], CONTRAST_DEFAULT),
                     (effect_vars["effect"], EFFECT_OPTIONS[0]),
                    )

class ExportFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color= "transparent")
        self.pack(expand = True, fill = "both")

        self.name_string = ctk.StringVar()
        self.file_string = ctk.StringVar(value = "jpg")

        FileNamePanel(self, self.name_string, self.file_string)
