from tkinter import *
from PIL import Image, ImageTk

names = []
class TitlePage:
 def __init__(self, parent):

   background_color="Grey"
 
   self.bg_image = Image.open("2.png")
   self.bg_image = self.bg_image.resize((475,475), Image.ANTIALIAS)
   self.bg_image = ImageTk.PhotoImage(self.bg_image) 
   self.title_frame=Frame(parent, bg = background_color, padx=180, pady=200)
   self.title_frame.grid()         
        
   self.bg_frame= Label(self.title_frame, image=self.bg_image)
   self.bg_frame.place(x=-205, y=-190, relwidth=3, relheight=7) 
    
   self.play_button = Button(self.title_frame, text="PLAY", font=("Courier", "13", "bold"), bg="green")
   self.play_button.place(x=170, y=170)

   self.exit_button = Button(self.title_frame, text="EXIT", font=("Courier", "13", "bold"), bg="Red")
   self.exit_button.place(x=-30, y=170)
   
   self.entry_box=Entry(self.title_frame)
   self.entry_box.grid(row=2,padx=20, pady=20)

if __name__ == "__main__":
   system = Tk()
   system.title("Shooting Game Quiz")
   quiz_instance = TitlePage(system)
   system.mainloop()