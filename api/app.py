from flask import Flask, jsonify
import random
import json

app = Flask(__name__)

def random_yozizyukugo():
    yozizyukugo_path = './data/yozizyukugo.json'

    with open(yozizyukugo_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if isinstance(data, list):
        selected_data = random.choice(data)
        moji_value = selected_data.get('moji', '')
        imi_value = selected_data.get('imi', '')
    else:
        moji_value = data.get('moji', '')
        imi_value = data.get('imi', '')

    quiz_sentence = f'「{moji_value}」の意味は\n「{imi_value}」である.\n'

    return quiz_sentence

@app.route('/oxquiz', methods=['GET'])
def get_quiz():
    random_question = random_yozizyukugo()
    return jsonify(
        {
            "question": random_question,
            "answer": "False"
        }
    )

if __name__ == '__main__':
    app.run(debug=True)
