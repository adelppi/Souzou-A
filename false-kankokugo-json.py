#jsonファイルを読みこみ、実行ごとに取得したjsonのリストからランダムで不正解の問題を生成するコード
#韓国語

import json
import random

json_file_path = 'C:/Users/m20279/Downloads/kankokugo.json'

with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

def generate_false_true_quiz(data):
    if isinstance(data, list):
        # ランダムに正解のデータを選択
        selected_data = random.choice(data)
        hangul_value = selected_data.get('hangul', '')
        nihongo_value = selected_data.get('nihongo', '')

        # 不正解のデータを異なるランダムなデータから選択
        false_data = random.choice([d for d in data if d != selected_data])
        false_hangul_value = false_data.get('hangul', '')
        false_nihongo_value = false_data.get('nihongo', '')

        return hangul_value, nihongo_value, false_hangul_value, false_nihongo_value

    else:
        hangul_value = data.get('hangul', '')
        nihongo_value = data.get('nihongo', '')

        # 不正解のデータを異なるランダムなデータから選択
        false_data = random.choice([d for d in data if d != data])
        false_hangul_value = false_data.get('hangul', '')
        false_nihongo_value = false_data.get('nihongo', '')

        return hangul_value, nihongo_value, false_hangul_value, false_nihongo_value

hangul_value, nihongo_value, false_hangul_value, false_nihongo_value = generate_false_true_quiz(data)

# 〇×形式のクイズ文章生成
quiz_sentence = f'「{hangul_value}」の意味は「{false_nihongo_value}」である.\n'
# 生成したクイズの文章を表示
print(quiz_sentence)
