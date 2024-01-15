from flask import Flask, jsonify, redirect, url_for
import random
import json

app = Flask(__name__)


def load_json_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def generate_false_true_quiz(data, question_key, answer_key):
    if isinstance(data, list):
        selected_data = random.choice(data)
        question_value = selected_data.get(question_key, "")
        answer_value = selected_data.get(answer_key, "")

        false_data = random.choice([d for d in data if d != selected_data])
        false_question_value = false_data.get(question_key, "")
        false_answer_value = false_data.get(answer_key, "")

        return question_value, answer_value, false_question_value, false_answer_value
    else:
        question_value = data.get(question_key, "")
        answer_value = data.get(answer_key, "")

        false_data = random.choice([d for d in data if d != data])
        false_question_value = false_data.get(question_key, "")
        false_answer_value = false_data.get(answer_key, "")

        return question_value, answer_value, false_question_value, false_answer_value


def quiz_generator(file_path):
    data = load_json_data(file_path)
    question_key, answer_key = data[0].keys()

    (
        question,
        answer,
        alternative_question,
        alternative_answer,
    ) = generate_false_true_quiz(data, question_key, answer_key)

    is_correct = random.choice([True, False])

    if is_correct:
        return question, answer, ("o" if is_correct else "x")
    else:
        return question, alternative_answer, ("o" if is_correct else "x")


@app.route("/random", methods=["GET"])
def get_random():
    return redirect(
        url_for(
            random.choice(
                ["get_syuku", "get_nandoku", "get_yoji", "get_eigo", "get_hangu"]
            )
        )
    )


@app.route("/yoji", methods=["GET"])
def get_yoji():
    quiz = quiz_generator("./data/yozizyukugo.json")
    return jsonify({"question": f"「{quiz[0]}」の意味は「{quiz[1]}」である.\n", "answer": quiz[2]})


@app.route("/nandoku", methods=["GET"])
def get_nandoku():
    quiz = quiz_generator("./data/nandokukanzi.json")
    return jsonify(
        {"question": f"「{quiz[0]}」の読み方は「{quiz[1]}」である.\n", "answer": quiz[2]}
    )


@app.route("/syuku", methods=["GET"])
def get_syuku():
    quiz = quiz_generator("./data/shukujitsu.json")
    return jsonify(
        {
            "question": random.choice(
                [f"{quiz[0]}は{quiz[1]}である.\n", f"{quiz[1]}は{quiz[0]}である.\n"]
            ),
            "answer": quiz[2],
        }
    )


@app.route("/eigo", methods=["GET"])
def get_eigo():
    quiz = quiz_generator("./data/eitango.json")
    return jsonify({"question": f"「{quiz[0]}」の意味は「{quiz[1]}」である.\n", "answer": quiz[2]})


@app.route("/hangu", methods=["GET"])
def get_hangu():
    quiz = quiz_generator("./data/kankokugo.json")
    return jsonify({"question": f"「{quiz[0]}」の意味は「{quiz[1]}」である.\n", "answer": quiz[2]})


if __name__ == "__main__":
    app.run(debug=True)
