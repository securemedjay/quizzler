import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.high_score = self.read_high_score()
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)  # to convert encoded text into human-readable format
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def read_high_score(self) -> int:
        try:
            with open("high_score.txt") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            with open("high_score.txt", "w") as file:
                file.write(str(self.score))
            return self.score
        else:
            return self.high_score

    def is_new_high_score(self) -> bool:
        if self.score > self.high_score:
            return True
        else:
            return False

    def write_high_score(self):
        if self.is_new_high_score():
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))

