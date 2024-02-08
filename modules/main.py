# Импорт библиотеки графического пользовательского интерфейса
from PySide6.QtWidgets import QMainWindow

# Импорт модулей программы
from .interface.ui_main_window import Ui_MainWindow
from .interface.fn_main_window_rab import UiFunctions


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # ------------------------------------------------------------------------------
        # Загрузка класса графического интерфейса главного окна Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Загрузка класса функциональности графического интерфейса
        self.ui_fn = UiFunctions(self)
        # ------------------------------------------------------------------------------

        # ------------------------------------------------------------------------------
        # Дополнительный функционал
        self.ui.about_qt_action.triggered.connect(qApp.aboutQt)
        self.ui.statusbar.showMessage('Добро пожаловать')
        self.show()
        # ------------------------------------------------------------------------------
