from typing import Tuple
import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.username = customtkinter.CTkEntry(self, placeholder_text="Username")
        self.username.place(relx=0.5, rely=0.4, anchor="c")

        self.password = customtkinter.CTkEntry(self, placeholder_text="Password")
        self.password.place(relx=0.5, rely=0.46, anchor="c")

        self.login_btn = customtkinter.CTkButton(self, text="login")
        self.login_btn.place(relx=0.5, rely=0.56, anchor="c")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Tournament Tracker")
        self.grid_columnconfigure(0, weight=1)
        self.iconbitmap("./images/run.ico")
        self.resizable(False, False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.login_frame = LoginFrame(master=self)
        self.login_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.img_background = customtkinter.CTkImage(light_image=Image.open("./images/background.jpg"), dark_image=Image.open("./images/background.jpg"), size=(600, 600))
        self.image_label = customtkinter.CTkLabel(self, image=self.img_background, text="")
        self.image_label.grid(row=0, column=1, rowspan=3)

    def login_admin(self):
        self.toplevel_window = LoginWindow(self)
        self.withdraw()

    def show_main_window(self):
        self.deiconify()


class LoginWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("300x300")
        self.grid_columnconfigure(0, weight=1)
        self.title("login")

        self.username_entry = customtkinter.CTkEntry(self, placeholder_text="username")
        self.username_entry.grid(row=0, column=0, padx=20, pady=20)

        self.cancel_btn = customtkinter.CTkButton(self, text="cancel", command=self.cancel_login)
        self.cancel_btn.grid(row=0, column=0, padx=20, pady=20)

    def cancel_login(self):
        self.master.show_main_window()
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
