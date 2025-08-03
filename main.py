import customtkinter as ctk
from tkinter import ttk
from image_widgets import Button_frame, ImageOutput, CloseOutput
from PIL import Image, ImageTk, ImageOps, ImageEnhance, ImageFilter
from menu import Menu
from settings import *

class SizeGrep(ttk.Sizegrip):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row = 1, column = 1, sticky = "se")

class Window(ctk.CTk):
    def __init__(self):

        super().__init__()
        ctk.set_appearance_mode("dark")
        self.geometry("900x500")
        self.title("PhotoTune")

        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 2, uniform = "a")
        self.columnconfigure(1, weight = 6, uniform = "a")

        # canvas data
        self.image_width = 0
        self.image_height = 0
        self.canvas_width = 0
        self.canvas_width = 0

        self.init_parameters()

        SizeGrep(self)

        self.image_import = Button_frame(self, self.import_image)

        self.bind("<KeyPress>", lambda event : self.quit())

        self.mainloop()
    
    def init_parameters(self):
        self.pos_vars = {
            'rotate' : ctk.DoubleVar(value = ROTATE_DEFAULT),
            'zoom' : ctk.DoubleVar(value = ZOOM_DEFAULT),
            'flip' : ctk.StringVar(value = FLIP_OPTIONS[0]),
        }

        # self.rotate_float = ctk.DoubleVar(value = ROTATE_DEFAULT)
        # self.rotate_float.trace('w', self.manipulate_image)

        # self.zoom_float = ctk.DoubleVar(value = ZOOM_DEFAULT)
        # self.zoom_float.trace('w', self.manipulate_image)

        self.color_vars = {
            'brightness' : ctk.DoubleVar(value = BRIGHTNESS_DEFAULT),
            'grayscale' : ctk.BooleanVar(value = GRAYSCALE_DEFAULT),
            'invert' : ctk.BooleanVar(value = INVERT_DEFAULT),
            'vibrance' : ctk.DoubleVar(value = VIBRANCE_DEFAULT),
        }

        self.effect_vars = {
            'blur' : ctk.DoubleVar(value= BLUR_DEFAULT) ,
            'contrast' : ctk.IntVar(value = CONTRAST_DEFAULT),
            'effect' : ctk.StringVar(value = EFFECT_OPTIONS[0]),
        }

        # tracing
        combined_tracing = list(self.pos_vars.values()) + list(self.color_vars.values()) + list(self.effect_vars.values())
        for var in combined_tracing:
            var.trace('w', self.manipulate_image)

    def manipulate_image(self, *args):
        self.image = self.original

        # Rotate
        self.image = self.image.rotate(self.pos_vars['rotate'].get())

        #Zoom
        self.image = ImageOps.crop(image = self.image, border = self.pos_vars['zoom'].get())

        # Flip
        if self.pos_vars['flip'].get() == 'X':
            self.image = ImageOps.mirror(self.image)
        if self.pos_vars['flip'].get() == 'Y':
            self.image = ImageOps.flip(self.image)
        if self.pos_vars['flip'].get() == 'Both':
            self.image = ImageOps.mirror(self.image)
            self.image = ImageOps.flip(self.image)

        # Brightness and vibrance
        brightness_enhancer = ImageEnhance.Brightness(self.image)
        self.image = brightness_enhancer.enhance(self.color_vars["brightness"].get())

        vibrance_enhancer = ImageEnhance.Color(self.image)
        self.image = vibrance_enhancer.enhance(self.color_vars["vibrance"].get())

        # grayscale and invert
        if self.color_vars["grayscale"].get():
            self.image = ImageOps.grayscale(self.image)
        if self.color_vars["invert"].get():
            if self.image.mode == "RGBA":
                # Split image into RGB and Alpha
                r, g, b, a = self.image.split()
                # Merge inverted RGB with original alpha
                rgb_image = Image.merge("RGB", (r, g, b))
                inverted_image = ImageOps.invert(rgb_image)
                r2, g2, b2 = inverted_image.split()
                self.image = Image.merge("RGBA", (r2, g2, b2, a))
            else:
                self.image = ImageOps.invert(self.image)
                

        self.place_image()

    def import_image(self, path):
        self.original = Image.open(path)
        self.image = self.original
        # self.image.show()
        self.image_ratio = self.image.size[0] / self.image.size[1]

        self.image_tk = ImageTk.PhotoImage(self.image)
        self.image_import.grid_forget()
        self.image_output = ImageOutput(self, self.resize_image)
        self.close_button = CloseOutput(self, self.close_edit)
        self.appmenu = Menu(self, self.pos_vars, self.color_vars, self.effect_vars)
        

        print(path)

    def resize_image(self, event):
        # print(event)
        # current canvas ratio
        canvas_ratio = event.width / event.height

        # canvas data
        self.canvas_width = event.width
        self.canvas_height = event.height

        # resize
        if canvas_ratio > self.image_ratio:
            self.image_height = int(event.height)
            self.image_width = int(self.image_height * self.image_ratio)

        else:
            self.image_width = int(event.width)
            self.image_height = int(self.image_width / self.image_ratio)

        self.place_image()

        # resized image
        
    def place_image(self):
        self.image_output.delete("all")
        resized_image = self.image.resize((self.image_width, self.image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.image_output.create_image(self.canvas_width / 2 , self.canvas_height / 2 , image = self.image_tk)

    def close_edit(self):
        self.image_output.grid_forget()
        self.close_button.place_forget()
        self.appmenu.grid_forget()
        
        self.image_import = Button_frame(self, self.import_image)


if __name__ ==  "__main__":
    Window()
