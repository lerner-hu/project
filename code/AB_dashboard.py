from tkinter import  messagebox
from customtkinter import *
from PIL import Image, ImageTk
import mysql.connector
from marks import mark
from skills import skill
from achiv import achiev
from grp import grp
from feedback import fdb
from certificate import certify
import random
from tkinter.filedialog import asksaveasfile
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from tkinter import Canvas


class PPT:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Progress Tracker")
        self.root.geometry("1535x786+0+0")
        self.root.resizable(False, False)


       
        # background imag
        self.bg_img = Image.open("images/cat.jpg").convert("RGBA")
        self.bg_img = self.make_transparent(self.bg_img, 0.5)
        self.bg_img = self.bg_img.resize((1920,1080 ), Image.LANCZOS)
        self.bg_img= ImageTk.PhotoImage(self.bg_img)
        bg_label=CTkLabel(self.root, image=self.bg_img)
        bg_label.place(x=0, y=45)


        


        # Logo
        self.logo = Image.open("images/progress.ico")
        self.logo = self.logo.resize((40, 40), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.logo)

         # List of quotes
        self.quotes = [
            "Success is not final; failure is not fatal; it is the courage to continue that counts.",
            "The future belongs to those who believe in the beauty of their dreams.",
            "Your limitation—it's only your imagination.",
            "Push yourself, because no one else is going to do it for you.",
            "Great things never come from comfort zones.",
            
            "Success doesn't just find you. You have to go out and get it.",
            "The harder you work for something, the greater you'll feel when you achieve it."
        ]

        # Randomly select a quote
        self.quote = random.choice(self.quotes)

         # Quote Box (message bubble shape)
        quote_frame = CTkFrame(self.root, width=400, corner_radius=30, fg_color="white")
        quote_frame.place(x=70, y=570)

         


        # Create a Canvas for the message bubble shape
        message_canvas = Canvas(quote_frame, width=400, height=150, bg="black", bd=0, highlightthickness=0)
        message_canvas.pack(fill="both", expand=True)

        # Draw the message bubble (rounded rectangle + triangle)
        message_canvas.create_polygon(20, 20, 380, 20, 380, 130, 20, 130, 20, 70, 0, 90, fill="white", outline="white", width=2)

        
         # Quote text inside the message bubble
        quote_label = CTkLabel(quote_frame, text=self.quote, text_color="black",
                               font=("goudy old style", 20, "bold" , "italic"), anchor="center", width=300, wraplength=300)
        quote_label.place(x=10, y=40)


        # Title
        title = CTkLabel(self.root, text="PERSONAL PROGRESS TRACKER",compound=LEFT, padx=20, image=self.logo,
                         font=("goudy old style", 25, "bold", "underline"),
                         height=50, bg_color="white", fg_color="darkslateblue")
        title.place(x=0, y=0, relwidth=1)

        # Menu Buttons
        m_frame = CTkFrame(self.root, width=1440, height=50, border_width=1,fg_color="black")
        m_frame.place(x=45, y=80 )
        
        mrk_btn=CTkButton(m_frame, text="MARKS", cursor="hand2",font=("goudy old style", 20, "bold"), height=35, width=140,command=self.add_marks)
        mrk_btn.place(x=220, y=11)
        skill_btn=CTkButton(m_frame, text="SKILLS", cursor="hand2",font=("goudy old style", 20, "bold"), height=35, width=140,command=self.add_skills)
        skill_btn.place(x=420, y=11)
        achiv_btn=CTkButton(m_frame, text="ACHIEVEMENT", cursor="hand2", font=("goudy old style", 20, "bold"), height=35, width=140,command=self.add_achievemnts)
        achiv_btn.place(x=630, y=11)
        grh_btn=CTkButton(m_frame, text="GRAPH", cursor="hand2", font=("goudy old style", 20, "bold"), height=35, width=140,command=self.add_graph) 
        grh_btn.place(x=850, y=11)
        fb_btn=CTkButton(m_frame, text="FEEDBACK", cursor="hand2", font=("goudy old style", 20, "bold"), height=35, width=140,command=self.add_feedback)
        fb_btn.place(x=1050, y=11)
        cert_btn=CTkButton(m_frame, text="CERTIFICATES", cursor="hand2", font=("goudy old style", 20, "bold"), height=35, width=140,command=self.add_certificate)
        cert_btn.place(x=1250, y=11)
        home_btn=CTkButton(m_frame, text="HOME", cursor="hand2", font=("goudy old style", 20, "bold"), height=35, width=140, command=self.home)
        home_btn.place(x=30, y=11)
        
         # PDF Section
       
        
        self.var_sem_search=StringVar()

        all_sem=["sem 1","sem 2","sem 3","sem 4","sem 5","sem 6","sem 7","sem 8"]
        self.semester=CTkComboBox(self.root,variable=self.var_sem_search,values=all_sem,height=30,width=250,state="readonly",font=("helvetica", 18),text_color="black",fg_color="azure")
        self.semester.place(x=620, y=670)
        self.semester.set("Enter Semester")
        pdf_btn=CTkButton(self.root, text="SAVE DATA",command=self.save_file, cursor="hand2", font=("goudy old style", 20, "bold"),height=35, width=200)
        pdf_btn.place(x=650, y=710)

    
    def save_file(self):
         file=filedialog.asksaveasfilename(
              filetypes=[("pdf file",".pdf")],defaultextension=".pdf")
         if file:
             self.share_btn(file)
         
    def share_btn(self, file_path):
        pdf = canvas.Canvas(file_path, bottomup=0)
        
        # Initialize y_position at the beginning
        y_position = 50  # Starting point for text
        # Add a title
        
        pdf.setFont("Helvetica-Bold", 20)
        pdf.drawString(200, 30, "Student Progress Report")
        pdf.setFont("Helvetica", 12)
        clg_name="JAIN COLLEGE OF ENGINEERING AND RESEARCH"
        student_name = "Priyanka K"
        usn="2JR22CS062"
        branch="CSE"
        div="A"
        
        click="click on the link to provide feedback:"
        #click="click on link to provide feedback"
        pdf.drawString(100, 80, f"College Name: {clg_name}")
        pdf.drawString(100, 100, f"Student Name: {student_name}")
        pdf.drawString(100, 120, f"USN: {usn}")
        pdf.drawString(100, 140, f"Branch: {branch}")
        pdf.drawString(100, 160, f"DIV: {div}")
        
        
        
        pdf.drawString(100, 180, "Click here to visit Google")
        # Define the clickable link's area (coordinates match text)
        x1, y1 = 100, 170  # Coordinates for the link's lower-left corner
        x2, y2 = 240, 190  # Adjust the width and height of the clickable area
        pdf.linkURL("https://forms.gle/mNkKDV1NrMFa63kBA", (x1, y1, x2, y2), relative=0, thickness=0, color=None)

        y_position = 200
        try:
            db = mysql.connector.connect(
                host="localhost",
                        user="root",
                        password="P@ss00p",
                        database="my_project",
                        use_pure=True
                )
            cursor = db.cursor()
            cursor.execute("SELECT * FROM sgpa WHERE sem = %s", (self.var_sem_search.get(),))
            sgpa_data = cursor.fetchall()
            if sgpa_data:
                pdf.setFont("Helvetica-Bold", 14)
                pdf.drawString(100, y_position, "your SGPA:")
                y_position += 20
                pdf.setFont("Helvetica", 12)
                for record in sgpa_data:
                    pdf.drawString(100, y_position, f"Sem: {record[0]}             SGPA: {record[1]}")
                    y_position += 20
                else:
                    pdf.setFont("Helvetica", 12)
                    pdf.setFont("Helvetica-Bold", 12)
                    pdf.drawString(100, y_position, "No SGPA data Available for this semester")
                    y_position += 20
                cursor.execute("SELECT * FROM skills WHERE progress = %s AND sem = %s", ('completed', self.var_sem_search.get()))
                skill_data = cursor.fetchall()
                if skill_data:
                    
                    pdf.setFont("Helvetica-Bold", 14)
                    y_position += 30 
                    pdf.drawString(100, y_position, "Skills Data:")
                    y_position += 20
                    pdf.setFont("Helvetica", 12)
                    for record in skill_data:
                        pdf.drawString(100, y_position, f"Skill Name: {record[3]}             Progress: {record[4]}")
                        y_position += 20
                else:
                    pdf.setFont("Helvetica", 12)
                    pdf.setFont("Helvetica-Bold", 12)
                    pdf.drawString(100, y_position, "No Skills Data Available for this semester")
                    y_position += 20
                # Query to fetch data for Marks
                cursor.execute("SELECT * FROM marks WHERE sem = %s", (self.var_sem_search.get(),))
                marks_data = cursor.fetchall()
                if marks_data:
                    pdf.setFont("Helvetica-Bold", 14)
                    y_position += 30  # Add some gap before Marks section
                    pdf.drawString(100, y_position, "Marks Data:")
                    y_position += 20
                    pdf.setFont("Helvetica", 12)
                    for record in marks_data:
                        pdf.drawString(100, y_position, f"Subject Name: {record[2]}             Marks: {record[3]}")
                        y_position += 20
                else:
                    pdf.setFont("Helvetica", 12)
                    pdf.setFont("Helvetica-Bold", 12)
                    pdf.drawString(100, y_position, "No Marks Data Available for this semester")
                    y_position += 20
                # Add more space before starting the Achievements section
                y_position += 30  # Increase this value to add a larger gap between Marks and Achievements
                # Query to fetch data for Achievements
                cursor.execute("SELECT * FROM archiev WHERE sem = %s", (self.var_sem_search.get(),))
                achievements_data = cursor.fetchall()
                if achievements_data:
                    pdf.setFont("Helvetica-Bold", 14)
                    #y_position += 50 
                    pdf.drawString(100, y_position, "Achievements Data:")
                    y_position += 20
                    pdf.setFont("Helvetica", 12)
                    for record in achievements_data:
                        pdf.drawString(100, y_position, f"Achievement: {record[2]}             Reward: {record[4]}")
                        y_position += 20
                else:
                    pdf.setFont("Helvetica", 12)
                    pdf.setFont("Helvetica-Bold", 12)
                    pdf.drawString(100, y_position, "No Achievements Data Available for this semester")
                    y_position += 20
                # Query to fetch data for sgpa
                
                pdf.showPage()
                pdf.save()
                messagebox.showinfo("Success", "PDF saved successfully!", parent=self.root)
        except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
            
    def make_transparent(self, img, alpha):
        """Modify the image to make it transparent."""
        assert 0 <= alpha <= 1, "Alpha must be between 0 and 1"
        transparent_img = Image.new("RGBA", img.size)
        for x in range(img.width):
            for y in range(img.height):
                r, g, b, a = img.getpixel((x, y))
                new_a = int(a * alpha)  # Adjust transparency
                transparent_img.putpixel((x, y), (r, g, b, new_a))
                return img


    def close_current_window(self):
        if hasattr(self, 'new_win'):
            self.new_win.destroy()
    

    def home(self):
        if hasattr(self, 'new_win'):
            self.new_win.destroy()


    def minimize_child_window(self, event=None):
        """Minimize the child window when the main window is minimized."""
        if self.new_win is not None and self.new_win.winfo_exists():
            self.new_win.withdraw()  # Minimize (hide) the child window
        

    def restore_child_window(self, event=None):
        """Restore the child window when the main window is restored."""
        if self.new_win is not None and self.new_win.winfo_exists():
            self.new_win.deiconify()  # Restore the child window
        


    def add_marks(self):
        self.close_current_window()
        self.new_win=CTkToplevel(self.root)
        self.new_win.overrideredirect(True)
        self.new_obj=mark(self.new_win)
        self.new_win.focus_force()
        self.new_win.attributes('-topmost', True)


        
    def add_skills(self):
        self.close_current_window()
        self.new_win=CTkToplevel(self.root)
        self.new_win.overrideredirect(True)
        self.new_obj=skill(self.new_win)
        self.new_win.focus_force()
        self.new_win.attributes('-topmost',True)
        

    def add_achievemnts(self):
        self.close_current_window()
        self.new_win=CTkToplevel(self.root)
        self.new_win.overrideredirect(True)
        self.new_obj=achiev(self.new_win)
        self.new_win.focus_force()
        self.new_win.attributes('-topmost',True)
        

    def add_graph(self):
        self.close_current_window()
        self.new_win=CTkToplevel(self.root)
        self.new_win.overrideredirect(True)
        self.new_obj=grp(self.new_win)
       
       
      
        self.new_win.focus_force()
        self.new_win.attributes('-topmost',True)
    

    
    def add_feedback(self):
        self.close_current_window()
        self.new_win=CTkToplevel(self.root)
        self.new_win.overrideredirect(True)
        self.new_obj=fdb(self.new_win)
        self.new_win.focus_force()
        self.new_win.attributes("-topmost",True)

    def add_certificate(self):
        self.close_current_window()
        self.new_win=CTkToplevel(self.root)
        self.new_win.overrideredirect(True)
        self.new_obj=certify(self.new_win)
        self.new_win.focus_force()
        self.new_win.attributes("-topmost",True)
       

if __name__ == "__main__":
    root = CTk()
    obj = PPT(root)
    root.mainloop()
