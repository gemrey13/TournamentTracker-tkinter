import customtkinter


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x600")
        self.title("Tournament Tracker")
        self.grid_columnconfigure(0, weight=1)
        self.login_btn = customtkinter.CTkButton(self, text="login", command=self.login_admin)
        self.login_btn.grid(row=0, column=0, padx=20, pady=20)

    def login_admin(self):
        print("pressed")
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
