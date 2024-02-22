import customtkinter
from PIL import Image
from admin import AdminWindow

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master, login_callback=None, **kwargs):
        super().__init__(master, **kwargs)
        self.login_callback = login_callback

        self.username = customtkinter.CTkEntry(self, placeholder_text="Username")
        self.username.place(relx=0.5, rely=0.4, anchor="c")

        self.password = customtkinter.CTkEntry(self, placeholder_text="Password", show="\u2022")
        self.password.place(relx=0.5, rely=0.46, anchor="c")

        self.login_btn = customtkinter.CTkButton(self, text="login", command=self.login_clicked)
        self.login_btn.place(relx=0.5, rely=0.56, anchor="c")

    def login_clicked(self):
        username = self.username.get()
        password = self.password.get()
        if self.login_callback:
            self.login_callback(username, password)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Tournament Tracker")
        self.iconbitmap("./images/run.ico")
        self.resizable(False, False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.login_frame = LoginFrame(master=self, login_callback=self.login_clicked)
        self.login_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.img_background = customtkinter.CTkImage(light_image=Image.open("./images/background.jpg"), dark_image=Image.open("./images/background.jpg"), size=(600, 600))
        self.image_label = customtkinter.CTkLabel(self, image=self.img_background, text="")
        self.image_label.grid(row=0, column=1, rowspan=3)

    def login_clicked(self, username, password):
        print("Username:", username)
        print("Password:", password)

        if username == "" and password == "":
            self.login_admin()

    def login_admin(self):
        self.admin_window = AdminWindow(self)
        self.withdraw()

    def logout(self):
        self.deiconify()


if __name__ == "__main__":
    app = App()
    app.mainloop()
