import os
import customtkinter
from PIL import Image


class HomeFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        images_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../images")
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(images_path, "image_icon_light.png")), size=(20, 20))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(images_path, "large_test_image.png")), size=(500, 150))

        self.home_label = customtkinter.CTkLabel(self, text="", image=self.large_test_image)
        self.home_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(self, text="", image=self.image_icon_image)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(self, text="CTkButton", image=self.image_icon_image, compound="right")
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_button_3 = customtkinter.CTkButton(self, text="CTkButton", image=self.image_icon_image, compound="top")
        self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.home_frame_button_4 = customtkinter.CTkButton(self, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)


class SecondFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.title = customtkinter.CTkLabel(self, text="SecondFrame")
        self.title.grid(row=0, column=0, padx=20, pady=10)


class ThirdFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.title = customtkinter.CTkLabel(self, text="ThirdFrame")
        self.title.grid(row=0, column=0, padx=20, pady=10)
