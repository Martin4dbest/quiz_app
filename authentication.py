import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import time
import game1
#import game2
#import game3



def create_database():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close()

def register_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False

def username_exists(username):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()
    return result is not None

def authenticate_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    return result is not None

def register():
    username = username_entry.get()
    password = password_entry.get()
    if not username or not password:
        messagebox.showerror("Error", "Please enter a username and password.")
        return
    if len(password) < 6 or not password.isalnum():
        messagebox.showerror("Error", "Password must be alphanumeric and at least 6 characters long.")
        return
    if username_exists(username):
        messagebox.showerror("Error", "Username already exists. Please choose a different username.")
        return
    if register_user(username, password):
        messagebox.showinfo("Success", "Registration successful. You can now log in.")
    else:
        messagebox.showerror("Error", "Failed to register user.")

def login():
    username = username_entry.get()
    password = password_entry.get()
    if not username or not password:
        messagebox.showerror("Error", "Please enter a username and password.")
        return
    if authenticate_user(username, password):
        messagebox.showinfo("Success", "Login successful.")
        root.destroy()  # Destroy the login window
        show_category_selection()  # Show category selection window
    else:
        messagebox.showerror("Error", "Invalid username or password.")

def forgot_password():
    messagebox.showinfo("Forgot Password", "Please contact support for assistance.")

def show_password():
    if password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")




def show_category_selection():
    category_window = tk.Tk()
    category_window.title("Category Selection")
    category_window.geometry("400x400")

    img = tk.PhotoImage(file="logo90.png")
    img_label = tk.Label(category_window, image=img)
    img_label.pack()



    categories = ["GENERAL KNOWLEDGE ", "GEOGRAPHY", "HISTORY", "LITERATURE", "MUSIC", "POP CULTURE", "SPORT"]

    for category in categories:
        button = ttk.Button(category_window, text=category, command=lambda c=category: start_timer(c))
        button.pack(pady=5)

   

    category_window.mainloop()



"""
def quiz_general_knowledge():
    quiz_general_knowledge.start_quiz()

def start_geography_quiz():
    start_geography_quiz()
    print("Starting Geography Quiz")

def start_history_quiz():
    start_history_quiz()
    print("Starting History Quiz")

def start_literature_quiz():
    start_literature_quiz()
    print("Starting Literature Quiz")

def start_movies_quiz():
    start_movies_quiz()
    print("Starting Movies Quiz")

def start_music_quiz():
    start_music_quiz()
    print("Starting Music Quiz")

def start_pop_culture_quiz():
    start_pop_culture_quiz()
    print("Starting Pop Culture Quiz")

def start_science_quiz():
    start_science_quiz
    print("Starting Science Quiz")

def start_sports_quiz():
    start_sports_quiz()
    print("Starting Sports Quiz")

def start_riddle_quiz():
    start_riddle_quiz()
    print("Starting Riddle Quiz")

"""

def start_timer(category):
    timer_decision_window = tk.Toplevel()  # Create a new window for timer decision
    timer_decision_window.title("Timer Decision")
    timer_decision_window.geometry("300x150")

    decision_label = ttk.Label(timer_decision_window, text="Do you want to enable the timer?")
    decision_label.pack(pady=10)

    def start_with_timer():
        timer_decision_window.destroy()  # Close the decision window
        start_timer_window(category)

    def start_without_timer():
        timer_decision_window.destroy()  # Close the decision window
        #start_quiz(category, enable_timer=False)  # Start the quiz without a timer

    timer_button_frame = ttk.Frame(timer_decision_window)
    timer_button_frame.pack(pady=10)

    timer_button = ttk.Button(timer_button_frame, text="Start with Timer", command=start_with_timer)
    timer_button.grid(row=0, column=0, padx=10)

    no_timer_button = ttk.Button(timer_button_frame, text="Continue without Timer", command=start_without_timer)
    no_timer_button.grid(row=0, column=1, padx=10)

def start_timer_window(category):
    timer_window = tk.Toplevel()  # Use Toplevel instead of Tk
    timer_window.title("Timer")
    timer_window.geometry("300x200")

    img = tk.PhotoImage(file="timerr.png")
    img_label = tk.Label(timer_window, image=img)
    img_label.pack()

    countdown_label = ttk.Label(timer_window, text="Time Left:")
    countdown_label.pack()

    countdown_var = tk.StringVar()
    countdown_display = ttk.Label(timer_window, textvariable=countdown_var)
    countdown_display.pack()

    # Timer countdown functionality
    def countdown(seconds):
        if seconds > 0:
            countdown_var.set(seconds)
            timer_window.after(1000, countdown, seconds - 1)  # Schedule the next call after 1000ms (1 second)
        else:
            countdown_var.set("Time's up!")
            try_again_button = ttk.Button(timer_window, text="Try Again", command=timer_window.destroy)
            try_again_button.pack(pady=5)

            # Call the appropriate quiz function based on the selected category
            start_quiz(category)

    countdown(60)  # Start the countdown from 60 seconds

    timer_window.mainloop()


"""
def start_quiz(category, enable_timer=True):
    # Dictionary mapping categories to quiz functions
    quiz_functions = {
        "GENERAL KNOWLEDGE": game1,
        #"GEOGRAPHY": start_geography_quiz,
        #"HISTORY2": start_history_quiz,
        #"LITERATURE": start_literature_quiz,
        #"MOVIES": start_movies_quiz,
        #"MUSIC": start_music_quiz,
        #"POP CULTURE": start_pop_culture_quiz,
        #"SCIENCE": start_science_quiz,
        #"SPORT": start_sports_quiz,
        #"RIDDLE": start_riddle_quiz
    }

   

# Now you can call the start_quiz 

    
     # Retrieve the quiz function based on the category
    quiz_function = quiz_functions.get(category)
    if quiz_function:
        # Call the quiz function
        quiz_function()
    else:
        print("Invalid category")
# Example usage:
#start_quiz("GENERAL KNOWLEDGE", enable_timer=False)  # This will start the General Knowledge quiz without a timer



    if category in quiz_functions:
        if enable_timer:
            start_timer(category)
            
        else:
            print(f"Starting {category} Quiz without Timer")
            # Call the corresponding quiz function based on the selected category
            quiz_functions[category]()
    else:
        print("Invalid category selected")







class QuizGeneralKnowledge:
    def start_quiz(self):
        # Your code for starting the quiz goes here
        print("Starting General Knowledge Quiz")

# Instantiate the class
quiz_general_knowledge = QuizGeneralKnowledge()

def start_quiz(category, enable_timer=True):
    # Dictionary mapping categories to quiz functions
    quiz_functions = {
        "GENERAL KNOWLEDGE": quiz_general_knowledge.start_quiz,
        #"GEOGRAPHY": start_geography_quiz,
        # Add other categories and their corresponding quiz functions here
    }

    # Check if the selected category is in the dictionary
    if category in quiz_functions:
        if enable_timer:
            # Start the timer if enabled
            start_timer(category)
        else:
            # Print message indicating starting quiz without a timer
            print(f"Starting {category} Quiz without Timer")
            # Call the corresponding quiz function based on the selected category
            quiz_functions[category]()
    else:
        print("Invalid category selected")


"""
def create_login_window():
    global root, username_entry, password_entry, password_var

    root = tk.Tk()
    root.title("Who Wants to Be a Millionaire - Login")
    root.geometry("1000x800")
    root.resizable(True, True)  # Allow window expansion

    # Add image of Who Wants to Be a Millionaire
    img = tk.PhotoImage(file="logo90.png")
    img_label = tk.Label(root, image=img)
    img_label.pack()

    frame = ttk.Frame(root)
    frame.pack(pady=10)

    username_label = ttk.Label(frame, text="Username:")
    username_label.grid(row=0, column=0, padx=5, pady=5)

    # Create a rounded entry widget for username
    username_entry = ttk.Entry(frame, style="Rounded.TEntry")
    username_entry.grid(row=0, column=1, padx=5, pady=5)

    password_label = ttk.Label(frame, text="Password:")
    password_label.grid(row=1, column=0, padx=5, pady=5)

    # Create a rounded entry widget for password
    password_var = tk.BooleanVar()
    password_entry = ttk.Entry(frame, show="*", style="Rounded.TEntry")
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    # Add "Show Password" checkbutton
    password_checkbutton = ttk.Checkbutton(frame, text="Show Password", variable=password_var, command=show_password)
    password_checkbutton.grid(row=2, columnspan=2, pady=5)

    login_button = ttk.Button(frame, text="Login", command=login, style="Green.TButton")
    login_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

    register_button = ttk.Button(frame, text="Register", command=register, style="Blue.TButton")
    register_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

    forgot_password_label = tk.Label(root, text="Forgot Password?", fg="blue", cursor="hand2")
    forgot_password_label.pack(pady=5)
    forgot_password_label.bind("<Button-1>", lambda e: forgot_password())

    # Define custom style for rounded entry widgets
    root.style = ttk.Style()
    root.style.theme_use("classic")
    #root.style.configure("Rounded.TEntry", padding=10, relief="flat", foreground="black")
    root.style.configure("Rounded.TEntry", padding=(10, 5), relief="raised", foreground="black")



    root.mainloop()

if __name__ == "__main__":
    create_database()
    create_login_window()
    #start_quiz("GENERAL KNOWLEDGE")
   

