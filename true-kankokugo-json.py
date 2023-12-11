
#jsonファイルを読みこみ、実行ごとに取得したjsonのリストからランダムで正解の問題を生成するコード
#韓国語

import json
import random

json_file_path = 'C:/Users/m20279/Downloads/kankokugo.json'

with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

if isinstance(data, list):
    selected_data = random.choice(data)
    hangul_value = selected_data.get('hangul', '')
    nihongo_value = selected_data.get('nihongo', '')
else:
    hangul_value = data.get('hangul', '')
    nihongo_value = data.get('nihongo', '')

quiz_sentence = f'「{hangul_value}」の意味は\n「{nihongo_value}」である.\n'

print(quiz_sentence)