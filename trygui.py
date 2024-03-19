from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json


class Student:
    def __init__(self, name, age, sport, position, school):
        self.name = name
        self.age = age
        self.sport = sport
        self.position = position
        self.school = school


# sad a


class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def view_students(self):
        return self.students

    def edit_student(self, name, new_age, new_sport, new_position, new_school, sports):
        for student in self.students:
            if student.name == name:
                old_sport = student.sport
                student.age = new_age
                student.sport = new_sport
                student.position = new_position
                student.school = new_school
                messagebox.showinfo("Succes", f"Student {name} details updated successfully!")
                # Update sports data
                if old_sport != new_sport:
                    self.update_sports_data(name, new_sport, new_position, old_sport, sports)
                return
        messagebox.showerror("Error", f"Student {name} not found.")

    def update_sports_data(self, name, new_sport, new_position, old_sport, sports):
        # Remove player from old sport
        if old_sport in sports.sports:
            for player in sports.sports[old_sport]:
                if player["name"] == name:
                    sports.sports[old_sport].remove(player)
                    break
            if not sports.sports[old_sport]:  # Remove sport if no players left
                del sports.sports[old_sport]
        # Add player to new sport
        if new_sport not in sports.sports:
            sports.sports[new_sport] = []
        sports.sports[new_sport].append({"name": name, "position": new_position})

    def delete_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                messagebox.showinfo("Success", f"Student {name} deleted successfully!")
                return
        messagebox.showerror("Error", f"Student {name} not found.")


class Sports:
    def __init__(self):
        self.sports = {}

    def add_player(self, student):
        if student.sport not in self.sports:
            self.sports[student.sport] = []
        self.sports[student.sport].append({"name": student.name, "position": student.position})


class Client:
    def __init__(self, filename):
        self.filename = filename

    def save_data(self, school, sports):
        data = {
            "students": [
                {"name": student.name, "age": student.age, "sport": student.sport, "position": student.position, "school": student.school} for student in school.students
            ],
            "sports": sports.sports,
        }
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=2)
        messagebox.showinfo("Success", "Data saved to JSON.")

    def load_data(self, school, sports):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                for student_data in data["students"]:
                    student = Student(student_data["name"], student_data["age"], student_data["sport"], student_data["position"], student_data["school"])
                    school.add_student(student)
                    sports.add_player(student)
                sports.sports = data["sports"]
            messagebox.showinfo("Success", "Data loaded from JSON.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No existing data found.")


class Admin(Client):
    def __init__(self, filename):
        super().__init__(filename)


class GUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x300")
        self.master.title("Sports Management System")

        self.school = School()
        self.sports = Sports()
        self.admin = Admin("sms_data.json")

        self.bg_image = Image.open("./images/background.jpg")
        self.resized_image = self.bg_image.resize((400, 300))
        self.bg_photo = ImageTk.PhotoImage(self.resized_image)

        self.my_canvas = Canvas(self.master, height=300, width=400)
        self.my_canvas.pack()
        self.my_canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        self.label = tk.Label(self.master, text="Sports Management System", font=("Arial", 20))
        self.label.pack()
        self.label_w = self.my_canvas.create_window(30, 20, anchor="nw", window=self.label)

        self.admin_button = tk.Button(self.master, text="Admin", font=("Arial", 14), width=10, command=self.admin_login)
        self.admin_button.pack()
        self.admin_button_w = self.my_canvas.create_window(20, 150, anchor="nw", window=self.admin_button)

        self.client_button = tk.Button(self.master, text="Client", font=("Arial", 14), width=10, command=self.client_login)
        self.client_button.pack()
        self.client_button_w = self.my_canvas.create_window(260, 150, anchor="nw", window=self.client_button)

    def admin_login(self):
        self.login_window = tk.Toplevel(self.master)
        self.login_window.geometry("300x300")
        self.login_window.title("Admin Login")

        self.bg = Image.open("./images/background.jpg")
        self.image = self.bg.resize((300, 300))
        self.photo = ImageTk.PhotoImage(self.image)

        self.canva = Canvas(self.login_window, height=300, width=300)
        self.canva.pack()
        self.canva.create_image(0, 0, image=self.photo, anchor="nw")

        self.username_label = tk.Label(self.login_window, text="Username:", font=("Arial", 14), width=10)
        self.username_label.pack()
        self.username_label_w = self.canva.create_window(10, 30, anchor="nw", window=self.username_label)

        self.username_entry = tk.Entry(self.login_window, font=("Arial", 14), width=12)
        self.username_entry.pack()
        self.username_entry_w = self.canva.create_window(150, 30, anchor="nw", window=self.username_entry)

        self.password_label = tk.Label(self.login_window, text="Password:", font=("Arial", 14), width=10)
        self.password_label.pack()
        self.password_label_w = self.canva.create_window(10, 120, anchor="nw", window=self.password_label)

        self.password_entry = tk.Entry(self.login_window, show="*", font=("Arial", 14), width=12)
        self.password_entry.pack()
        self.password_entry_w = self.canva.create_window(150, 120, anchor="nw", window=self.password_entry)

        self.login_button = tk.Button(self.login_window, text="Login", font=("Arial", 14), width=15, command=self.admin_authenticate)
        self.login_button.pack()
        self.ulogin_button_w = self.canva.create_window(70, 250, anchor="nw", window=self.login_button)

    def admin_authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "" and password == "":
            self.admin_menu()
            self.login_window.destroy()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def admin_menu(self):
        self.master.withdraw()
        self.admin_window = tk.Toplevel(self.master)
        self.admin_window.geometry("1000x600")
        self.admin_window.title("Admin Menu")

        self.topframe = Frame(self.admin_window, height=50, width=1000, bg="#118ab2")
        self.topframe.pack(fill="x", side="top")
        self.leftframe = Frame(self.admin_window, height=600, width=350, bg="#118ab2", bd=0)
        self.leftframe.pack(fill="y", side="left")
        self.rigthframe = Frame(self.admin_window, height=600, width=820)
        self.rigthframe.pack(fill="both", side="right")

        self.l = Label(self.topframe, text="Sports Management System", bg="#118ab2", fg="black", font=("Arial", 30), justify="center")
        self.l.pack()

        self.add_student_button = tk.Button(self.leftframe, text="Add Student", width=15, font=("Arial", 12), command=self.add_student)
        self.add_student_button.pack(pady=5)

        self.view_students_button = tk.Button(self.leftframe, text="View Students", width=15, font=("Arial", 12), command=self.view_students)
        self.view_students_button.pack(pady=5)

        self.view_sports_button = tk.Button(self.leftframe, text="View Sports", width=15, font=("Arial", 12), command=self.view_sports)
        self.view_sports_button.pack(pady=5)

        self.edit_student_button = tk.Button(self.leftframe, text="Edit Data", width=15, font=("Arial", 12), command=self.edit_student_window)
        self.edit_student_button.pack(pady=5)

        self.delete_student_button = tk.Button(self.leftframe, text="Delete Data", width=15, font=("Arial", 12), command=self.delete_student_window)
        self.delete_student_button.pack(pady=5)

        self.save_button = tk.Button(self.leftframe, text="Save to JSON", width=15, font=("Arial", 12), command=self.save_data)
        self.save_button.pack(pady=5)

        self.load_button = tk.Button(self.leftframe, text="Load from JSON", width=15, font=("Arial", 12), command=self.load_data)
        self.load_button.pack(pady=5)

        self.logout_button = tk.Button(self.leftframe, text="Log Out", width=15, font=("Arial", 12), command=self.admin_log_out)
        self.logout_button.pack(pady=5)

        self.exit_button = tk.Button(self.leftframe, text="Exit", width=15, font=("Arial", 12), command=self.exit_app)
        self.exit_button.pack(pady=5)

        self.abt_b = Button(self.topframe, text="About", command=self.showAbt, font=("Arial", 15), bg="#118ab2", fg="black", bd=0)
        self.abt_b.pack(side=RIGHT, anchor=N)
        self.prof_b = Button(self.topframe, text="Profile", command=self.showProf, font=("Arial", 15), bg="#118ab2", fg="black", bd=0)
        self.prof_b.pack(side=RIGHT, anchor=N)

        self.aboutIterate = 0
        self.txt = ""

        self._a = "Sports Management System"
        self.a = [
            """ 
                Welcome to the Sports Management System, your all-in-one solution for efficiently organizing 
                and accessing sports-related data!
                Designed to streamline administrative tasks and provide convenient access to information,
                our system offers a range of powerful features
                Administrators can effortlessly add and manage student profiles, including details
                such as name, age, sport, position, and school affiliation.
                With the ability to view both individual student data and sports teams' compositions,
                tracking and organizing sports participation has never been easier.
                Plus, our system allows for seamless data storage and retrieval, 
                with support for saving and loading data in a structured JSON format.
                Whether you're overseeing sports programs, managing student profiles, 
                or simply accessing sports data, our system provides a user-friendly interface 
                to meet your needs effectively. 
                Welcome to a smarter way of managing sports information!"
"""
        ]

        self.prof = Frame(self.rigthframe, bg="black")
        self.abt = Frame(self.rigthframe, width=500, height=750)
        self.a_l = Label(self.abt, text=self._a, font=("Arial", 25), fg="black", justify="center")
        self.a_l1 = Label(self.abt, font=("Arial", 14), fg="black", justify="center")

        self.a_l.pack(fill="both")
        self.a_l1.pack(pady=10)

        self.abt.pack()

        self.bg_image = Image.open("pic.webp")
        self.resized_image = self.bg_image.resize((970, 600))
        self.bg_photo = ImageTk.PhotoImage(self.resized_image)

        self.my_canvas = Canvas(self.prof, height=600, width=1000)
        self.my_canvas.pack()
        self.my_canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        self.prof.pack()
        self.abt.pack_forget()

    def animateAbout(self):
        if self.aboutIterate < len(self.a):
            self.txt += self.a[self.aboutIterate] + "\n"
            self.a_l1.config(text=self.txt)
            self.aboutIterate += 1
            self.a_l1.after(200, self.animateAbout)

    def showProf(self):
        self.prof.pack()
        self.abt.pack_forget()

    def showAbt(self):
        self.abt.pack(fill="both")
        self.prof.pack_forget()
        self.animateAbout()

    def add_student(self):
        self.add_student_window = tk.Toplevel(self.admin_window)
        self.add_student_window.geometry("400x350")
        self.add_student_window.title("Add Student")
        self.add_student_window.configure(bg="#b7b7a4")

        self.name_label = tk.Label(self.add_student_window, text="Name:", width=15, font=("Arial", 15), bg="#b7b7a4")
        self.name_label.grid(row=0, column=0, padx=5, pady=15)
        self.name_entry = tk.Entry(self.add_student_window, width=18, font=("Arial", 15))
        self.name_entry.grid(row=0, column=1, padx=5, pady=15)

        self.age_label = tk.Label(self.add_student_window, text="Age:", width=15, font=("Arial", 15), bg="#b7b7a4")
        self.age_label.grid(row=1, column=0, padx=5, pady=15)
        self.age_entry = tk.Entry(self.add_student_window, width=18, font=("Arial", 15))
        self.age_entry.grid(row=1, column=1, padx=5, pady=15)

        self.sport_label = tk.Label(self.add_student_window, text="Sport:", width=15, font=("Arial", 15), bg="#b7b7a4")
        self.sport_label.grid(row=2, column=0, padx=5, pady=15)
        self.sport_entry = tk.Entry(self.add_student_window, width=18, font=("Arial", 15))
        self.sport_entry.grid(row=2, column=1, padx=5, pady=15)

        self.position_label = tk.Label(self.add_student_window, text="Position:", width=15, font=("Arial", 15), bg="#b7b7a4")
        self.position_label.grid(row=3, column=0, padx=5, pady=15)
        self.position_entry = tk.Entry(self.add_student_window, width=18, font=("Arial", 15))
        self.position_entry.grid(row=3, column=1, padx=5, pady=15)

        self.school_label = tk.Label(self.add_student_window, text="School:", width=15, font=("Arial", 15), bg="#b7b7a4")
        self.school_label.grid(row=4, column=0, padx=5, pady=15)
        self.school_entry = tk.Entry(self.add_student_window, width=18, font=("Arial", 15))
        self.school_entry.grid(row=4, column=1, padx=5, pady=15)

        self.add_button = tk.Button(self.add_student_window, text="Add Student", command=self.save_student, width=15, font=("Arial", 12), bg="#6b705c")
        self.add_button.grid(row=5, columnspan=2, padx=5, pady=15)

    def save_student(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        sport = self.sport_entry.get()
        position = self.position_entry.get()
        school = self.school_entry.get()

        if name and age and sport and position and school:
            student = Student(name, age, sport, position, school)
            self.school.add_student(student)
            self.sports.add_player(student)
            messagebox.showinfo("Success", "Student added successfully!")
            self.add_student_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required.")

    def view_students(self):
        students = self.school.view_students()
        if students:
            self.view_window = tk.Toplevel(self.admin_window)
            self.view_window.title("View Students")

            self.students_text = tk.Text(self.view_window)
            self.students_text.pack()

            for student in students:
                self.students_text.insert(
                    tk.END, f"Name: {student.name}, Age: {student.age}, Sport: {student.sport}, Position: {student.position}, School: {student.school}\n"
                )
        else:
            messagebox.showinfo("Info", "No students to display.")

    def view_sports(self):
        sports = self.sports.sports
        if sports:
            self.view_window = tk.Toplevel(self.admin_window)
            self.view_window.title("View Sports")

            self.sports_text = tk.Text(self.view_window)
            self.sports_text.pack()

            for sport, players in sports.items():
                self.sports_text.insert(tk.END, f"\nSport: {sport}\n")
                for player in players:
                    self.sports_text.insert(tk.END, f"Name: {player['name']}, Position: {player['position']}\n")
        else:
            messagebox.showinfo("Info", "No sports data available.")

    def edit_student_window(self):
        self.edit_student_window = tk.Toplevel(self.admin_window)
        self.edit_student_window.geometry("400x350")
        self.edit_student_window.title("Edit Student")
        self.edit_student_window.configure(bg="#b7b7a4")

        self.name_label = tk.Label(self.edit_student_window, text="Name:", width=15, font=("Arial", 15), bg="#b7b7a4")
        self.name_label.grid(row=0, column=0, padx=5, pady=15)
        self.name_entry = tk.Entry(self.edit_student_window, width=18, font=("Arial", 15))
        self.name_entry.grid(row=0, column=1, padx=5, pady=15)

        self.new_age_label = tk.Label(self.edit_student_window, text="Age:", width=15, font=("Arial", 15), bg="#b7b7a4")
        self.new_age_label.grid(row=1, column=0, padx=5, pady=15)
        self.new_age_entry = tk.Entry(self.edit_student_window, width=18, font=("Arial", 15))
        self.new_age_entry.grid(row=1, column=1, padx=5, pady=15)

        self.new_sport_label = tk.Label(self.edit_student_window, text="Sports:", width=15, font=("Arial", 15), bg="#b7b7a4")
        self.new_sport_label.grid(row=2, column=0, padx=5, pady=15)
        self.new_sport_entry = tk.Entry(self.edit_student_window, width=18, font=("Arial", 15))
        self.new_sport_entry.grid(row=2, column=1, padx=5, pady=15)

        self.new_position_label = tk.Label(self.edit_student_window, text="Position:", width=15, font=("Arial", 15), bg="#b7b7a4")
        self.new_position_label.grid(row=3, column=0, padx=5, pady=15)
        self.new_position_entry = tk.Entry(self.edit_student_window, width=18, font=("Arial", 15))
        self.new_position_entry.grid(row=3, column=1, padx=5, pady=15)

        self.new_school_label = tk.Label(self.edit_student_window, text="School:", width=15, font=("Arial", 15), bg="#b7b7a4")
        self.new_school_label.grid(row=4, column=0, padx=5, pady=15)
        self.new_school_entry = tk.Entry(self.edit_student_window, width=18, font=("Arial", 15))
        self.new_school_entry.grid(row=4, column=1, padx=5, pady=15)

        self.edit_button = tk.Button(self.edit_student_window, text="Edit", command=self.edit_student, width=15, font=("Arial", 12), bg="#6b705c")
        self.edit_button.grid(row=5, columnspan=2, padx=5, pady=15)

    def edit_student(self):
        name = self.name_entry.get()
        new_age = self.new_age_entry.get()
        new_sport = self.new_sport_entry.get()
        new_position = self.new_position_entry.get()
        new_school = self.new_school_entry.get()

        self.school.edit_student(name, new_age, new_sport, new_position, new_school, self.sports)
        self.edit_student_window.withdraw()

    def delete_student_window(self):
        self.delete_student_window = tk.Toplevel(self.admin_window)
        self.delete_student_window.geometry("400x200")
        self.delete_student_window.title("Delete Student")
        self.delete_student_window.configure(bg="#b7b7a4")

        self.name_label = tk.Label(self.delete_student_window, text="Name:", width=15, font=("Arial", 15), bg="#b7b7a4")
        self.name_label.grid(row=0, column=0, padx=5, pady=15)
        self.name_entry = tk.Entry(self.delete_student_window, width=18, font=("Arial", 15))
        self.name_entry.grid(row=0, column=1, padx=5, pady=15)

        self.delete_button = tk.Button(self.delete_student_window, text="Delete", command=self.delete_student, width=15, font=("Arial", 12), bg="#6b705c")
        self.delete_button.grid(row=1, columnspan=2, padx=5, pady=15)

    def delete_student(self):
        name = self.name_entry.get()
        self.school.delete_student(name)

    def save_data(self):
        self.admin.save_data(self.school, self.sports)

    def load_data(self):
        self.admin.load_data(self.school, self.sports)

    def admin_log_out(self):
        self.admin_window.destroy()
        self.master.deiconify()

    def client_login(self):
        self.master.withdraw()
        self.client_window = tk.Toplevel(self.master)
        self.client_window.geometry("1000x600")
        self.client_window.title("Client Menu")

        self.topframe = Frame(self.client_window, height=50, width=1000, bg="#118ab2")
        self.topframe.pack(fill="x", side="top")
        self.leftframe = Frame(self.client_window, height=600, width=350, bg="#118ab2", bd=0)
        self.leftframe.pack(fill="y", side="left")
        self.rigthframe = Frame(self.client_window, height=600, width=820)
        self.rigthframe.pack(fill="both", side="right")

        self.l = Label(self.topframe, text="Sports Management System", bg="#118ab2", fg="black", font=("Arial", 30), justify="center")
        self.l.pack()

        self.add_student_button = tk.Button(self.leftframe, text="Add Student", width=15, font=("Arial", 12), command=self.client_add_student)
        self.add_student_button.pack(pady=5)

        self.view_students_button = tk.Button(self.leftframe, text="View Students", width=15, font=("Arial", 12), command=self.client_view_students)
        self.view_students_button.pack(pady=5)

        self.view_sports_button = tk.Button(self.leftframe, text="View Sports", width=15, font=("Arial", 12), command=self.client_view_sports)
        self.view_sports_button.pack(pady=5)

        self.delete_student_button = tk.Button(self.leftframe, text="Delete Data", width=15, font=("Arial", 12), command=self.client_delete_window)
        self.delete_student_button.pack(pady=5)

        self.save_button = tk.Button(self.leftframe, text="Save to JSON", width=15, font=("Arial", 12), command=self.client_save_data)
        self.save_button.pack(pady=5)

        self.load_button = tk.Button(self.leftframe, text="Load from JSON", width=15, font=("Arial", 12), command=self.client_load_data)
        self.load_button.pack(pady=5)

        self.logout_button = tk.Button(self.leftframe, text="Log Out", width=15, font=("Arial", 12), command=self.client_log_out)
        self.logout_button.pack(pady=5)

        self.exit_button = tk.Button(self.leftframe, text="Exit", width=15, font=("Arial", 12), command=self.exit_app)
        self.exit_button.pack(pady=5)

        self.abt_b = Button(self.topframe, text="About", command=self.showAbt, font=("Arial", 15), bg="#118ab2", fg="black", bd=0)
        self.abt_b.pack(side=RIGHT, anchor=N)
        self.prof_b = Button(self.topframe, text="Profile", command=self.showProf, font=("Arial", 15), bg="#118ab2", fg="black", bd=0)
        self.prof_b.pack(side=RIGHT, anchor=N)

        self.aboutIterate = 0
        self.txt = ""

        self._a = "Sports Management System"
        self.a = [
            """ 
                Welcome to the Sports Management System, your all-in-one solution for efficiently organizing 
                and accessing sports-related data!
                Designed to streamline administrative tasks and provide convenient access to information,
                our system offers a range of powerful features
                Administrators can effortlessly add and manage student profiles, including details
                such as name, age, sport, position, and school affiliation.
                With the ability to view both individual student data and sports teams' compositions,
                tracking and organizing sports participation has never been easier.
                Plus, our system allows for seamless data storage and retrieval, 
                with support for saving and loading data in a structured JSON format.
                Whether you're overseeing sports programs, managing student profiles, 
                or simply accessing sports data, our system provides a user-friendly interface 
                to meet your needs effectively. 
                Welcome to a smarter way of managing sports information!"
"""
        ]

        self.prof = Frame(self.rigthframe, bg="black")
        self.abt = Frame(self.rigthframe, width=500, height=750)
        self.a_l = Label(self.abt, text=self._a, font=("Arial", 25), fg="black", justify="center")
        self.a_l1 = Label(self.abt, font=("Arial", 14), fg="black", justify="center")

        self.a_l.pack(fill="both")
        self.a_l1.pack(pady=10)

        self.abt.pack()

        self.bg_image = Image.open("pic.webp")
        self.resized_image = self.bg_image.resize((970, 600))
        self.bg_photo = ImageTk.PhotoImage(self.resized_image)

        self.my_canvas = Canvas(self.prof, height=600, width=1000)
        self.my_canvas.pack()
        self.my_canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        self.prof.pack()
        self.abt.pack_forget()

    def animateAbout(self):
        if self.aboutIterate < len(self.a):
            self.txt += self.a[self.aboutIterate] + "\n"
            self.a_l1.config(text=self.txt)
            self.aboutIterate += 1
            self.a_l1.after(200, self.animateAbout)

    def showProf(self):
        self.prof.pack()
        self.abt.pack_forget()

    def showAbt(self):
        self.abt.pack(fill="both")
        self.prof.pack_forget()
        self.animateAbout()

    def client_add_student(self):
        self.add_student_window = tk.Toplevel(self.client_window)
        self.add_student_window.geometry("400x350")
        self.add_student_window.title("Add Student")
        self.add_student_window.configure(bg="#b7b7a4")

        self.name_label = tk.Label(self.add_student_window, text="Name:", width=15, font=("Arial", 15), bg="#b7b7a4")
        self.name_label.grid(row=0, column=0, padx=5, pady=15)
        self.name_entry = tk.Entry(self.add_student_window, width=18, font=("Arial", 15))
        self.name_entry.grid(row=0, column=1, padx=5, pady=15)

        self.age_label = tk.Label(self.add_student_window, text="Age:", width=15, font=("Arial", 15), bg="#b7b7a4")
        self.age_label.grid(row=1, column=0, padx=5, pady=15)
        self.age_entry = tk.Entry(self.add_student_window, width=18, font=("Arial", 15))
        self.age_entry.grid(row=1, column=1, padx=5, pady=15)

        self.sport_label = tk.Label(self.add_student_window, text="Sport:", width=15, font=("Arial", 15), bg="#b7b7a4")
        self.sport_label.grid(row=2, column=0, padx=5, pady=15)
        self.sport_entry = tk.Entry(self.add_student_window, width=18, font=("Arial", 15))
        self.sport_entry.grid(row=2, column=1, padx=5, pady=15)

        self.position_label = tk.Label(self.add_student_window, text="Position:", width=15, font=("Arial", 15), bg="#b7b7a4")
        self.position_label.grid(row=3, column=0, padx=5, pady=15)
        self.position_entry = tk.Entry(self.add_student_window, width=18, font=("Arial", 15))
        self.position_entry.grid(row=3, column=1, padx=5, pady=15)

        self.school_label = tk.Label(self.add_student_window, text="School:", width=15, font=("Arial", 15), bg="#b7b7a4")
        self.school_label.grid(row=4, column=0, padx=5, pady=15)
        self.school_entry = tk.Entry(self.add_student_window, width=18, font=("Arial", 15))
        self.school_entry.grid(row=4, column=1, padx=5, pady=15)

        self.add_button = tk.Button(self.add_student_window, text="Add Student", command=self.client_save_student, width=15, font=("Arial", 12), bg="#6b705c")
        self.add_button.grid(row=5, columnspan=2, padx=5, pady=15)

    def client_save_student(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        sport = self.sport_entry.get()
        position = self.position_entry.get()
        school = self.school_entry.get()

        if name and age and sport and position and school:
            student = Student(name, age, sport, position, school)
            self.school.add_student(student)
            self.sports.add_player(student)
            messagebox.showinfo("Success", "Student added successfully!")
            self.add_student_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required.")

    def client_view_students(self):
        students = self.school.view_students()
        if students:
            self.view_window = tk.Toplevel(self.client_window)
            self.view_window.title("View Students")

            self.students_text = tk.Text(self.view_window)
            self.students_text.pack()

            for student in students:
                self.students_text.insert(
                    tk.END, f"Name: {student.name}, Age: {student.age}, Sport: {student.sport}, Position: {student.position}, School: {student.school}\n"
                )
        else:
            messagebox.showinfo("Info", "No students to display.")

    def client_view_sports(self):
        sports = self.sports.sports
        if sports:
            self.view_window = tk.Toplevel(self.client_window)
            self.view_window.title("View Sports")

            self.sports_text = tk.Text(self.view_window)
            self.sports_text.pack()

            for sport, players in sports.items():
                self.sports_text.insert(tk.END, f"\nSport: {sport}\n")
                for player in players:
                    self.sports_text.insert(tk.END, f"Name: {player['name']}, Position: {player['position']}\n")
        else:
            messagebox.showinfo("Info", "No sports data available.")

    def client_delete_window(self):
        self.delete_student_window = tk.Toplevel(self.client_window)
        self.delete_student_window.geometry("400x200")
        self.delete_student_window.title("Delete Student")
        self.delete_student_window.configure(bg="#b7b7a4")

        self.name_label = tk.Label(self.delete_student_window, text="Name:", width=15, font=("Arial", 15), bg="#b7b7a4")
        self.name_label.grid(row=0, column=0, padx=5, pady=15)
        self.name_entry = tk.Entry(self.delete_student_window, width=18, font=("Arial", 15))
        self.name_entry.grid(row=0, column=1, padx=5, pady=15)

        self.delete_button = tk.Button(self.delete_student_window, text="Delete", command=self.client_delete, width=15, font=("Arial", 12), bg="#6b705c")
        self.delete_button.grid(row=1, columnspan=2, padx=5, pady=15)

    def client_delete(self):
        name = self.name_entry.get()
        self.school.delete_student(name)

    def client_save_data(self):
        self.admin.save_data(self.school, self.sports)

    def client_load_data(self):
        self.admin.load_data(self.school, self.sports)

    def client_log_out(self):
        self.client_window.destroy()
        self.master.deiconify()

    def exit_app(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
