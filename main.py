import customtkinter as ctk
from tkinter import ttk
from image_widgets import Button_frame, ImageOutput, CloseOutput
from PIL import Image, ImageTk
from menu import Menu

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

        SizeGrep(self)
        self.image_import = Button_frame(self, self.import_image)

        self.bind("<KeyPress>", lambda event : self.quit())

        self.mainloop()

    def import_image(self, path):
        self.image = Image.open(path)
        # self.image.show()
        self.image_ratio = self.image.size[0] / self.image.size[1]

        self.image_tk = ImageTk.PhotoImage(self.image)
        self.image_import.grid_forget()
        self.image_output = ImageOutput(self, self.resize_image)
        self.close_button = CloseOutput(self, self.close_edit)
        self.appmenu = Menu(self)
        

        print(path)

    def resize_image(self, event):
        # print(event)
        # current canvas ratio
        canvas_ratio = event.width / event.height

        # resize
        if canvas_ratio > self.image_ratio:
            image_height = int(event.height)
            image_width = int(image_height * self.image_ratio)

        else:
            image_width = int(event.width)
            image_height = int(image_width / self.image_ratio)

        # resized image

        self.image_output.delete("all")
        resized_image = self.image.resize((image_width, image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.image_output.create_image(event.width / 2 , event.height / 2 , image = self.image_tk)

    def close_edit(self):
        self.image_output.grid_forget()
        self.close_button.place_forget()
        self.appmenu.grid_forget()
        
        self.image_import = Button_frame(self, self.import_image)


if __name__ ==  "__main__":
    Window()
