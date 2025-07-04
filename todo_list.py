import csv


CSV_FILE = "todo.csv"


def main():
    """todoリストアプリのメイン関数"""

    while True:
        print("==== 選択メニューの番号を入力してください ====")
        print("1: 新規タスク追加")
        print("2: タスク一覧表示")
        print("3: タスク削除")
        print("4: 終了")

        try:
            choice_mode = int(input(">>> "))
        except ValueError:
            print("エラー: 整数を入力してください")
            continue

        if choice_mode == 1:
            add_task()
        elif choice_mode == 2:
            show_task_list()
        elif choice_mode == 3:
            delete_task()
        elif choice_mode == 4:
            print("==== アプリを終了します ====")
            break
        else:
            print("エラー: 1~4までのいずれかの整数を入力してください")


def add_task():
    """
    新規タスクを登録する関数
    ユーザーに新規タスクの入力を促すプロンプトを表示
    入力されたタスクはCSVファイルに書き込む
    """

    task_list = []
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            task_list.append(row[0])

    print("==== 新規タスクを追加します ====")

    print("タスクを入力してください")
    input_task = input(">>> ")
    task_list.append(input_task)

    with open(CSV_FILE, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for task in task_list:
            # writerow()メソッドはイテラブルな引数を要求する
            # 文字列もイテラブルなため、リストにしないとタスクが1文字ずつカンマ区切りで書き込まれてしまう
            writer.writerow([task])


def show_task_list():
    """
    タスク一覧を表示する関数
    CSVファイルからタスクを読み込みタスク一覧を表示
    CSVファイルもしくはCSVファイルの中身がない場合は新規タスク登録を促すプロンプトを表示
    """
    print("==== タスク一覧を表示します ====")
    task_list = []  # CSVファイルからタスク一覧を受け取る空のリスト

    try:
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                task_list.append(row[0])

    except FileNotFoundError:
        print("エラー: CSVファイルがありません 新規タスク追加をしてください")
        return

    # CSVファイルの中身をチェックする
    if not task_list:
        print("エラー: CSVファイルの中身が空です 新規タスク追加をしてください")
        return

    # enumerate()関数 enumerate("第1引数: リストなどのイテラブルオブジェクト","第2引数: インデックス開始番号")
    for i, task in enumerate(task_list, 1):
        print(f"{i}: {task}")


def delete_task():
    """
    タスク一覧からタスクを選択し削除する関数
    番号の入力を促すプロンプトを表示し該当のタスク一覧から削除する
    残ったタスク一覧をCSVファイルに上書きする
    """
    print("==== タスクを削除します ====")

    task_list = []

    try:
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                task_list.append(row[0])
    except FileNotFoundError:
        print("エラー: CSVファイルがありません 新規タスク追加をしてください")
        return

    if not task_list:
        print("エラー: CSVファイルの中身が空です 新規タスク追加をしてください")
        return

    for i, task in enumerate(task_list, 1):
        print(f"{i}: {task}")

    while True:
        print("削除するタスクの番号を入力してください")
        try:
            # ユーザー入力値から削除対象のindexを取得する
            input_task = int(input(">>> ")) - 1
            alert_delete_task = task_list[input_task]
            # 該当のタスクを削除し、CSVを上書きする
            task_list.pop(input_task)
            break

        except ValueError:
            print("エラー: 整数を入力してください")

        except IndexError:
            print("エラー: 該当のタスクがありません リストの中から数字を選んでください")

    try:
        with open(CSV_FILE, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            for row in task_list:
                writer.writerow([row])
    except IOError as e:
        print(f"エラー: ファイルへの書き込みに失敗しました - {e}")
    else:
        print(f"タスク'{alert_delete_task}'を削除しました")


if __name__ == "__main__":
    main()
