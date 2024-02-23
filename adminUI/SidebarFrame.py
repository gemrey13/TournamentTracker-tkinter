import os
import customtkinter
from PIL import Image


class Sidebar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        images_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(images_path, "run.ico")), size=(26, 26))

        self.logo_label = customtkinter.CTkLabel(
            self, image=self.logo_image, compound="left", text="  Tournament Tracker", font=customtkinter.CTkFont(size=15, weight="bold")
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=30)

        self.add_team_btn = customtkinter.CTkButton(self, text="Add Team", command=self.sidebar_button_event)
        self.add_team_btn.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.add_tournament_btn = customtkinter.CTkButton(self, text="Add Tournament", command=self.sidebar_button_event)
        self.add_tournament_btn.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.add_sport_btn = customtkinter.CTkButton(self, text="Add Sport", command=self.sidebar_button_event)
        self.add_sport_btn.grid(row=3, column=0, padx=20, pady=10)

        self.string_input_button = customtkinter.CTkButton(self, text="Open CTkInputDialog", command=self.open_input_dialog_event)
        self.string_input_button.grid(row=4, column=0, padx=20, pady=(10, 10))

        self.appearance_mode_label = customtkinter.CTkLabel(self, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.logout_btn = customtkinter.CTkButton(self, text="logout", command=self.logout)
        self.logout_btn.grid(row=7, column=0, padx=20, pady=20, sticky="ew")

    def logout(self):
        self.master.master.logout()
        self.master.destroy()

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def sidebar_button_event(self):
        print("sidebar_button click")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)


class HomeFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=50)
        images_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../images")
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(images_path, "image_icon_light.png")), size=(20, 20))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(images_path, "large_test_image.png")), size=(500, 150))

        self.add_team_btn = customtkinter.CTkButton(self, text="add team", compound="right")
        self.add_team_btn.grid(row=0, column=1)

        self.home_label = customtkinter.CTkLabel(self, text="", image=self.large_test_image)
        # self.home_label.grid(row=0, column=0, padx=20, pady=10)

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
