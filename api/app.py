from flask import Flask, jsonify
import random

app = Flask(__name__)

# クイズの問題と回答を含むJSONデータ
questions = [
    {
        "id": 1,
        "question": "問題1！",
        "answer": "False"
    },
    {
        "id": 2,
        "question": "問題2！",
        "answer": "True"
    }
]

@app.route('/oxquiz', methods=['GET'])
def get_quiz():
    random_question = random.choice(questions)
    return jsonify(random_question)

if __name__ == '__main__':
    app.run(debug=True)
