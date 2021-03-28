"""
Here we will create a GUI which will work to edit the image
Author : Shobhit Mishra
"""

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as msg
import os
from PIL import Image, ImageTk
from image_process import image_processor


class editor_interface:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = None
        self.status_var = None
        self.file_name = None
        self.pro_img = False
        self.img_slot = None

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

        def button_pressed(e):

            convertor = image_processor.image_convertor(self.file_name)

            if e.widget.cget('text') == 'Gray shade':
                img = convertor.color_to_gray()
                self.img_slot = img

                img = Image.fromarray(img)

                Label(f2, text='Processed Image').grid(row=0, column=1)

                lb = Label(f2)
                image = ImageTk.PhotoImage(img)
                lb['image'] = image
                lb.image = image
                lb.grid(row=1, column=1)
                self.pro_img = True

            elif e.widget.cget('text') == 'Red shade':
                img = convertor.color_to_red()
                self.img_slot = img

                img = Image.fromarray(img)

                Label(f2, text='Processed Image').grid(row=0, column=1)

                lb = Label(f2)
                image = ImageTk.PhotoImage(img)
                lb['image'] = image
                lb.image = image
                lb.grid(row=1, column=1)
                self.pro_img = True

            elif e.widget.cget('text') == 'Blue shade':
                img = convertor.color_to_blue()
                self.img_slot = img

                img = Image.fromarray(img)

                Label(f2, text='Processed Image').grid(row=0, column=1)

                lb = Label(f2)
                image = ImageTk.PhotoImage(img)
                lb['image'] = image
                lb.image = image
                lb.grid(row=1, column=1)
                self.pro_img = True

            elif e.widget.cget('text') == 'Green shade':
                img = convertor.color_to_green()
                self.img_slot = img

                img = Image.fromarray(img)

                Label(f2, text='Processed Image').grid(row=0, column=1)

                lb = Label(f2)
                image = ImageTk.PhotoImage(img)
                lb['image'] = image
                lb.image = image
                lb.grid(row=1, column=1)
                self.pro_img = True
            elif e.widget.cget('text') == 'Black shade':
                img = convertor.color_to_black()
                self.img_slot = img

                img = Image.fromarray(img)

                Label(f2, text='Processed Image').grid(row=0, column=1)

                lb = Label(f2)
                image = ImageTk.PhotoImage(img)
                lb['image'] = image
                lb.image = image
                lb.grid(row=1, column=1)
                self.pro_img = True

        # Fuctions for the submenues

        def openfile():
            self.file_name = filedialog.askopenfilename()

            img = Image.open(self.file_name)
            img = img.resize((500, 500), Image.ANTIALIAS)

            photo = ImageTk.PhotoImage(img)

            Label(f2, text="Original Image").grid(row=0, column=0, pady=4)

            lb = Label(f2, borderwidth=2, relief='sunken', bg='gray')
            lb['image'] = photo
            lb.image = photo
            lb.grid(row=1, column=0)

            self.status_var.set(f"Image: {os.path.basename(self.file_name)}")

            for i in range(len((lt_button))):
                lt_button[i]['state'] = 'normal'

        def savefile():
            if self.pro_img == False:
                msg.showerror(
                    "Error", 'First perform the operations on the image.')
            else:
                location = filedialog.asksaveasfile(defaultextension=".jpg", filetypes=[(
                    "jpg Image", "*.jpg"), ("png Image", "*.png"), ("jpeg Image", "*.jpeg")])
                img_saver = image_processor.save_file(image=self.img_slot,location=location)

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
            msg.showinfo('About application',
                         "It is a simple GUI to do image editing")

        # Menu of file
        menu_lb = ["Open image", "save as", "Exit"]
        menu_command = [openfile, savefile, Exit]
        nameofsubmenu = "File"
        func_for_submenu(menubar, menu_lb, menu_command, nameofsubmenu)

        # Menu of customization
        menu_lb = ["RGB color", "Merging images", "Crop", "Resizing"]
        menu_command = [RGB_color, merging_images, crop, resizing]
        nameofsubmenu = "Customization"
        func_for_submenu(menubar, menu_lb, menu_command, nameofsubmenu)

        # Menu of about
        menu_lb = ["About"]
        menu_command = [about]
        nameofsubmenu = "About us"
        func_for_submenu(menubar, menu_lb, menu_command, nameofsubmenu)

        # Variables for the buttons
        gray_button = None
        red_button = None
        blue_button = None
        green_button = None
        black_button = None

        # Lists for the buttons and texts in the buttons
        lt_button = [gray_button, red_button,
                     blue_button, green_button, black_button]
        lt_txt = ['Gray shade', 'Red shade',
                  'Blue shade', 'Green shade', 'Black shade']

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
            lt_button[i]['state'] = 'disabled'
            lt_button[i].bind('<Button-1>', button_pressed)

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
