import logging

from .utils.file_handler import load_tasks
from .utils.file_handler import save_tasks


logger = logging.getLogger(__name__)


def add_task():
    """
    新規タスクを登録する関数
    ユーザーに新規タスクの入力を促すプロンプトを表示
    入力されたタスクはCSVファイルに書き込む
    """

    task_list = load_tasks()

    logger.info("新規タスク処理を開始しました。")
    print("==== 新規タスクを追加します ====")

    while True:
        print("タスクを入力してください")
        input_task = input(">>> ")
        # 入力値の前後の空白文字を削除する
        register_task = input_task.strip()

        if register_task:
            break
        else:
            logger.warning("入力値不正: 新規タスクが空文字で入力されました。")
            print("エラー: タスクは1文字以上で入力してください")

    # タスクをCSVに保存する
    task_list.append(register_task)
    save_tasks(task_list)
    logger.info(f"タスク'{register_task}'を登録しました。")
    logger.info("新規タスク処理を終了しました。")
    print(f"タスク'{register_task}'を登録しました")


def show_task_list():
    """
    タスク一覧を取得する関数
    CSVファイルからタスクを読み込みタスク一覧を取得し返却
    CSVファイルもしくはCSVファイルの中身がない場合は新規タスク登録を促すプロンプトを表示
    """
    logger.info("タスク一覧取得処理を開始しました。")
    print("==== タスク一覧を取得します ====")

    try:
        task_list = load_tasks()
        # CSVファイルが存在しない、もしくは空の場合はmain()関数に戻る
        if not task_list:
            print("エラー: 新規タスク追加をしてください")
            return
        # enumerate()関数 enumerate("第1引数: リストなどのイテラブルオブジェクト","第2引数: インデックス開始番号")
        logger.info(f"タスク一覧取得結果: {task_list}")
        for i, task in enumerate(task_list, 1):
            print(f"{i}: {task}")

    finally:
        logger.info("タスク一覧取得処理を終了しました。")


def delete_task():
    """
    タスク一覧からタスクを選択し削除する関数
    番号の入力を促すプロンプトを表示し該当のタスク一覧から削除する
    残ったタスク一覧をCSVファイルに上書きする
    """
    logger.info("タスク削除処理を開始しました。")
    print("==== タスクを削除します ====")

    try:
        task_list = load_tasks()
        # CSVファイルが存在しない、もしくは空の場合はmain()関数に戻る
        if not task_list:
            logger.warning("不正な操作: タスク一覧がない状態で一覧取得が行われました。")
            logger.info("タスク削除処理を終了しました。")
            print("エラー:新規タスク追加をしてください")
            return

        for i, task in enumerate(task_list, 1):
            print(f"{i}: {task}")

        while True:
            print("削除するタスクの番号を入力してください")
            try:
                # ユーザー入力値から削除対象のindexを取得する
                input_task = int(input(">>> ")) - 1
                alert_delete_task = task_list[input_task]
                # task_listから該当のタスクを削除する
                task_list.pop(input_task)
                logger.info(f"タスク一覧から'{alert_delete_task}'を削除しました。")
                break

            except ValueError as e:
                logger.warning(f"{e}: 削除対象を選ぶのに整数以外が入力されました。")
                print("エラー: 整数を入力してください")

            except IndexError as e:
                logger.warning(
                    f"{e}: 削除対象を選ぶのにリスト外の整数が入力されました。"
                )
                print(
                    "エラー: 該当のタスクがありません リストの中から数字を選んでください"
                )

        try:
            # task_listのタスクをCSVファイルに保存する
            save_tasks(task_list)
        except IOError as e:
            logger.error(f"{e}: ファイルへの書き込みに失敗しました。")
            print(f"エラー: ファイルへの書き込みに失敗しました - {e}")
        else:
            logger.info(f"メモリから'{alert_delete_task}'を削除しました")

            print(f"CSVファイルから'{alert_delete_task}'を削除しました")

    finally:
        logger.info("タスク削除処理を終了しました。")
