#jsonファイルを読みこみ、実行ごとに取得したjsonのリストからランダムで不正解の問題を生成するコード
#英単語
 
import json
import random

json_file_path = 'C:/Users/m20279/Downloads/eitango.json'

with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

def generate_false_true_quiz(data):
    if isinstance(data, list):
        # ランダムに正解のデータを選択
        selected_data = random.choice(data)
        english_value = selected_data.get('english', '')
        japanese_value = selected_data.get('japanese', '')

        # 不正解のデータを異なるランダムなデータから選択
        false_data = random.choice([d for d in data if d != selected_data])
        false_english_value = false_data.get('english', '')
        false_japanese_value = false_data.get('japanese', '')

        return english_value, japanese_value, false_english_value, false_japanese_value

    else:
        english_value = data.get('english', '')
        japanese_value = data.get('japanese', '')

        # 不正解のデータを異なるランダムなデータから選択
        false_data = random.choice([d for d in data if d != data])
        false_english_value = false_data.get('english', '')
        false_japanese_value = false_data.get('japanese', '')

        return english_value, japanese_value, false_english_value, false_japanese_value

english_value, japanese_value, false_english_value, false_japanese_value = generate_false_true_quiz(data)

# 〇×形式のクイズ文章生成
quiz_sentence = f'「{english_value}」の意味は「{false_japanese_value}」である.\n'
# 生成したクイズの文章を表示
print(quiz_sentence)
