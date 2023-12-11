#jsonファイルを読みこみ、実行ごとに取得したjsonのリストからランダムで正解の問題を生成するコード
#四字熟語

import json
import random

json_file_path = 'C:/Users/m20279/Downloads/yozizyukugo.json'

with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

def generate_false_true_quiz(data):
    if isinstance(data, list):
        # ランダムに正解のデータを選択
        selected_data = random.choice(data)
        moji_value = selected_data.get('moji', '')
        imi_value = selected_data.get('imi', '')

        # 不正解のデータを異なるランダムなデータから選択
        false_data = random.choice([d for d in data if d != selected_data])
        false_moji_value = false_data.get('moji', '')
        false_imi_value = false_data.get('imi', '')

        return moji_value, imi_value, false_moji_value, false_imi_value

    else:
        moji_value = data.get('moji', '')
        imi_value = data.get('imi', '')

        # 不正解のデータを異なるランダムなデータから選択
        false_data = random.choice([d for d in data if d != data])
        false_moji_value = false_data.get('moji', '')
        false_imi_value = false_data.get('imi', '')

        return moji_value, imi_value, false_moji_value, false_imi_value

moji_value, imi_value, false_moji_value, false_imi_value = generate_false_true_quiz(data)

# 〇×形式のクイズ文章生成
quiz_sentence = f'「{moji_value}」の意味は「{imi_value}」である.\n'
# 生成したクイズの文章を表示
print(quiz_sentence)
