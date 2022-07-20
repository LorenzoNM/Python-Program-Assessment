from tkinter import *
import random
from PIL import Image, ImageTk
from tkinter import messagebox

names = []
global questions
global bg_image
asked = []
score = 0
questions = {
    1: [
        "What is this game", "Fortnite", "Halo", "CSGO", "Rainbow Six Siege",
        "Fortnite", 0
    ],
    2: ["Question", "Choice", "Choice", "Choice", "Choice", "", 1],
    3: ["Question", "Choice", "Choice", "Choice", "Choice", "Answer", 2],
    4: ["Question", "Choice", "Choice", "Choice", "Choice", "Answer", 2],
    5: ["Question", "Choice", "Choice", "Choice", "Choice", "Answer", 3],
    6: ["Question", "Choice", "Choice", "Choice", "Choice", "Answer", 3],
    7: ["Question", "Choice", "Choice", "Choice", "Choice", "Answer", 4],
    8: ["Question", "Choice", "Choice", "Choice", "Choice", "Answer", 1],
    9: ["Question", "Choice", "Choice", "Choice", "Choice", "Answer", 3],
    10: ["Question", "Choice", "Choice", "Choice", "Choice", "Answer", 1],
}


def random_gen():
    global inquiry
    inquiry = random.randint(1, 10)
    if inquiry not in asked:
        asked.append(inquiry)
    elif inquiry in asked:
        random_gen()


class TitlePage:
    def __init__(self, parent):
        background_color = "DarkBlue"

        self.play_button = Button(parent,
                                  text="PLAY",
                                  font=("Courier", "13", "bold"),
                                  bg="Green",
                                  command=self.name_collection,
                                  border=4)
        self.play_button.place(x=280, y=375, height=50, width=155)

        self.exit_button = Button(parent,
                                  text="EXIT",
                                  font=("Courier", "13", "bold"),
                                  bg="Red",
                                  border=4)
        self.exit_button.place(x=65, y=375, height=50, width=155)

        def tmp_text(all):
            self.username_box.delete(0, "end")

        self.username_box = Entry(parent, borderwidth=2)
        self.username_box.insert(0, "Enter Username here")
        self.username_box.place(x=160, y=287.5, height=50, width=180)
        self.username_box.bind("<FocusIn>", tmp_text)

    def name_collection(self):
        name = self.username_box.get()
        if str. isalpha(name):
          if len(name) < 1:
              names.append(name)
            
          elif len(name) > 9:
            messagebox.showerror("Error","Only Less Than 10 Letters")
            return()
        else:
          messagebox.showerror("Error","Only Letters and No Spaces and No Blanks")
          return()    
        self.exit_button.after(0, self.exit_button.destroy)
        self.play_button.after(0, self.play_button.destroy)
        self.username_box.after(0, self.username_box.destroy)
        QuizPage(system)


class QuizPage:
    def __init__(self, parent):
        background_color = "DarkBlue"
        global bg_image
        bg_image = Image.open("1.png")
        bg_image = bg_image.resize((500, 500), Image.ANTIALIAS)
        bg_image = ImageTk.PhotoImage(bg_image)
        bg_frame = Label(system, image=bg_image)
        bg_frame.place(x=0, y=2, relwidth=1, relheight=1)

        self.questions_text = Label(parent,
                                    text=questions[inquiry][0],
                                    font=("Courier", "16"),
                                    background="LightYellow")
        self.questions_text.place(x=120, y=30, height=50)

        self.VB1 = IntVar()
        self.bt1 = Radiobutton(parent,
                               text=questions[inquiry][1],
                               font=("Courier", "13"),
                               bg=background_color,
                               value=1,
                               padx=10,
                               pady=10,
                               variable=self.VB1,
                               indicator=1,
                               background="LightYellow",
                               border=4)
        self.bt1.place(x=35, y=300)

        self.bt2 = Radiobutton(parent,
                               text=questions[inquiry][2],
                               font=("Courier", "13"),
                               bg=background_color,
                               value=2,
                               padx=10,
                               pady=10,
                               variable=self.VB1,
                               indicator=1,
                               background="LightYellow",
                               border=4)
        self.bt2.place(x=290, y=300)

        self.bt3 = Radiobutton(parent,
                               text=questions[inquiry][3],
                               font=("Courier", "13"),
                               bg=background_color,
                               value=3,
                               padx=10,
                               pady=10,
                               variable=self.VB1,
                               background="LightYellow",
                               border=4)
        self.bt3.place(x=35, y=400)

        self.bt4 = Radiobutton(parent,
                               text=questions[inquiry][4],
                               font=("Courier", "13"),
                               bg=background_color,
                               value=4,
                               padx=10,
                               pady=10,
                               variable=self.VB1,
                               indicator=1,
                               background="LightYellow",
                               border=4)
        self.bt4.place(x=290, y=400)

        self.quiz_instance = Button(parent,
                                    text="Next",
                                    font=("Courier", "13", "bold"),
                                    bg="Green",
                                    border=4)
        self.quiz_instance.place(x=425, y=22.5, height=60, width=60)
        self.quit_button = Button(parent,
                                  text="Quit",
                                  font=("Courier", "13", "bold"),
                                  bg="red2",
                                  border=4)
        self.quit_button.place(x=20, y=22.5, height=60, width=60)


random_gen()
if __name__ == "__main__":
    system = Tk()
    system.geometry("500x500")

    system.title("Shooting Game Quiz")
    bg_image = Image.open("Title.png")
    bg_image = bg_image.resize((500, 500), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)
    bg_frame = Label(system, image=bg_image)
    bg_frame.place(x=0, y=2, relwidth=1, relheight=1)

    quiz_program = TitlePage(system)
    system.mainloop()
