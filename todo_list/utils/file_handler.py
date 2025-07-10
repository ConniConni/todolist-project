import csv
import logging

CSV_FILE = "todo.csv"

logger = logging.getLogger(__name__)


def load_tasks():
    """CSVファイルを読み込み、読み取ったタスクをリストに追加し返す関数"""
    logger.info("CSVファイル読み込み処理を開始しました。")

    try:
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            return [row[0] for row in reader if row]

    except FileNotFoundError as e:
        logger.error(f"{e}: ファイルの読み取りに失敗しました。")
        return []

    finally:
        logger.info("CSVファイル読み込み処理を終了しました。")


def save_tasks(task_list):
    """task_listのタスクをCSVに書き込む関数"""

    logger.info("CSVファイル書き込み処理を開始しました。")

    with open(CSV_FILE, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        for task in task_list:
            # writerow()メソッドはイテラブルな引数を要求する
            # 文字列もイテラブルなため、リストにしないとタスクが1文字ずつカンマ区切りで書き込まれてしまう
            writer.writerow([task])

    logger.info("CSVファイル書き込み処理を終了しました。")
