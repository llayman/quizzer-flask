"""Backend logic for the quiz app"""

import random

from questions import MultipleChoiceQuestion, QUESTIONS

def get_random_question() -> MultipleChoiceQuestion:
    """Return a random question from the list of questions

    Returns:
        MultipleChoiceQuestion: the random question
    """
    return random.choice(QUESTIONS)

def check_answer(question_id: str, answer: int) -> bool:
    """Check if the answer provided is correct.

    Args:
        question_id (str): the unique id of the question in QUESTIONS
        answer (int): the index of the answer in the choices list

    Raises:
        ValueError: raised if the question_id is not a string or is not in the QUESTIONS list
        ValueError: raised if the answer is not an integer in the range of the choices list

    Returns:
        bool: True if the answer is correct, False otherwise
    """
    question = get_question(question_id)

    if not isinstance(answer, int) or not 0 <= answer < len(question.choices):
        raise ValueError(f"Provider an answer index between 0 and {len(question.choices) - 1}")

    return question.answer_index == answer

def get_question(question_id: str) -> MultipleChoiceQuestion:
    """Return a question by its id

    Args:
        question_id (str): the unique id of the question in QUESTIONS

    Raises:
        ValueError: raised if the question_id is not a string or is not in the QUESTIONS list

    Returns:
        MultipleChoiceQuestion: the question
    """
    if not isinstance(question_id, str):
        raise ValueError("Question id must be a string.")

    for question in QUESTIONS:
        if question.question_id == question_id:
            return question

    raise ValueError(f"Question with id {question_id} not found.")
