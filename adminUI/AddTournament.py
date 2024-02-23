import customtkinter
import json


class AddTournamentWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("700x400")
        self.title("Tournament Tracker | Add Tournament")
        self.after(250, lambda: self.iconbitmap("./images/run.ico"))
        self.resizable(False, False)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.tournament_data = {"tournament_name": "", "teams": []}

        self.add_tournament_name = customtkinter.CTkEntry(self, placeholder_text="add tournament name")
        self.add_tournament_name.grid(row=0, column=0)

        self.add_tournament_name_btn = customtkinter.CTkButton(self, text="add tournament name", command=self.save_tournament_name)
        self.add_tournament_name_btn.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.add_team_entry = customtkinter.CTkEntry(self, placeholder_text="add team")
        self.add_team_entry.grid(row=2, column=0)

        self.add_team_btn = customtkinter.CTkButton(self, text="add team", command=self.save_team)
        self.add_team_btn.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        self.add_tournament = customtkinter.CTkButton(self, text="add tournament", command=self.save_data)
        self.add_tournament.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

    def save_team(self):
        value = self.add_team_entry.get()
        print(value)
        teams = self.tournament_data["teams"]
        if value == "":
            print("No value")
            return False
        if len(teams) == None:
            print("Team data none")
            return False
        for i in teams:
            if value == i:
                print("Similar team name")
                return False
        self.tournament_data["teams"].append(value)

    def save_tournament_name(self):
        value = self.add_tournament_name.get()
        self.tournament_data["tournament_name"] = value
        print(value)

    def save_data(self):
        if self.tournament_data["tournament_name"] == "" or len(self.tournament_data["teams"]) == 0:
            print("No Tournament name or teams")
            return False

        with open("db.json", "r+") as file:
            data = json.load(file)
            tournament = data["tournament_tracker"]
            tournament.append(self.tournament_data)
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
            print("saved")
