import customtkinter as ctk
from settings import SLIDER_BG, DARK_GREY

class Panel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color= DARK_GREY)
        self.pack(fill = "x", pady = 4, ipady = 8)

class SliderPanel(Panel):
    def __init__(self, parent, text, data_var, min_value, max_value):
        super().__init__(parent)

        self.rowconfigure((0,1), weight = 1)
        self.columnconfigure((0,1), weight = 1, )


        ctk.CTkLabel(self, text = text).grid(row = 0, column = 0, padx = 5, sticky = "w")

        self.num_label = ctk.CTkLabel(self, text = data_var.get())
        self.num_label.grid(row = 0, column = 1, padx = 5, sticky = "e")
        ctk.CTkSlider(self, 
                      fg_color= SLIDER_BG, 
                      from_ = min_value,
                      to = max_value,
                      command = self.update_text,
                      variable= data_var).grid(row = 1 , column = 0, columnspan = 2, sticky = "we", pady = 5, padx = 5)
        
    def update_text(self, value):
        self.num_label.configure(text = f"{round(value,2)}")