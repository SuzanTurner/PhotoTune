import customtkinter as ctk
from tkinter import ttk
from tkinter import filedialog, Canvas
from PIL import Image, ImageTk
from settings import *

class Button_frame(ctk.CTkFrame):
    def __init__(self, parent, import_func):
        super().__init__(parent)

        self.import_fun = import_func 

        self.button()
        self.grid(row = 0, column = 0, columnspan = 2, sticky = "nsew")

    def open_dialog(self):
        path = filedialog.askopenfile().name
        self.import_fun(path)

    def button(self, ):
        import_button = ctk.CTkButton(self, text = "Import", command = self.open_dialog)
        import_button.pack(expand = True)

class ImageOutput(Canvas):
    def __init__(self, parent, resize_image):
        super().__init__(parent, background= "#242424", bd = 0, highlightthickness= 0 , relief= "ridge")

        self.bind("<Configure>", resize_image)

        self.grid(row = 0, column= 1, sticky= "news", padx = 10, pady = 10)

class CloseOutput(ctk.CTkButton):
    def __init__(self, parent, close_func):
        super().__init__(parent, 
                         command = close_func,
                         text = "X", width = 40, height = 40, fg_color= "transparent", text_color= WHITE, corner_radius= 10, hover_color= CLOSE_RED)
        self.place(relx = 0.99, rely = 0.01, anchor = "ne")
    