from tkinter import *
from PIL import Image, ImageTk
name = []
class TitlePage:
 def __init__(self, parent):

   background_color="DarkBlue"
  
   self.play_button = Button(parent, text="PLAY", font=("Courier", "13", "bold"),bg = "Green",command=self.name_collection)
   self.play_button.place(x=280, y=375,height= 50, width=155)

   self.exit_button = Button(parent, text="EXIT", font=("Courier", "13", "bold"), bg="Red")
   self.exit_button.place(x=65, y=375,height= 50, width=155)

   self.username_box=Entry(parent,borderwidth=2)
   self.username_box.place(x=171.8,y=297.5,height= 25, width=155)
 def name_collection(self):
   name=self.username_box.get()
   names.append(name)
   self.quiz_frame.destroy()
   TitlePage(root)  
class QuizPage:
 def __init__(self, parent):
   background_color=("DarkBlue")
   
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