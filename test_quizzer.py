"""Unit tests for quizzer.py"""

import pytest
from quizzer import get_random_question, check_answer, get_question
from questions import MultipleChoiceQuestion, QUESTIONS

def test_get_random_question():
    """ Test get_random_question function """
    question = get_random_question()
    assert isinstance(question, MultipleChoiceQuestion)
    assert question in QUESTIONS

def test_check_answer_correct():
    """ Test check_answer function """
    # Test the correct answer index
    assert check_answer(0, 1) is True
    assert check_answer(0, 3) is False

def test_check_answer_invalid_question_id():
    """ Test check_answer function with invalid question id """
    with pytest.raises(ValueError) as e:
        check_answer("a", 0)
    assert str(e.value).startswith("Provide a question id between 0 and")

    with pytest.raises(ValueError) as e:
        check_answer(-1, 0)
    assert str(e.value).startswith("Provide a question id between 0 and")

    with pytest.raises(ValueError) as e:
        check_answer(len(QUESTIONS), 0)
    assert str(e.value).startswith("Provide a question id between 0 and")

def test_check_answer_invalid_answer():
    """ Test check_answer function with invalid answer index """
    with pytest.raises(ValueError) as e:
        check_answer(0, "a")
    assert str(e.value).startswith("Provider an answer index between 0 and")

    with pytest.raises(ValueError) as e:
        check_answer(0, -1)
    assert str(e.value).startswith("Provider an answer index between 0 and")

    with pytest.raises(ValueError) as e:
        check_answer(0, len(QUESTIONS[0].choices))
    assert str(e.value).startswith("Provider an answer index between 0 and")

def test_get_question():
    """ Test get_question function """
    question = get_question(0)
    assert isinstance(question, MultipleChoiceQuestion)
    assert question.question_text == QUESTIONS[0].question_text

def test_get_question_invalid_id():
    """ Test get_question function with invalid question id """
    with pytest.raises(ValueError) as e:
        get_question("a")
    assert str(e.value).startswith("Provide a question id between 0 and")

    with pytest.raises(ValueError) as e:
        get_question(-1)
    assert str(e.value).startswith("Provide a question id between 0 and")

    with pytest.raises(ValueError) as e:
        get_question(len(QUESTIONS))
    assert str(e.value).startswith("Provide a question id between 0 and")
