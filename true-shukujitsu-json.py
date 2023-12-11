
#jsonファイルを読みこみ、実行ごとに取得したjsonのリストからランダムで正解の問題を生成するコード
#祝日

import json
import random

json_file_path = 'C:/Users/m20279/Downloads/shukujitsu.json'

with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

if isinstance(data, list):
    selected_data = random.choice(data)
    meisyo_value = selected_data.get('meisyo', '')
    date_value = selected_data.get('date', '')
else:
    meisyo_value = data.get('meisyo', '')
    date_value = data.get('date', '')

quiz_sentence = f'「{meisyo_value}」の意味は\n「{date_value}」である.\n'

print(quiz_sentence)