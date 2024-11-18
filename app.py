from flask import Flask, render_template

import quizzer

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return render_template('index.html')


    @app.route('/random-question')
    def get_random_question():
        return vars(quizzer.get_random_question())
    
    @app.route('/question/<int:question_id>/answer/<int:answer>')
    def check_answer(question_id: int, answer: int):
        try:
            quizzer.check_answer(question_id, answer)
        except ValueError as e:
            return {
                'message': "Bad request!",
                'status': 400,
                'Error': str(e),
            }, 400
        

    @app.route('/question/<int:question_id>')
    def get_question(question_id: int):
        try:
            return vars(quizzer.get_question(question_id))
        except ValueError as e:
            return {
                'message': "Bad request!",
                'status': 400,
                'Error': str(e),
            }, 400

    return app
