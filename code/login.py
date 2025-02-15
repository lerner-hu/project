from customtkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from login_trp import trp
from AB_dashboard import PPT



class register():
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Progress Tracker")
        self.root.geometry("1200x600+230+90")
        self.root.resizable(False, False)
        set_appearance_mode("light")

        self.new_win = None
        
        #self.root.attributes("-topmost",True)
        #self.root.focus_force()

     #----------------------------title---------------------------------------------------------
        

 #----------------------------BACKGROUNG IMAGE---------------------------------------------------------
        
        self.bg_img = Image.open("images/13.jpg")
        self.bg_img = self.bg_img.resize((1500,750 ), Image.LANCZOS)
        self.bg_img= ImageTk.PhotoImage(self.bg_img)
        bg_label=tk.Label(self.root, image=self.bg_img)
        bg_label.place(x=-2, y=-2)

        self.root.bind("<Unmap>", self.minimize_child_window)
        self.root.bind("<Map>", self.restore_child_window)
        

        self.add_reg()

    
        
    def add_reg(self):
        
        self.new_win=CTkToplevel(self.root)
        
        self.new_win.overrideredirect(True)
        self.new_obj=trp(self.new_win)
        self.new_win.focus_force()
        self.new_win.attributes("-topmost",True)

    def minimize_child_window(self, event=None):
        """Minimize the child window when the main window is minimized."""
        if self.new_win is not None:
            self.new_win.withdraw()  # Minimize the child window (hide it)

    def restore_child_window(self, event=None):
        """Restore the child window when the main window is restored."""
        if self.new_win is not None:
            self.new_win.deiconify()

    
        

if __name__ == "__main__":
    root = CTk()
    obj = register(root)
    root.mainloop()