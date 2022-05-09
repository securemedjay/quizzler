from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):  # quiz_brain: QuizBrain to indicate quiz_brain is a QuizBrain object
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.quiz = quiz_brain

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, font=FONT, text="", width=280)
        self.high_score_text = self.canvas.create_text(150, 50, font=("Arial", 20, "bold"), text="", width=280,
                                                       fill="green")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.current_score_label = Label(text="", bg=THEME_COLOR, fg="white")
        self.current_score_label.grid(row=0, column=1)
        self.high_score_label = Label(text=f"High Score: {self.quiz.high_score}", bg=THEME_COLOR, fg="white")
        self.high_score_label.grid(row=0, column=0)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_img, highlightthickness=0, command=self.is_right)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.is_wrong)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.current_score_label.config(text=f"Current Score: {self.quiz.score}/{self.quiz.question_number}")
        if self.quiz.still_has_questions():
            quiz_text = self.quiz.next_question()  # self.quiz is a QuizBrain object calling a QuizBrain method
            self.canvas.itemconfig(self.question_text, text=quiz_text)

        # Game ending
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")

            self.true_button.config(state="disabled")  # state="disabled" disables the button
            self.false_button.config(state="disabled")

            if self.quiz.is_new_high_score():
                self.canvas.itemconfig(self.high_score_text,
                                       text=f"Congratulations!!! You have a new high score")

            self.quiz.write_high_score()
            self.high_score_label.config(text=f"High Score: {self.quiz.high_score}")

    def is_right(self):
        is_right_answer = self.quiz.check_answer("True")
        self.give_feedback(is_right_answer)

    def is_wrong(self):
        is_right_answer = self.quiz.check_answer("False")
        self.give_feedback(is_right_answer)

    def give_feedback(self, is_right_answer):
        if is_right_answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
