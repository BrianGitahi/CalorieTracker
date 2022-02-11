import tkinter as tk  # Import statements
from tkinter import font
import pyodbc  #


# Receives user input for food item to search for.
def get_input(entry):
    global name
    name = entry
    return name


# Connects to the database and searches for food item from entry given by user and returns the kcal/100g value for the food item
def get_food(name):
    conn = pyodbc.connect("Driver={SQL Server};"
                          r"Server=LAPTOP-AVKA8FMQ\SQLEXPRESS;"
                          "Database=Food_table;"
                          "Trusted_Connection=yes;")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM food WHERE Food_name = ?", name)
    food = cursor.fetchall()
    for row in food:
        kcal = int(row[2])

    return kcal


# Takes input for user regarding the weight of the food item.
def grams(entry_1):
    return entry_1


# Calculates the calories for the food item at the weight given.
def calculate():
    gram = int(entry_1.get())
    kcal = get_food(name)
    total = kcal * gram / 100
    return total


# Displays the following info: Food name, weight, total calories ; on the label
def display_text():
    name = entry.get()
    new = name.capitalize()
    weight = str(entry_1.get())
    calories = calculate()

    label.config(text=new + "\n" + weight + "g" + "\n" + str(calories) + " calories")


# The size of the GUI window
HEIGHT = 600
WIDTH = 950

# Creating the GUI....
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file=r"C:\Users\brian\PycharmProjects\Calories\food2.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#b3ffff", bd=5)
frame.place(relx=0.5, rely=0.2, relwidth=0.85, relheight=0.3, anchor='n')

label = tk.Label(frame, text="Food item:", font=("Courier", 12), bg="#b3ffff")
label.place(relx=0, rely=0.13, relwidth=0.2, relheight=0.3)

entry = tk.Entry(frame, font=("Courier", 12))
entry.place(relx=0.21, rely=0.13, relwidth=0.4, relheight=0.2)

button_1 = tk.Button(frame, text="Enter", bg="gray", font=("Courier", 12), command=lambda: get_input(entry.get()))
button_1.place(relx=0.7, rely=0.13, relwidth=0.25, relheight=0.2)

label_1 = tk.Label(frame, text="Weight (grams):", font=("Courier", 12), bg="#b3ffff")
label_1.place(relx=0, rely=0.4, relwidth=0.2, relheight=0.3)

entry_1 = tk.Entry(frame, font=("Courier", 12))
entry_1.place(relx=0.21, rely=0.4, relwidth=0.4, relheight=0.2)

button_2 = tk.Button(frame, text="Enter", bg="gray", font=("Courier", 12), command=lambda: grams(entry_1.get()))
button_2.place(relx=0.7, rely=0.4, relwidth=0.25, relheight=0.2)

button_3 = tk.Button(frame, text="Calculate Calories", bg="gray", font=("Courier", 12), command=lambda: calculate())
button_3.place(relx=0.7, rely=0.68, relwidth=0.25, relheight=0.2)

frame_2 = tk.Frame(root, bg="#b3ffff", bd=5)
frame_2.place(relx=0.375, rely=0.55, relwidth=0.6, relheight=0.3, anchor='n')

label = tk.Label(frame_2, font=("Courier", 18), anchor='nw', justify='left', bd=4)
label.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

button = tk.Button(frame_2, text="Display Result", bg="gray", font=("Courier", 12), command=lambda: display_text())
button.place(relx=0.69, rely=0.78, relwidth=0.3, relheight=0.2)

# Displays the GUI
root.mainloop()
