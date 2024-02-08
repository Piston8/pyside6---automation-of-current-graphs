# Импорт стандартной библиотеки
import sys
# Импорт библиотеки графического пользовательского интерфейса
from PySide6.QtWidgets import QApplication
# Импорт модулей программы
from modules.main import MainWindow

if __name__ == '__main__':
    # Инициализация приложения
    app = QApplication.instance() or QApplication(sys.argv)
    # Загрузка главного окна приложения
    window = MainWindow()
    # Исполнение приложения (проверка версии)
    try:
        app_exec = app.exec
    except AttributeError:
        app_exec = app.exec_
    # Исполнение приложения
    sys.exit(app_exec())
