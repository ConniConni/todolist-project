def main():
    """todoリストアプリのメイン関数"""

    while True:
        print("==== 選択メニューの番号を入力してください ====")
        print("1: 新規タスク追加")
        print("2: タスク一覧表示")
        print("3: タスク削除")
        print("4: 終了")

        choice_mode = int(input(">>> "))

        if choice_mode == 1:
            print("==== 新規タスクを追加します ====")
        if choice_mode == 2:
            print("==== タスク一覧を表示します ====")
        if choice_mode == 3:
            print("==== タスクを削除します ====")
        if choice_mode == 4:
            print("==== アプリを終了します ====")
            break


if __name__ == "__main__":
    main()
