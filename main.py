import monitoring
import telegram_bot
import gui
import threading

if __name__ == "__main__":
    # Запускаем мониторинг файлов в отдельном потоке, без параметров
    monitoring_thread = threading.Thread(target=monitoring.start_monitoring)
    monitoring_thread.daemon = True
    monitoring_thread.start()

    # Запускаем телеграм-бота в отдельном потоке
    telegram_bot_thread = threading.Thread(target=telegram_bot.run_telegram_bot)
    telegram_bot_thread.daemon = True
    telegram_bot_thread.start()

    # Запускаем графический интерфейс
    gui_thread = threading.Thread(target=gui.run_gui)
    gui_thread.daemon = True
    gui_thread.start()

    # Основной поток
    while True:
        pass
