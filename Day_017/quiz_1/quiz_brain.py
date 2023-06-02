class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        player_answer = input(f"Q.{self.question_number}: {current_question.question} (True/False): ").lower()
        self.check_answer(player_answer, (current_question.answer))
    
    def check_answer(self, player_answer, correct_answer):
        if player_answer == correct_answer.lower():
            self.score += 1
            print(f"You're right. The answer is {correct_answer}.")
        else:
            print(f"That's wrong. The answer is {correct_answer}.")
        print(f"Your score: {self.score}/{self.question_number}")
        print()
