



from customtkinter import *
import mysql.connector
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Scrollbar, Canvas
import numpy as np

class Graph:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Progress Tracker")
        self.root.geometry("1800x600+80+280")
        
        title = CTkLabel(self.root, text="GRAPHS", font=("goudy old style", 25, "bold", "underline"), height=50, bg_color="white", fg_color="dodgerblue")
        title.place(x=0, y=0, relwidth=1)
        
        self.bg_img = Image.open("images/bg6.jpg")
        self.bg_img = self.bg_img.resize((1920,1060 ), Image.LANCZOS)
        self.bg_img= ImageTk.PhotoImage(self.bg_img)
        bg_label=CTkLabel(self.root, image=self.bg_img)
        bg_label.place(x=0, y=50)
        
        # Create a frame to hold the graphs
        self.graph_frame1 = Canvas(self.root, width=500, height=400)
        self.graph_frame1.place(x=50, y=100)
        
        self.graph_frame2 = Canvas(self.root, width=500, height=200)
        self.graph_frame2.place(x=600, y=100)
        
        self.graph_frame3 = Canvas(self.root, width=500, height=400)
        self.graph_frame3.place(x=1150, y=100)
        
        self.create_graph1()
        self.create_graph2()
        self.create_graph3()
        
    def fetch_data1(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="P@ss00p",
            database="my_project"
        )
        cursor = db.cursor()
        cursor.execute("select * from archiev")
        data = cursor.fetchall()
        return data

    def create_graph1(self):
        data = self.fetch_data1()
        sem_data = [i[1] for i in data]
        counts = [sem_data.count(i) for i in set(sem_data)]
        labels = list(set(sem_data))
        
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(counts, labels=labels, autopct='%1.1f%%')
        ax.set_title('Achievements during each semester')
        
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame1)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def fetch_data2(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="P@ss00p",
            database="my_project"
        )
        cursor = db.cursor()
        cursor.execute("SELECT Sem, sgpa FROM sgpa")
        data = cursor.fetchall()
        return data

    def create_graph2(self):
        data = self.fetch_data2()
        # Sort the data by semester
        data.sort(key=lambda x: x[0])
        # Extract semester and SGPA values
        semesters = [row[0] for row in data]
        sgpas = [float(row[1]) for row in data]
        
        fig, ax = plt.subplots(figsize=(8,6))
        ax.plot(semesters, sgpas, marker='o')
        ax.set_title('SGPA Analysis For Each Sem')
        ax.set_xlabel('Semester')
        ax.set_ylabel('SGPA')
        ax.set_xticks(semesters)  # set xticks to semester numbers
        
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame2)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def fetch_data3(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="P@ss00p",
            database="my_project"
        )
        cursor = db.cursor()
        cursor.execute("SELECT Progress FROM skills")
        data = cursor.fetchall()
        return data

    def create_graph3(self):
        data = self.fetch_data3()
        incomplete = 0
        inprogress = 0
        complete = 0
        for row in data:
            if row[0] == "Incomplete":
                incomplete += 1
            elif row[0] == "In Progress":
                inprogress += 1
            elif row[0] == "Completed":
                complete += 1
        labels = ['Incomplete', 'In Progress', 'Completed']
        sizes = [incomplete, inprogress, complete]
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax.set_title('Skill Progress Status')

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame3)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
if __name__ == "__main__":
    root = CTk()
    obj = Graph(root)
    root.mainloop()

