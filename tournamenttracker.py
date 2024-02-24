"""
A text application with Python as its core, 
the Tournament Tracker system is used to manage tournaments. 
It provides participant administration features, such as the ability to add, remove, and update participants. 
Data is persistently kept in a JSON file. Error management, 
the ability to create various participant categories with flexibility, 
and user-friendly procedures are some of the key features. All things considered, 
the system offers a flexible and effective way to manage competitions.
"""

import json


class Participant:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {"name": self.name}


class Player(Participant):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def to_dict(self):
        data = super().to_dict()
        data["age"] = self.age
        return data


class Team(Participant):
    def __init__(self, name, players):
        super().__init__(name)
        self.players = players

    def to_dict(self):
        data = super().to_dict()
        data["players"] = [player.to_dict() for player in self.players]
        return data


class Tournament:
    def __init__(self, name):
        self.name = name
        self.participants = []

    def add_participant(self, participant):
        self.participants.append(participant)

    def remove_participant(self, participant):
        if participant in self.participants:
            self.participants.remove(participant)
        else:
            print(f"{participant} not found in the tournament.")

    def update_participant(self, old_participant, new_participant):
        if old_participant in self.participants:
            index = self.participants.index(old_participant)
            self.participants[index] = new_participant
        else:
            print(f"{old_participant} not found in the tournament.")

    def display_participants(self):
        print("Participants:")
        for participant in self.participants:
            print(participant.name)

    def to_dict(self):
        return {"name": self.name, "participants": [participant.to_dict() for participant in self.participants]}


class TournamentTracker:
    def __init__(self, filename):
        self.filename = filename

    def save_tournament(self, tournament):
        with open(self.filename, "w") as file:
            json.dump(tournament.to_dict(), file)

    def load_tournament(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                tournament = Tournament(data["name"])
                for participant_data in data["participants"]:
                    if "age" in participant_data:
                        participant = Player(participant_data["name"], participant_data["age"])
                    elif "players" in participant_data:
                        players = [Player(player["name"], player["age"]) for player in participant_data["players"]]
                        participant = Team(participant_data["name"], players)
                    else:
                        participant = Participant(participant_data["name"])
                    tournament.add_participant(participant)
                return tournament
        except FileNotFoundError:
            print("File not found. Creating a new tournament.")
            return Tournament("New Tournament")


if __name__ == "__main__":
    tracker = TournamentTracker("tournament.json")
    tournament = tracker.load_tournament()

    while True:
        print("\n1. Add Participant")
        print("2. Remove Participant")
        print("3. Update Participant")
        print("4. Display Participants")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter participant name: ")
            participant_type = input("Enter participant type (player/team): ")
            if participant_type.lower() == "player":
                age = input("Enter participant age: ")
                participant = Player(name, age)
            elif participant_type.lower() == "team":
                num_players = int(input("Enter the number of players in the team: "))
                players = []
                for i in range(num_players):
                    player_name = input(f"Enter name of player {i+1}: ")
                    player_age = input(f"Enter age of player {i+1}: ")
                    players.append(Player(player_name, player_age))
                participant = Team(name, players)
            else:
                participant = Participant(name)
            tournament.add_participant(participant)
        elif choice == "2":
            name = input("Enter participant name to remove: ")
            participant = Participant(name)
            tournament.remove_participant(participant)
        elif choice == "3":
            old_name = input("Enter participant name to update: ")
            new_name = input("Enter new participant name: ")
            new_age = input("Enter new participant age: ")
            old_participant = Participant(old_name)
            new_participant = Player(new_name, new_age)
            tournament.update_participant(old_participant, new_participant)
        elif choice == "4":
            tournament.display_participants()
        elif choice == "5":
            tracker.save_tournament(tournament)
            break
        else:
            print("Invalid choice. Please choose again.")
