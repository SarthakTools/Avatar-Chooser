import customtkinter as ct
from tkinter import X, TOP, LEFT, RIGHT, BOTTOM
import os
from PIL import Image

ct.set_appearance_mode("dark")

profile_window = ct.CTk(fg_color="black")
profile_window.title("Select your avator for profile")
profile_window.geometry("750x450")
profile_window.resizable(False, False)
profile_window.attributes("-topmost", True)
profile_window.grab_set()

# List of avator images
avator_images = []
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "avator")

for i in range(1, 17):
    avator_images.append(ct.CTkImage(Image.open(os.path.join(image_path, f"avator{i}.png")), size=(200, 200)))

current_avator_index = 0

def select_avator():
    avator.configure(fg_color="#222", hover_color="#222")
    image = f"avator{current_avator_index+1}.png"
    print(image)

def change_avator_right():
    avator.configure(fg_color="transparent", hover_color="black")
    global current_avator_index
    current_avator_index = (current_avator_index + 1) % len(avator_images)
    avator.configure(image=avator_images[current_avator_index])

def change_avator_left():
    avator.configure(fg_color="transparent", hover_color="black")
    global current_avator_index
    current_avator_index = (current_avator_index - 1) % len(avator_images)
    avator.configure(image=avator_images[current_avator_index])

avator_frame = ct.CTkFrame(profile_window, fg_color="transparent")
ct.CTkLabel(avator_frame, text="Select your Avator", font=("Canbera", 45, "bold"), text_color="white").pack(side=TOP, fill=X, anchor="nw", padx=0, pady=10)

avator1 = avator_images[0]
avator2 = avator_images[1]
avator3 = avator_images[2]
avator4 = avator_images[3]
avator5 = avator_images[4]
avator6 = avator_images[5]
avator7 = avator_images[6]

icon_right = ct.CTkImage(Image.open(os.path.join(image_path, "right.png")), size=(50, 50))
icon_left = ct.CTkImage(Image.open(os.path.join(image_path, "left.png")), size=(50, 50))

ct.CTkButton(avator_frame, text="", image=icon_left, fg_color="transparent", width=0, hover_color="#222", command=change_avator_left).pack(side=LEFT, padx=5)
avator = ct.CTkButton(avator_frame, text="", image=avator1, width=1, height=1, fg_color="transparent", hover_color="#000", corner_radius=50)
avator.pack(side=LEFT, anchor="center", padx=120)
ct.CTkButton(avator_frame, text="", image=icon_right, fg_color="transparent", width=0, hover_color="#222", command=change_avator_right).pack(side=RIGHT, padx=5)

ct.CTkButton(profile_window, text="Select", font=("monospace", 25, "bold"), height=50, width=150, command=select_avator).pack(side=BOTTOM, anchor="center", pady=20)

avator_frame.pack(side=TOP, fill=X, padx=80, pady=40, ipadx=50, ipady=20)

profile_window.mainloop()
