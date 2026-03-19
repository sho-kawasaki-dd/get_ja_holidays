import json
import os
from datetime import date
import holidays

def generate_holidays():
    # 現在の年を取得し、前後数年分のデータを生成
    current_year = date.today().year
    years = [current_year - 1, current_year, current_year + 1, current_year + 2]
    
    jp_holidays = holidays.country_holidays('JP', years=years)
    
    holiday_list = []
    for date_obj, name in sorted(jp_holidays.items()):
        holiday_list.append({
            "date": date_obj.strftime('%Y-%m-%d'),
            "name": name
        })
    
    # publicディレクトリを作成してJSONを保存
    os.makedirs("public", exist_ok=True)
    with open("public/ja_holidays.json", "w", encoding="utf-8") as f:
        json.dump(holiday_list, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate_holidays()