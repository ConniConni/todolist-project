from todo_list import main
from todo_list import logger_config


if __name__ == "__main__":

    # アプリケーションのログ設定処理を呼び出す
    logger_config.setup_logging()
    # アプリのエントリーポイントを実行する
    main.run_app()
