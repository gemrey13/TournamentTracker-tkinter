import customtkinter
from PIL import Image
import os
from adminUI.SidebarFrame import HomeFrame, SecondFrame, ThirdFrame


class AdminWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x600")
        self.title("Tournament Tracker | Admin")
        self.after(250, lambda: self.iconbitmap("./images/run.ico"))
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        images_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(images_path, "run.ico")), size=(26, 26))

        self.home_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(images_path, "home_dark.png")), dark_image=Image.open(os.path.join(images_path, "home_light.png")), size=(20, 20)
        )
        self.chat_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(images_path, "chat_dark.png")), dark_image=Image.open(os.path.join(images_path, "chat_light.png")), size=(20, 20)
        )
        self.add_user_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(images_path, "add_user_dark.png")), dark_image=Image.open(os.path.join(images_path, "add_user_light.png")), size=(20, 20)
        )

        self.navigation_frame_label = customtkinter.CTkLabel(
            self, text="  Image Example", image=self.logo_image, compound="left", font=customtkinter.CTkFont(size=15, weight="bold")
        )
        self.navigation_frame_label.grid(row=0, column=0, padx=10, pady=20)

        self.home_frame = HomeFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.second_frame = SecondFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame = ThirdFrame(self, corner_radius=0, fg_color="transparent")

        self.home_button = customtkinter.CTkButton(
            self,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Home",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.home_image,
            anchor="w",
            command=self.home_button_event,
        )
        self.home_button.grid(row=1, column=0, padx=20, pady=5, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(
            self,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Frame 2",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.chat_image,
            anchor="w",
            command=self.frame_2_button_event,
        )
        self.frame_2_button.grid(row=2, column=0, padx=20, pady=5, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(
            self,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Frame 3",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.add_user_image,
            anchor="w",
            command=self.frame_3_button_event,
        )
        self.frame_3_button.grid(row=3, column=0, padx=20, pady=5, sticky="ew")

        self.logout_brn = customtkinter.CTkButton(self, text="logout", command=self.logout)
        self.logout_brn.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self, values=["Dark", "Light", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=5, column=0, padx=20, pady=20, sticky="ew")

        self.select_frame_by_name("home")

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def logout(self):
        self.master.logout()
        self.destroy()

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


class TabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.add("Tournaments")
        self.add("Teams")

        self.label = customtkinter.CTkLabel(master=self.tab("Tournaments"), text="Hellow")
        self.label.place(relx=0.5, rely=0.4, anchor="c")
