from tkinter import *
THEME_COLOR = "#375362"
class QuizzUi:
    def __init__(self):
        self.window = Tk()
        self.window.config(padx=20,pady=20,background=THEME_COLOR)
        
        self.canvas = Canvas(width=300, height=250, background='white')
        self.canvas.grid(column=0,row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text((150,95),text="Question goes here!",font=('Ariel',20,'italic'),width=280)
        
        self.score_text = Label(fg='white',text='Score:0')
        self.score_text.config(background=THEME_COLOR)
        self.score_text.grid(row=0,column=1)
        
        correct_image = PhotoImage(file="./images/true.png")
        wrong_image = PhotoImage(file="./images/false.png")
        
        self.right_button = Button(self.window,
                                   image=correct_image,
                                   highlightthickness=0)
        self.wrong_button = Button(self.window, image=wrong_image,
                                   highlightthickness=0)
        
        self.right_button.grid(column=1,row=2)
        self.wrong_button.grid(column=0,row=2)
        
        self.window.mainloop()
        