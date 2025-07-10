import csv


CSV_FILE = "todo.csv"


def load_tasks():
    """CSVファイルを読み込み、読み取ったタスクをリストに追加し返す関数"""

    try:
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            return [row[0] for row in reader if row]

    except FileNotFoundError:
        return []


def save_tasks(task_list):
    """task_listのタスクをCSVに書き込む関数"""

    with open(CSV_FILE, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        for task in task_list:
            # writerow()メソッドはイテラブルな引数を要求する
            # 文字列もイテラブルなため、リストにしないとタスクが1文字ずつカンマ区切りで書き込まれてしまう
            writer.writerow([task])
