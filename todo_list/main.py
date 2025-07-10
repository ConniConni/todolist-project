from .core import add_task
from .core import show_task_list
from .core import delete_task


def run_app():
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
