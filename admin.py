import customtkinter


class AdminWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x600")
        self.title("Tournament Tracker | Admin")
        self.after(250, lambda: self.iconbitmap("./images/run.ico"))
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.username_entry = customtkinter.CTkEntry(self, placeholder_text="username")
        self.username_entry.grid(row=0, column=0, padx=20, pady=20)

        self.logout_brn = customtkinter.CTkButton(self, text="logout", command=self.logout)
        self.logout_brn.grid(row=0, column=0, padx=20, pady=20)

    def logout(self):
        self.master.logout()
        self.destroy()
