from tkinter import *
import random
from PIL import Image, ImageTk
names = []
global questions
asked = []
score=0
questions = {
    1: ["What is this game",
        "Fortnite",
        "Halo",
        "CSGO",
        "Rainbow Six Siege",
        "Fortnite", 0],
    2: ["Question",
        "Choice",
        "Choice",
        "Choice",
        "Choice",
        "", 1],
    3: ["Question",
        "Choice",
        "Choice",
        "Choice",
        "Choice",
        "Answer",2],
    4: ["Question",
        "Choice",
        "Choice",
        "Choice",
        "Choice",
        "Answer", 2],
    5: ["Question",
        "Choice",
        "Choice",
        "Choice",
        "Choice",
        "Answer", 3],
    6: ["Question",
        "Choice",
        "Choice",
        "Choice",
        "Choice",
        "Answer", 3],
    7: ["Question",
        "Choice",
        "Choice",
        "Choice",
        "Choice",
        "Answer", 4],
    8: ["Question",
        "Choice",
        "Choice",
        "Choice",
        "Choice",
        "Answer", 1],
    9: ["Question",
        "Choice",
        "Choice",
        "Choice",
        "Choice",
        "Answer", 3],
    10: ["Question",
        "Choice",
        "Choice",
        "Choice",
        "Answer", 1],}
def random_gen():
 global inquiry
 inquiry = random.randint(1, 10)
 if inquiry not in asked:
   asked.append(inquiry)
 elif inquiry in asked:
   random_gen()


class TitlePage:
 def __init__(self, parent):

   background_color="DarkBlue"
  
   self.play_button = Button(parent, text="PLAY", font=("Courier", "13", "bold"),bg = "Green", command=self.name_collection)
   self.play_button.place(x=280, y=375,height= 50, width=155)

   self.exit_button = Button(parent, text="EXIT", font=("Courier", "13", "bold"), bg="Red")
   self.exit_button.place(x=65, y=375,height= 50, width=155)
   def tmp_text(all):
     self.username_box.delete(0,"end")
   self.username_box=Entry(parent,borderwidth=2)
   self.username_box.insert(0, "Enter Username here")
   self.username_box.place(x=160, y=287.5,height= 50, width=180)

   self.username_box.bind("<FocusIn>", tmp_text)


       
 def name_collection(self):
   name=self.username_box.get()
   names.append(name)
   self.exit_button.after(0,self.exit_button.destroy)
   self.play_button.after(0,self.play_button.destroy)
   self.username_box.after(0,self.username_box.destroy)
   QuizPage(system)  

   
class QuizPage:
 def __init__(self, parent):
   background_color="DarkBlue"
   bg_image = Image.open("1.png")
   bg_image = bg_image.resize((500,500), Image.ANTIALIAS)
   bg_image = ImageTk.PhotoImage(bg_image) 
   bg_frame= Label(system, image=bg_image)
   bg_frame.place(x=0, y=2, relwidth=1, relheight=1)
   
   self.questions_text=Label(parent, text=questions[inquiry][0], font=("Tw Cen MT","16"),bg= background_color)
   self.questions_text.place(x=65, y=375,height= 50, width=155)


   self.var1 = IntVar()
   self.rb1= Radiobutton(parent, text=questions[inquiry][1], font=("Helvetica","12"),bg= background_color, value=1, padx=10, pady=10, variable=self.var1, indicator= 1, background = "light blue")
   self.rb1.grid(row=2, sticky=W)

   self.rb2= Radiobutton(parent, text=questions[inquiry][2], font=("Helvetica","12"),bg= background_color, value=2, padx=10, pady=10, variable=self.var1, indicator= 1, background = "light blue")
   self.rb2.grid(row=3, sticky=W)

   self.rb3= Radiobutton(parent, text=questions[inquiry][3], font=("Helvetica","12"),bg= background_color, value=3, padx=10, pady=10, variable=self.var1, background = "light blue")
   self.rb3.grid(row=4, sticky=W)

   self.rb4= Radiobutton(parent, text=questions[inquiry][4], font=("Helvetica","12"),bg= background_color, value=4, padx=10, pady=10, variable=self.var1, indicator= 1, background = "light blue")
   self.rb4.grid(row=5, sticky=W)

   self.quiz_instance=Button(parent, text="Confirm", font=("Helvetica","13","bold"), bg="SpringGreen3")
   self.quiz_instance.place(x=65, y=375,height= 50, width=155)

random_gen()
if __name__ == "__main__":
   system = Tk()
   system.geometry("500x500")

   system.title("Shooting Game Quiz")
   bg_image = Image.open("2.png")
   bg_image = bg_image.resize((500,500), Image.ANTIALIAS)
   bg_image = ImageTk.PhotoImage(bg_image) 
   bg_frame= Label(system, image=bg_image)
   bg_frame.place(x=0, y=2, relwidth=1, relheight=1)
   
   quiz_program = TitlePage(system)
   system.mainloop()