import logging


def setup_logging():
    """todoリストアプリのログ設定を行う関数"""

    # ルートロガーを取得
    logger = logging.getLogger()
    # ルートロガーのログレベルをINFOとする
    logger.setLevel(logging.INFO)
    # フォーマッタを設定
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "%Y-%m-%d %H:%M:%S",  # タイムスタンプの書式
    )
    # ハンドラを設定
    file_handler = logging.FileHandler("todo_list_log.txt", encoding="utf-8")
    file_handler.setFormatter(formatter)

    # ルートロガーに登録されているハンドラがなければハンドラを登録
    if not logger.handlers:
        logger.addHandler(file_handler)
