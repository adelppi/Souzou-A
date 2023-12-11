
#jsonファイルを読みこみ、実行ごとに取得したjsonのリストからランダムで正解の問題を生成するコード
#英単語

import json
import random

json_file_path = 'C:/Users/m20279/Downloads/eitango.json'

with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

if isinstance(data, list):
    selected_data = random.choice(data)
    english_value = selected_data.get('english', '')
    japanese_value = selected_data.get('japanese', '')
else:
    english_value = data.get('english', '')
    japanese_value = data.get('japanese', '')

quiz_sentence = f'「{english_value}」の意味は「{japanese_value}」である.\n'

print(quiz_sentence)