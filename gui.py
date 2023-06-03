from quiz_brain import QuizBrain
from tkinter import *
THEME_COLOR = "#375362"


class QuizzUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(padx=20,pady=20,background=THEME_COLOR)
        
        self.canvas = Canvas(width=300,height=250,background='white')
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
        self.question_text = self.canvas.create_text((150,95),text="Question txt here!",font=('Ariel',20,'italic'),width=280)
        
        self.score_text = Label(fg='white',text=f"Score:0")
        self.score_text.config(background=THEME_COLOR)
        self.score_text.grid(row=0,column=1)
        
        correct_image = PhotoImage(file="./images/true.png") 
        wrong_image = PhotoImage(file="./images/false.png")
        
        self.right_button = Button(self.window,image=correct_image,
                                   highlightthickness=0,
                                   command=lambda: self.submit_answer(answer='True'))
        self.wrong_button = Button(self.window,image=wrong_image, 
                                   highlightthickness=0,
                                   command=lambda: self.submit_answer(answer='False'))
        
        self.right_button.grid(column=1,row=2)
        self.wrong_button.grid(column=0,row=2)
        self.get_next_question()
        
        self.window.mainloop()
       
    def get_next_question(self):  
        q_text = self.quiz.next_question()    
        self.score_text.config(text=f"Score:{self.quiz.score}")
        self.canvas.itemconfig(self.question_text,text=q_text) 
    
    def submit_answer(self,answer:str):
        
        if self.quiz.check_answer(user_answer=answer):
            
            self.window.config(background='green')
            self.window.after(500,self.reset_background_color)
            
            
            
        else:
            self.window.config(background='red')
            self.window.after(500,self.reset_background_color)            
           
       
    def reset_background_color(self):
        self.window.config(background=THEME_COLOR)
        
        if self.quiz.still_has_questions():
            self.get_next_question()        
        else:
            self.canvas.itemconfig(self.question_text,text="Game over.")
            self.wrong_button.config(state='disabled') 
            self.right_button.config(state='disabled')   