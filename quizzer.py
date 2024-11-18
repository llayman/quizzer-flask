"""Backend logic for the quiz app"""

import random

from questions import MultipleChoiceQuestion, QUESTIONS

def get_random_question() -> MultipleChoiceQuestion:
    """Return a random question from the list of questions

    Returns:
        MultipleChoiceQuestion: the random question
    """
    return random.choice(QUESTIONS)

def check_answer(question_id: int, answer: int) -> bool:
    """Check if the answer provided is correct.

    Args:
        question_id (int): the index of the question in QUESTIONS
        answer (int): the index of the answer in the choices list

    Raises:
        ValueError: raised if the question_id is not an integer or not in the range of the questions list
        ValueError: raised if the answer is not an integer or not in the range of the choices list

    Returns:
        bool: True if the answer is correct, False otherwise
    """

    if not isinstance(question_id, int) or not 0 <= question_id < len(QUESTIONS):
        raise ValueError(f"Provide a question id between 0 and {len(QUESTIONS)}")
    
    question = QUESTIONS[question_id]

    if not isinstance(answer, int) or not 0 <= answer < len(question.choices):
        raise ValueError(F"Provider an answer index between 0 and {len(question.choices)}")
    
    return question.answer_index == answer

def get_question(question_id: int) -> MultipleChoiceQuestion:
    """Return a question by its id

    Args:
        question_id (int): the index of the question in QUESTIONS

    Raises:
        ValueError: raised if the question_id is not an integer or not in the range of the questions

    Returns:
        MultipleChoiceQuestion: the question
    """
    if not isinstance(question_id, int) or not 0 <= question_id < len(QUESTIONS):
        raise ValueError(f"Provide a question id between 0 and {len(QUESTIONS)}")

    return QUESTIONS[question_id]
