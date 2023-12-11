#jsonファイルを読みこみ、実行ごとに取得したjsonのリストからランダムで不正解の問題を生成するコード
#祝日

import json
import random

json_file_path = 'C:/Users/m20279/Downloads/shukujitsu.json'

with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

def generate_false_true_quiz(data):
    if isinstance(data, list):
        # ランダムに正解のデータを選択
        selected_data = random.choice(data)
        meisyo_value = selected_data.get('meisyo', '')
        date_value = selected_data.get('date', '')

        # 不正解のデータを異なるランダムなデータから選択
        false_data = random.choice([d for d in data if d != selected_data])
        false_meisyo_value = false_data.get('meisyo', '')
        false_date_value = false_data.get('date', '')

        return meisyo_value, date_value, false_meisyo_value, false_date_value

    else:
        meisyo_value = data.get('meisyo', '')
        date_value = data.get('date', '')

        # 不正解のデータを異なるランダムなデータから選択
        false_data = random.choice([d for d in data if d != data])
        false_meisyo_value = false_data.get('meisyo', '')
        false_date_value = false_data.get('date', '')

        return meisyo_value, date_value, false_meisyo_value, false_date_value

meisyo_value, date_value, false_meisyo_value, false_date_value = generate_false_true_quiz(data)

# 〇×形式のクイズ文章生成
quiz_sentence = f'「{meisyo_value}」は「{false_date_value}」である.\n'
# 生成したクイズの文章を表示
print(quiz_sentence)
