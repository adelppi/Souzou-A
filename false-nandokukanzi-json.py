#jsonファイルを読みこみ、実行ごとに取得したjsonのリストからランダムで不正解の問題を生成するコード
#難読漢字

import json
import random

json_file_path = 'C:/Users/m20279/Downloads/nandokukanzi.json'

with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

def generate_false_true_quiz(data):
    if isinstance(data, list):
        # ランダムに正解のデータを選択
        selected_data = random.choice(data)
        moji_value = selected_data.get('moji', '')
        yomi_value = selected_data.get('yomi', '')

        # 不正解のデータを異なるランダムなデータから選択
        false_data = random.choice([d for d in data if d != selected_data])
        false_moji_value = false_data.get('moji', '')
        false_yomi_value = false_data.get('yomi', '')

        return moji_value, yomi_value, false_moji_value, false_yomi_value

    else:
        moji_value = data.get('moji', '')
        yomi_value = data.get('yomi', '')

        # 不正解のデータを異なるランダムなデータから選択
        false_data = random.choice([d for d in data if d != data])
        false_moji_value = false_data.get('moji', '')
        false_yomi_value = false_data.get('yomi', '')

        return moji_value, yomi_value, false_moji_value, false_yomi_value

moji_value, yomi_value, false_moji_value, false_yomi_value = generate_false_true_quiz(data)

# 〇×形式のクイズ文章生成
quiz_sentence = f'「{moji_value}」の読み方は「{false_yomi_value}」である.\n'

# 生成したクイズの文章を表示
print(quiz_sentence)
