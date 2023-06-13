from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain, question_bank):
        self.quiz = quiz_brain
        self.qtn_bank = question_bank

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.resizable(False, False)
        self.score_label = Label(text=f"Score: 0/10", bg=THEME_COLOR, fg="white", font=("Arial", 12))
        self.score_label.grid(row=0, column=1, pady=(0, 10), padx=(70, 0))

        false_btn_img = PhotoImage(file="images/false.png")
        true_btn_img = PhotoImage(file="images/true.png")

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="#fff", highlightthickness=0)

        self.qtn_text = self.canvas.create_text(150, 125, text="Question", width=280, fill=THEME_COLOR, font=("Arial", 18, "italic"))

        self.canvas.grid(column=0, row=1, columnspan=2)

        # Create wrong button
        # Same background color as active background (activebackground="#b1ddc6") and sunken relief removes animation on button
        self.wrong_btn = Button(image=false_btn_img, highlightthickness=0, activebackground="#ee665d", relief='sunken',
                           borderwidth=0, bg="#ee665d", width=142, command=self.false_pressed)

        # Define wrong button position on window
        self.wrong_btn.grid(column=0, row=2, padx=(3, 5), pady=20)

        # Create right button
        self.right_btn = Button(image=true_btn_img, highlightthickness=0, activebackground="#29b677", relief='sunken',
                           borderwidth=0, bg="#29b677", width=145, command=self.true_pressed)

        # Define right button position on window
        self.right_btn.grid(column=1, row=2, padx=(5, 0), pady=20)

        self.get_next_qtn()

        self.window.mainloop()

    def get_next_qtn(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}/{len(self.qtn_bank)}")
            self.canvas.itemconfig(self.qtn_text, text=question_text)
        else:
            self.canvas.itemconfig(self.qtn_text, text=f"You've reached the end of the quiz. Your score total is {self.quiz.score}/{len(self.qtn_bank)}")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right= self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#29b677")
        else:
            self.canvas.config(bg="#ee665d")
        self.window.after(1000, self.get_next_qtn)
