
#jsonファイルを読みこみ、実行ごとに取得したjsonのリストからランダムで正解の問題を生成するコード
#英単語

import json
import random

json_file_path = 'C:/Users/m20279/Downloads/eitango.json'

with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

if isinstance(data, list):
    selected_data = random.choice(data)
    moji_value = selected_data.get('moji', '')
    imi_value = selected_data.get('imi', '')
else:
    moji_value = data.get('moji', '')
    imi_value = data.get('imi', '')

quiz_sentence = f'「{moji_value}」の意味は\n「{imi_value}」である.\n'

print(quiz_sentence)