""" This module specifies the Flask web app server for the quizzer application"""
from flask import Flask, render_template

import quizzer
from questions import QUESTIONS

def create_app():
    """ Factory method for creating the flask app server"""
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        """Return the homepage from templates/index.html"""
        return render_template('index.html', question=QUESTIONS[0])

    @app.route('/api/random-question')
    def get_random_question():
        """
            Return a random question from the quizzer module as a dictionary.

            Supports requests of the form http://<host>:<port>/api/random-question
            For example, http://localhost:5000/api/random-question
    
        Returns:
            dict: dictionary containing the http response, status code, and the question as a dict (question_id, question_text, choices, and answer_index).
        """

        return vars(quizzer.get_random_question())

    @app.route('/api/question/<question_id>/answer/<int:answer>')
    def check_answer(question_id: str, answer: int):
        """Returns whether the answer is correct for the given question wrapped in a dictionary object.

        Args:
            question_id (str): the unique identifer (UUID) of the question
            answer (int): the index of the answer in the choices list

        Returns:
            dict: dictionary containing the http responses, status code, and a boolean of whether the answer is correct.
        """
        try:
            return {
                'message': "Ok",
                'status': 200,
                'is_correct': quizzer.check_answer(question_id, answer)
            }
        except ValueError as e:
            return {
                'message': "Bad request!",
                'status': 400,
                'Error': str(e),
            }, 400

    @app.route('/api/question/<question_id>')
    def get_question(question_id: str):
        """Returns the question with the given question_id wrapped in a dictionary.

        Args:
            question_id (str): the unique identifier (UUID) of the quesiton

        Returns:
            dict: dictionary containing the http response, status code, and the question as a dict (question_id, question_text, choices, and answer_index).
        """
        try:
            return {
                'message': "Ok",
                'status': 200,
                'question': vars(quizzer.get_question(question_id))
            }
        except ValueError as e:
            return {
                'message': "Bad request!",
                'status': 400,
                'Error': str(e),
            }, 400

    return app
