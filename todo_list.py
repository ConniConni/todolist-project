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

    print("==== 新規タスクを追加します ====")
    print("タスクを入力してください")
    input_task = input(">>> ")
    task_list.append(input_task)

    # TODO sho_task_list実装後、todo.csvにすでに値が登録してある場合、タスクを読み込み、task_listに代入する処理を追加

    with open(CSV_FILE, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(task_list)


def show_task_list():
    """
    タスク一覧を表示する関数
    CSVファイルからタスクを読み込みタスク一覧を表示
    CSVファイルもしくはCSVファイルの中身がない場合は新規タスク登録を促すプロンプトを表示
    """
    print("==== タスク一覧を表示します ====")


def delete_task():
    """
    タスク一覧からタスク選択し削除する関数
    番号の入力を促すプロンプトを表示し該当のタスク一覧から削除する
    残ったタスク一覧をCSVファイルに上書きする
    """
    print("==== タスクを削除します ====")


if __name__ == "__main__":
    main()
