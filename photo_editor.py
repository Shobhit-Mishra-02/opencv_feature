"Here we will create a GUI which will work to edit the image"

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as msg
import os


class editor_interface:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = None
        self.status_var = None

    def start_interface(self):
        '''
        This method will create the main body of the interface.
        Here we will add buttons, image slot and status bar
        '''
        # Here I have started the main GUI
        self.root = Tk()
        self.root.geometry(f"{self.width}x{self.height}+0+0")
        self.root.title("Photo Editor")
        self.status_var = StringVar()

        self.status_var.set('Testing the interface....')

        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        # This function will create the title menu and the title of each sub_menu
        def func_for_submenu(menubar, menu_lb, menu_command, nameofsubmenu):
            m = Menu(menubar, tearoff=0)
            for i in range(len(menu_lb)):
                m.add_command(label=menu_lb[i], command=menu_command[i])
            menubar.add_cascade(label=nameofsubmenu, menu=m)

        def newfile():
            pass
        def openfile():
            pass
        def Exit():
            self.root.destroy()

        def RGB_color():
            pass
        def merging_images():
            pass
        def crop():
            pass
        def resizing():
            pass
        def about():
            pass

        menu_lb=["Open image", "save as", "Exit"]
        menu_command=[newfile, openfile, Exit]
        nameofsubmenu="File"
        func_for_submenu(menubar, menu_lb, menu_command, nameofsubmenu)
        
        menu_lb=["RGB color", "Merging images", "Crop", "Resizing"]
        menu_command=[RGB_color, merging_images, crop, resizing]
        nameofsubmenu="Customization"
        func_for_submenu(menubar, menu_lb, menu_command, nameofsubmenu)
        
        menu_lb=["About"]
        menu_command=[about]
        nameofsubmenu="About us"
        func_for_submenu(menubar, menu_lb, menu_command, nameofsubmenu)

        # Variables for the buttons
        gray_button = None
        red_button = None
        blue_button = None
        green_button = None

        # Lists for the buttons and texts in the buttons
        lt_button = [gray_button, red_button, blue_button, green_button]
        lt_txt = ['Gray shade', 'Red shade', 'Blue shade', 'Green shade']

        # Frame first which on the top of the window
        f1 = Frame(self.root)
        f1.pack(side=TOP, fill=X)

        # Control frame for the insertion of the buttons
        control_frame = ttk.LabelFrame(f1, text="Controls of colors")
        control_frame.pack(side=TOP, fill=X)

        # Applying for loop for the insertions of the buttons
        for i in range(len((lt_button))):
            lt_button[i] = ttk.Button(control_frame, text=lt_txt[i])
            lt_button[i].grid(row=0, column=i, pady=3, padx=4)

        # Second frame which is in the mid of the window
        f2 = Frame(self.root)
        f2.pack(side=TOP, fill=X)

        # Third frame which is in the bottom of the window
        f3 = Frame(self.root)
        f3.pack(side=BOTTOM, fill=X)

        status_bar = Label(f3, textvariable=self.status_var,
                           borderwidth=3, relief='raised', anchor='w')
        status_bar.pack(side=BOTTOM, fill=X)

    def End(self):
        self.root.mainloop()


if __name__ == "__main__":
    x = editor_interface(1005, 637)
    x.start_interface()
    x.End()
