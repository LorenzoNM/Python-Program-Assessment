from tkinter import *
from PIL import Image, ImageTk

names = []
class TitlePage:
 def __init__(self, parent):

   background_color="Grey"
 
   self.bg_image = Image.open("2.png")
   self.bg_image = self.bg_image.resize((515,515), Image.ANTIALIAS)
   self.bg_image = ImageTk.PhotoImage(self.bg_image) 
   self.title_frame=Frame(parent, bg = background_color, padx=200, pady=220)
   self.title_frame.grid()         
        
   self.bg_frame= Label(self.title_frame, image=self.bg_image)
   self.bg_frame.place(x=-305, y=-220, relwidth=6, relheight=6.8) 
    
   self.play_button = Button(self.title_frame, text="PLAY", font=("Helvetica", "13", "bold"), bg="green")
   self.play_button.grid(row=3, padx=20, pady=20)        



if __name__ == "__main__":
   system = Tk()
   system.title("NZ Road Rules Quiz")
   quiz_instance = TitlePage(system)
   system.mainloop()