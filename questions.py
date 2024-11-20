"""This module defines study questions for the app"""

import uuid

class MultipleChoiceQuestion:
    """A class to represent a multiple choice question"""
    def __init__(self, question_id: str, question_text: str,  answer_index: int, choices: list[str]):
        """Constructor for MultipleChoiceQuestion

        Args:
            question_id (str): The unique identifier for the question
            question_text (str): The question to be asked
            answer_index (int): The index of the correct answer in the choices list
            choices (list[str]): the list of choices for the question
        """
        self.question_id = question_id
        self.question_text = question_text
        self.answer_index = answer_index
        self.choices = choices

    def __repr__(self) -> str:
        return f"MultipleChoiceQuestion({self.question_id}, {self.question_text}, {self.answer_index}, {self.choices})"


QUESTIONS = [
    MultipleChoiceQuestion(str(uuid.uuid4()),  # Generate a unique ID for the question
                            "What is the capital of England?",
                           1,
                           ["Paris", "London", "Berlin", "Madrid"]),
    MultipleChoiceQuestion(str(uuid.uuid4()),  # Generate a unique ID for the question
                           "Who invented Git?",
                           0,
                           ["Linus Torvalds", "Bill Gates", "Steve Jobs", "Jeff Bezos"]),
]
