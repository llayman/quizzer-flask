""" This module specifies the Flask web app server for the quizzer application"""
from flask import Flask, render_template

import quizzer

def create_app():
    """ Factory method for creating the flask app server"""
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return render_template('index.html')

    @app.route('/api/random-question')
    def get_random_question():
        return vars(quizzer.get_random_question())

    @app.route('/api/question/<int:question_id>/answer/<int:answer>')
    def check_answer(question_id: int, answer: int):
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

    @app.route('/api/question/<int:question_id>')
    def get_question(question_id: int):
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
