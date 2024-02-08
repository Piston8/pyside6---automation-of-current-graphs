# Импорт стандартных библиотек
import math  # Математические функции
from decimal import Decimal  # Точные числа

# Импорт библиотек анализа данных
import numpy as np  # Работа с массивами
from PySide6.QtCore import QSize
from scipy.signal import hilbert  # Анализ
from scipy.fft import fft, fftfreq

# Импорт библиотеки визуализации данных
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

# Импорт библиотеки графического пользовательского интерфейса
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QFileDialog, QWidget, QVBoxLayout, QMessageBox

# Импорт модулей программы
from .ui_main_window import Ui_MainWindow


class UiFunctions(QMainWindow):
    """ Класс функциональности пользовательского интерфейса """
    def __init__(self, parent: QMainWindow):  # Инициализация класса
        super(UiFunctions, self).__init__(parent)
        # Импорт пространства имен интерфейса
        self.app = parent
        self.ui: Ui_MainWindow = self.app.ui

        # ------------------------------------------------------------------------------
        # Инициализация переменных
        self.file_1, self.file_2, self.file_3 = [], [], []
        self.file_1_cor, self.file_2_cor, self.file_3_cor = [], [], []
        self.data_v, self.data_d = [0, 0], [0, 0]
        self.correction = 0

        self.envelope_1, self.envelope_2, self.envelope_3 = [], [], []
        self.smoothed_envelope_1, self.smoothed_envelope_2, self.smoothed_envelope_3 = [], [], []
        self.derivative_envelope_1, self.derivative_envelope_2, self.derivative_envelope_3 = [], [], []

        self.t_act, self.t_str, self.t_razg = [0, 0, 0], [0, 0, 0], [0, 0, 0]
        self.i_pusk, self.i_rab = [0, 0, 0], [0, 0, 0]
        self.isr_pusk, self.isr_rab = 0, 0
        self.mod = [0, 0, 0]
        self.mod_sr = 0
        self.peak_point = [0, 0, 0]
        # ------------------------------------------------------------------------------

        # ------------------------------------------------------------------------------
        self.ui.correction_groupBox.hide()
        # self.ui.phases_tabWidget.setTabText(self.phases_tabWidget.indexOf(self.phase_tab),)
        self.ui.phases_tabWidget.setTabText(self.ui.phases_tabWidget.indexOf(self.ui.phase_tab), "Спектральный анализ")
        self.f_c = 50  # Частота сетевой составляющей
        self.t_c = 1 / 50  # Период сетевой составляющей
        # ------------------------------------------------------------------------------

        # ------------------------------------------------------------------------------
        # Параметры главного окна
        self.app.setWindowTitle('Plot')
        self.app.setWindowIcon(QIcon('resources/icon.ico'))
        self.app_resolution()
        # ------------------------------------------------------------------------------

        # ------------------------------------------------------------------------------
        # Установка связей
        self.setup_initial_data()
        # ------------------------------------------------------------------------------

    def open_file_click(self):
        """ Выбор и открытие файла с данными """
        sender = self.sender()

        index = sender.objectName().split('_')[1]
        index_name = None
        index_file = None
        line_edit = None

        if index == '1':
            index_name = f'{index} (Фаза A)'
            line_edit = self.ui.file_1_lineEdit
            index_file = self.file_1
        elif index == '2':
            index_name = f'{index} (Фаза B)'
            line_edit = self.ui.file_2_lineEdit
            index_file = self.file_2
        elif index == '3':
            index_name = f'{index} (Фаза C)'
            line_edit = self.ui.file_3_lineEdit
            index_file = self.file_3

        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self.app, f'Открыть файл: {index_name}', '', 'Текстовые файлы (*.txt);;Все файлы (*)',
                                                   options=options)

        if file_name:
            if file_name.endswith('.txt'):
                self.open_file(index_file, file_name, line_edit)

    def open_file(self, index_file, file_name, line_edit):
        if file_name.endswith('.txt'):
            line_edit.setText(file_name)
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file.readlines():
                    parts = line.strip().split()
                    if len(parts) == 2:
                        signal_x = float(parts[0].replace(",", "."))
                        signal_y = float(parts[1].replace(",", "."))

                        index_file.append([signal_x, signal_y])

    def set_initial_data(self):
        self.open_file(self.file_1, r"C:\Files\Project\f_energy_auto\current_files\f_A.txt", self.ui.file_1_lineEdit)
        self.open_file(self.file_2, r"C:\Files\Project\f_energy_auto\current_files\f_B.txt", self.ui.file_2_lineEdit)
        self.open_file(self.file_3, r"C:\Files\Project\f_energy_auto\current_files\f_C.txt", self.ui.file_3_lineEdit)

        self.ui.data_lineEdit_1_1.setText("490")
        self.ui.data_lineEdit_1_2.setText("540")

        self.ui.data_lineEdit_2_1.setText("920")
        self.ui.data_lineEdit_2_2.setText("320")

    def setup_initial_data(self):
        """ Установка связей в приложение """
        # self.set_initial_data()
        self.ui.correction_doubleSpinBox.setValue(1)
        self.ui.reset_correction_pushButton.clicked.connect(lambda: self.ui.correction_doubleSpinBox.setValue(1))

        self.ui.file_1_pushButton.clicked.connect(self.open_file_click)
        self.ui.file_2_pushButton.clicked.connect(self.open_file_click)
        self.ui.file_3_pushButton.clicked.connect(self.open_file_click)

        self.ui.plot_pushButton.setEnabled(True)
        self.ui.plot_pushButton.clicked.connect(self.check_plot_data)

    def check_plot_data(self):
        """ Проверка входных данных """
        self.read_data()
        if self.data_v[0] != '' and self.data_v[1] != '' and self.data_d[0] != '' and self.data_d[1] != ''\
                and self.ui.file_1_lineEdit.text() != '' and self.ui.file_2_lineEdit.text() != ''\
                and self.ui.file_3_lineEdit.text() != '':
            self.plot_graphs()
        else:
            warning_dialog = QMessageBox(self.app)
            warning_dialog.setIcon(QMessageBox.Warning)
            warning_dialog.setText("Проверьте входные данные\n(не указаны файлы, данные)")
            warning_dialog.setWindowTitle("Предупреждение")
            warning_dialog.exec()

    def read_data(self):
        """ Чтение входных данных """
        self.correction = self.ui.correction_doubleSpinBox.value()
        self.data_v[0], self.data_v[1] = self.ui.data_lineEdit_1_1.text(), self.ui.data_lineEdit_1_2.text()
        self.data_d[0], self.data_d[1] = self.ui.data_lineEdit_2_1.text(), self.ui.data_lineEdit_2_2.text()

    def correction_data(self):
        """ Фильтр коррекции данных """
        # Сброс коррекционных значений
        self.file_1_cor, self.file_2_cor, self.file_3_cor = [], [], []

        # Коррекция значений файла 1
        for data in self.file_1:
            y_cor = data[1] * self.correction
            self.file_1_cor.append([data[0], y_cor])

        # Коррекция значений файла 2
        for data in self.file_2:
            y_cor = data[1] * self.correction
            self.file_2_cor.append([data[0], y_cor])

        # Коррекция значений файла 3
        for data in self.file_3:
            y_cor = data[1] * self.correction
            self.file_3_cor.append([data[0], y_cor])

    def plot_graphs(self):
        """ Чтение данных, построение графиков, заполнение таблицы """
        # Чтение данных
        #self.correction_data()

        # Построение базового графика
        self.create_base_graph(self.ui.base_tab_1, self.file_1, 'A')  # A
        self.create_base_graph(self.ui.base_tab_2, self.file_2, 'B')  # B
        self.create_base_graph(self.ui.base_tab_3, self.file_3, 'C')  # C

        # Построение основного графика
        self.create_main_graph(self.ui.main_tab_1, self.file_1, 'A')  # A
        self.create_main_graph(self.ui.main_tab_2, self.file_2, 'B')  # B
        self.create_main_graph(self.ui.main_tab_3, self.file_3, 'C')  # C

        # Построение графиков времени активации, страгивания, разгона
        self.create_time_graph(self.ui.time_tab_1, self.file_1, 'A')  # A
        self.create_time_graph(self.ui.time_tab_2, self.file_2, 'B')  # B
        self.create_time_graph(self.ui.time_tab_3, self.file_3, 'C')  # C

        # Построение графика фазы
        self.create_phase_detection_graph(self.ui.phase_tab_1, self.file_1, 'A')  # A
        self.create_phase_detection_graph(self.ui.phase_tab_2, self.file_2, 'B')  # B
        self.create_phase_detection_graph(self.ui.phase_tab_3, self.file_3, 'C')  # C

        # Построение графика модуляции
        self.create_modulation_graph(self.ui.modulation_tab_1, self.file_1, 'A')  # A
        self.create_modulation_graph(self.ui.modulation_tab_2, self.file_2, 'B')  # B
        self.create_modulation_graph(self.ui.modulation_tab_3, self.file_3, 'C')  # C



        # # Построение основного графика
        # self.create_main_graph(self.ui.main_tab_1, self.file_1_cor, 'A')  # A
        # self.create_main_graph(self.ui.main_tab_2, self.file_2_cor, 'B')  # B
        # self.create_main_graph(self.ui.main_tab_3, self.file_3_cor, 'C')  # C

        # # Построение графиков времени активации, страгивания, разгона
        # self.create_time_graph(self.ui.time_tab_1, self.file_1_cor, 'A')  # A
        # self.create_time_graph(self.ui.time_tab_2, self.file_2_cor, 'B')  # B
        # self.create_time_graph(self.ui.time_tab_3, self.file_3_cor, 'C')  # C

        # # Построение графика модуляции
        # self.create_modulation_graph(self.ui.modulation_tab_1, self.file_1_cor, 'A')  # A
        # self.create_modulation_graph(self.ui.modulation_tab_2, self.file_2_cor, 'B')  # B
        # self.create_modulation_graph(self.ui.modulation_tab_3, self.file_3_cor, 'C')  # C

        # # Построение графика фазы
        # self.create_phase_detection_graph(self.ui.phase_tab_1, self.file_1_cor, 'A')  # A
        # self.create_phase_detection_graph(self.ui.phase_tab_2, self.file_2_cor, 'B')  # B
        # self.create_phase_detection_graph(self.ui.phase_tab_3, self.file_3_cor, 'C')  # C

        # Заполнение таблицы
        self.fill_table()

    def fill_table(self):
        """ Заполнение таблицы значениями"""
        # ------------------------------------------------------------------------------
        # Временные параметры
        # Время активации
        self.ui.act_time_lineEdit.setText("{:.2f}".format(max(self.t_act)))
        # Время страгивания
        self.ui.str_time_lineEdit.setText("{:.2f}".format(max(self.t_str)))
        # Время разгона
        self.ui.razg_time_lineEdit.setText("{:.2f}".format(max(self.t_razg)))
        # Полное время
        self.ui.tp_time_lineEdit.setText("{:.2f}".format(max(self.t_act) + max(self.t_str) + max(self.t_razg)))
        # ------------------------------------------------------------------------------

        # ------------------------------------------------------------------------------
        # Токовые параметры
        # Пусковые токи
        self.ui.i1_pusk_lineEdit.setText("{:.2f}".format(self.i_pusk[0]))
        self.ui.i2_pusk_lineEdit.setText("{:.2f}".format(self.i_pusk[1]))
        self.ui.i3_pusk_lineEdit.setText("{:.2f}".format(self.i_pusk[2]))
        # Средний пусковой ток
        self.isr_pusk = Decimal(sum(self.i_pusk) / len(self.i_pusk))
        self.ui.isr_pusk_lineEdit.setText("{:.2f}".format(self.isr_pusk))
        # Сигма
        sigma_pusk = Decimal(abs(self.i_pusk[2] - self.i_pusk[0])) / self.isr_pusk
        self.ui.sigma_pusk_lineEdit.setText("{:.2f}".format(sigma_pusk))

        # Рабочие токи
        self.ui.i1_rab_lineEdit.setText("{:.2f}".format(self.i_rab[0]))
        self.ui.i2_rab_lineEdit.setText("{:.2f}".format(self.i_rab[1]))
        self.ui.i3_rab_lineEdit.setText("{:.2f}".format(self.i_rab[2]))
        # Средний рабочий ток
        self.isr_rab = Decimal(sum(self.i_rab) / len(self.i_rab))
        self.ui.isr_rab_lineEdit.setText("{:.2f}".format(self.isr_rab))
        # Сигма
        sigma_rab = Decimal(abs(self.i_rab[2] - self.i_rab[0])) / self.isr_rab
        self.ui.sigma_rab_lineEdit.setText("{:.2f}".format(sigma_rab))

        # Отношение пускового тока к рабочему
        self.ui.isr_pusk_isr_rab_lineEdit.setText("{:.2f}".format(self.isr_pusk / self.isr_rab))
        # ------------------------------------------------------------------------------

        # ------------------------------------------------------------------------------
        # Модуляция
        self.ui.mod1_lineEdit.setText("{:.4f}".format(self.mod[0]))
        self.ui.mod2_lineEdit.setText("{:.4f}".format(self.mod[1]))
        self.ui.mod3_lineEdit.setText("{:.4f}".format(self.mod[2]))
        # Средняя
        self.mod_sr = Decimal(sum(self.mod) / len(self.mod))
        self.ui.mod_sr_lineEdit.setText("{:.3f}".format(self.mod_sr))
        # Сигма
        sigma_mod = Decimal(abs(self.mod[2] - self.mod[0])) / self.mod_sr
        self.ui.sigma_mod_lineEdit.setText("{:.3f}".format(sigma_mod))
        # ------------------------------------------------------------------------------

        # ------------------------------------------------------------------------------
        # Параметры электродвигателя
        d_radians_per_sec = f"{int(self.data_d[0]) / 60:.2f}"  # Перевод об/мин в рад/с
        self.ui.spectr_d_lineEdit.setText(d_radians_per_sec)

        # Параметры Вентилятора
        v_radians_per_sec = f"{int(self.data_v[0]) / 60:.2f}"  # Перевод об/мин в рад/с
        self.ui.spectr_v_lineEdit.setText(v_radians_per_sec)
        # ------------------------------------------------------------------------------

    def create_base_graph(self, tab, data, phase=''):
        """ Базовые графики """
        layout = tab.layout()
        if layout:
            for i in reversed(range(layout.count())):
                layout.itemAt(i).widget().deleteLater()

        x_axis, y_axis = [i[0] for i in data], [i[1] for i in data]

        fig = Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        ax.scatter(x_axis, y_axis, label=f'Исходный сигнал ({phase})', color='b')

        ax.set_title(f'Диаграмма формы сигнала фаза {phase}')
        ax.set_xlabel('Время, с')
        ax.set_ylabel('Сила тока, А')
        ax.grid(True)

        widget = self.create_graph_widget(canvas)
        layout.addWidget(widget)

    def create_main_graph(self, tab, data, phase=''):
        """ Основные графики """
        layout = tab.layout()
        if layout:
            for i in reversed(range(layout.count())):
                layout.itemAt(i).widget().deleteLater()

        x_axis, y_axis = [i[0] for i in data], [i[1] for i in data]

        n_c = int(self.t_c / (x_axis[1] - x_axis[0]))  # Число точек в одном периоде

        # Огибающая
        envelope = []
        for i in range(0, len(y_axis), n_c):
            segment = y_axis[i:i + n_c]
            rms_value = np.sqrt(np.mean(np.square(segment)))
            envelope.extend([rms_value] * len(segment))

        # Сглаженная
        window_size = 25  # Скользящее среднее (10 - почти тоже самое, 50 - норм, 100 - как будто много)
        smoothed_envelope = np.convolve(envelope, np.ones(window_size) / window_size, mode='same')

        # Производная
        derivative = np.gradient(smoothed_envelope, x_axis)

        # Сглаживание производной
        derivative_envelope = np.zeros(len(derivative))
        derivative_envelope[0] = derivative[0]
        alpha = 0.001
        
        for i in range(1, len(derivative)):
            derivative_envelope[i] = alpha * derivative[i] + (1 - alpha) * derivative_envelope[i - 1]
            
        # Сохранение расчетов
        if phase == 'A':
            self.envelope_1 = envelope
            self.smoothed_envelope_1 = smoothed_envelope.tolist()
            self.derivative_envelope_1 = derivative_envelope.tolist()
        elif phase == 'B':
            self.envelope_2 = envelope
            self.smoothed_envelope_2 = smoothed_envelope.tolist()
            self.derivative_envelope_2 = derivative_envelope.tolist()
        elif phase == 'C':
            self.envelope_3 = envelope
            self.smoothed_envelope_3 = smoothed_envelope.tolist()
            self.derivative_envelope_3 = derivative_envelope.tolist()

        fig = Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        # ax.scatter(y_axis, x_axis, label=f'Исходный сигнал ({phase})', color='b')
        ax.plot(x_axis, envelope, label='Огибающая', color='black')  # Огибающая
        ax.plot(x_axis, smoothed_envelope, label='Огибающая (сглаженная)', color='g')  # Огибающая (сглаженная)
        # plt.plot(s_time, derivative, label='Производная', color='orange')  # Производная
        ax.plot(x_axis, derivative_envelope, label='Производная', color='r')  # Производная (масштабированная)

        ax.set_title('Огибающая, сглаженная, производная')
        ax.set_xlabel('Время, с')
        ax.set_ylabel('Сила тока, А')
        ax.grid(True)
        ax.legend()

        widget = self.create_graph_widget(canvas)
        layout.addWidget(widget)

    def create_time_graph(self, tab, data, phase=''):
        """ Графики времени активации, страгивания, разгона """
        layout = tab.layout()
        if layout:
            for i in reversed(range(layout.count())):
                layout.itemAt(i).widget().deleteLater()

        x_axis, y_axis = [i[0] for i in data], [i[1] for i in data]

        envelope, smoothed_envelope, derivative_envelope = None, None, None
        if phase == 'A':
            envelope = self.envelope_1
            smoothed_envelope = self.smoothed_envelope_1
            derivative_envelope = self.derivative_envelope_1
        elif phase == 'B':
            envelope = self.envelope_2
            smoothed_envelope = self.smoothed_envelope_2
            derivative_envelope = self.derivative_envelope_2
        elif phase == 'C':
            envelope = self.envelope_3
            smoothed_envelope = self.smoothed_envelope_3
            derivative_envelope = self.derivative_envelope_3

        point_1 = self.find_point(envelope, x_axis, 0, direction=max)  # MAX 1
        point_2 = self.find_point(derivative_envelope, x_axis, x_axis.index(point_1[1]), direction=min)  # MIN 1
        point_2 = (smoothed_envelope[x_axis.index(point_2[1])], point_2[1])
        point_3 = self.find_point(smoothed_envelope, x_axis, x_axis.index(point_2[1]), direction=max)  # MAX 2
        # point_4
        search_index = x_axis.index(point_3[1])
        negative_index = next((i for i, val in enumerate(derivative_envelope[search_index:]) if val < 0), None)
        crossing_point = x_axis[search_index + negative_index + 1000]
        point_4 = (smoothed_envelope[x_axis.index(crossing_point)], crossing_point)

        point_start = self.find_start_point(smoothed_envelope, x_axis, point_1, direction=min)  # Start
        point_end = self.find_point(derivative_envelope, x_axis, x_axis.index(point_3[1]), direction=min)  # END
        point_end = (smoothed_envelope[x_axis.index(point_end[1]) + 500], x_axis[x_axis.index(point_end[1]) + 500])  # END

        t_act = point_1[1] - point_start[1]  # Время активации
        t_str = (point_2[1] - point_1[1]) + (point_4[1] - point_3[1])  # Время страгивания
        t_razg = (point_end[1] - point_4[1])  # Время разгона

        if phase == 'A':
            self.t_act[0] = t_act
            self.t_str[0] = t_str
            self.t_razg[0] = t_razg
            self.i_pusk[0] = point_1[0]
        elif phase == 'B':
            self.t_act[1] = t_act
            self.t_str[1] = t_str
            self.t_razg[1] = t_razg
            self.i_pusk[1] = point_1[0]
        elif phase == 'C':
            self.t_act[2] = t_act
            self.t_str[2] = t_str
            self.t_razg[2] = t_razg
            self.i_pusk[2] = point_1[0]

        fig = Figure()
        canvas = FigureCanvas(fig)
        ax_1 = fig.add_subplot(121)

        new_index = x_axis.index(point_1[1]) + 200
        ax_1.plot(x_axis[:new_index], smoothed_envelope[:new_index], label='Огибающая', color='r')  # Огибающая (сглаженная)
        ax_1.axvline(point_start[1], color='black', linestyle='--')  # Вертикальная линия
        ax_1.axvline(point_1[1], color='black', linestyle='--')  # Вертикальная линия

        ax_1.set_title(f'Время активации: {t_act:.3f} с')
        ax_1.set_xlabel('Время, с')
        ax_1.set_ylabel('Сила тока, А')
        ax_1.grid(True)

        ax_2 = fig.add_subplot(122)
        new_index = x_axis.index(point_end[1]) + x_axis.index(point_1[1])
        ax_2.plot(x_axis[:new_index], smoothed_envelope[:new_index], label='Огибающая', color='r')  # Огибающая (сглаженная)
        ax_2.axvline(point_1[1], color='black', linestyle='--')  # Вертикальная линия
        ax_2.axvline(point_2[1], color='black', linestyle='--')  # Вертикальная линия
        ax_2.axvline(point_3[1], color='black', linestyle='--')  # Вертикальная линия
        ax_2.axvline(point_4[1], color='black', linestyle='--')  # Вертикальная линия
        ax_2.axvline(point_end[1], color='black', linestyle='--')  # Вертикальная линия

        ax_2.set_title(f'Время страгивания: {t_str:.2f} с, время разгона: {t_razg:.2f} с')
        ax_2.set_xlabel('Время, с')
        ax_2.set_ylabel('Сила тока, А')
        ax_2.grid(True)

        widget = self.create_graph_widget(canvas)
        layout.addWidget(widget)

    def create_modulation_graph(self, tab, data, phase=''):
        """ Графики модуляции """
        layout = tab.layout()
        if layout:
            for i in reversed(range(layout.count())):  # Очистка
                layout.itemAt(i).widget().deleteLater()

        # Входные данные для построения
        x_axis, y_axis = [i[0] for i in data], [i[1] for i in data]
        envelope, derivative_envelope = None, None
        if phase == 'A':
            envelope = self.envelope_1
            derivative_envelope = self.derivative_envelope_1
        elif phase == 'B':
            envelope = self.envelope_2
            derivative_envelope = self.derivative_envelope_2
        elif phase == 'C':
            envelope = self.envelope_3
            derivative_envelope = self.derivative_envelope_3

        # Поиск пиковых точек
        point_peak = self.find_point(derivative_envelope, x_axis, x_axis.index(40), x_axis.index(60), direction=max)  # PEAK
        start_pos = x_axis.index(point_peak[1]) + 5000
        end_pos = len(x_axis) - 50
        point_i_max = self.find_point(envelope, x_axis, start_pos, end_pos, direction=max)  # I MAX
        point_i_min = self.find_point(envelope, x_axis, start_pos, end_pos, direction=min)  # I MIN

        # Промежуток модуляции
        start_pos = x_axis.index(point_peak[1]) + 500
        end_pos = len(x_axis) - 50
        nex_x_axis = [i / 10 for i in range(0, len(x_axis[start_pos:end_pos]))]
        new_envelope = envelope[start_pos:end_pos]

        point_i_max_new_x = new_envelope.index(point_i_max[0]) / 10
        point_i_min_new_x = new_envelope.index(point_i_min[0]) / 10

        # Рабочий ток
        i_rab = sum(new_envelope) / len(new_envelope)
        # Модуляция
        mod = ((point_i_max[0] - point_i_min[0]) / (point_i_max[0] + point_i_min[0]))

        # Запись полученных значений
        if phase == 'A':
            self.i_rab[0] = i_rab
            self.mod[0] = mod
        elif phase == 'B':
            self.i_rab[1] = i_rab
            self.mod[1] = mod
        elif phase == 'C':
            self.i_rab[2] = i_rab
            self.mod[2] = mod

        # Построение графика
        fig = Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        ax.plot(nex_x_axis, new_envelope, label='Огибающая', color='black')  # Огибающая
        ax.scatter(point_i_max_new_x, point_i_max[0], color='r', label=point_i_max)  # PEAK
        ax.scatter(point_i_min_new_x, point_i_min[0], color='r', label=point_i_min)  # PEAK

        ax.set_title(f'Модуляция, m = {mod:.4f} %')
        ax.set_xlabel('Время, с')
        ax.set_ylabel('Амплитуда')

        ax.grid(True)

        widget = self.create_graph_widget(canvas)
        layout.addWidget(widget)

    def create_phase_detection_graph(self, tab, data, phase=''):
        """ Графики определения фазы"""
        layout = tab.layout()
        if layout:
            for i in reversed(range(layout.count())):  # Очистка
                layout.itemAt(i).widget().deleteLater()

        # Входные данные для построения
        x_axis, y_axis = [i[0] for i in data], [i[1] for i in data]

        hamming_window = np.hamming(len(y_axis))
        signal_windowed = y_axis * hamming_window

        # # Вычисление преобразования Фурье
        fft_values = fft(signal_windowed)  # Y
        freq_values = fftfreq(len(signal_windowed), x_axis[1] - x_axis[0])  # X

        # Отсечение отрицательных частот и нормализация
        positive_freq_mask = freq_values > 0
        freq_values = freq_values[positive_freq_mask]
        fft_values = np.abs(fft_values[positive_freq_mask]) / len(signal_windowed)
        db_values = 20 * np.log10(fft_values)

        freq_values = freq_values.tolist()
        db_values = db_values.tolist()

        peak_point = self.find_point(db_values, freq_values, 0)  # X, Y
        # Диапазон поиска фаз
        # min_index = self.find_nearest_value(freq_values, peak_point[1] - 20)
        max_index = self.find_nearest_value(freq_values, peak_point[1] + 50)

        # new_x_axis = freq_values[min_index[1]:max_index[1]]
        # new_y_axis = db_values[min_index[1]:max_index[1]]

        new_x_axis = freq_values[0:max_index[1]]
        new_y_axis = db_values[0:max_index[1]]

        ob_per_sec = round(int(self.data_v[0]) / 60, 1)

        # Диапазоны поиска макс и мин значения
        min_point = self.find_nearest_value(new_x_axis, peak_point[1] - ob_per_sec)
        max_point = self.find_nearest_value(new_x_axis, peak_point[1] + ob_per_sec)

        min_search_range = range(new_x_axis.index(min_point[0]) - 100, new_x_axis.index(min_point[0]) + 100)
        max_search_range = range(new_x_axis.index(max_point[0]) - 100, new_x_axis.index(max_point[0]) + 100)

        # Максимальные значения в указанных диапазонах
        max_value_near_min = max(new_y_axis[i] for i in min_search_range)
        max_value_near_max = max(new_y_axis[i] for i in max_search_range)

        #max_value_near_min, max_value_near_max = new_y_axis[min_point[1]], new_y_axis[max_point[1]]

        # Построение графика
        fig = Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        ax.plot(new_x_axis, new_y_axis, label='Огибающая', color='r')  # Огибающая
        ax.scatter(peak_point[1], peak_point[0], color='black', label=peak_point)  # PEAK

        ax.scatter(new_x_axis[new_y_axis.index(max_value_near_min)], max_value_near_min, color='black', label=peak_point)
        ax.scatter(new_x_axis[new_y_axis.index(max_value_near_max)], max_value_near_max, color='black', label=peak_point)

        # ax.scatter(min_point[1], min_point[0], color='black', label=peak_point)
        # ax.scatter(max_point[1], max_point[0], color='black', label=peak_point)


        # ax.axvline(min_point, color='black', linestyle='--')  # Вертикальная линия
        # ax.axvline(max_point, color='black', linestyle='--')  # Вертикальная линия
        ax.annotate(
            '',
            xy=(new_x_axis[new_y_axis.index(max_value_near_min)], max_value_near_min),  # Конец стрелки
            xytext=(peak_point[1], peak_point[0]),  # Координаты начала стрелки
            arrowprops=dict(arrowstyle='->')
        )
        ax.annotate(
            '',
            xy=(new_x_axis[new_y_axis.index(max_value_near_max)], max_value_near_max),  # Конец стрелки

            xytext=(peak_point[1], peak_point[0]),  # Координаты начала стрелки
            arrowprops=dict(arrowstyle='->')
        )

        ax.set_title(f'Спектральный анализ')
        ax.set_xlabel('Частота')
        ax.set_ylabel('Амплитуда')

        ax.grid(True)

        widget = self.create_graph_widget(canvas)
        layout.addWidget(widget)

    def create_graph_widget(self, canvas):
        """ Панель управления графиками """
        toolbar = NavigationToolbar(canvas, self)
        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(canvas)
        widget = QWidget()
        widget.setLayout(layout)
        return widget

    def app_resolution(self):
        """ Адаптивное разрешение окна """
        screen_resolution = self.app.screen().size()
        screen_width, screen_height = screen_resolution.width(), screen_resolution.height()
        self.app.resize(int(screen_width * 0.75), int(screen_height * 0.75))  # Window resolution
        self.app.setMinimumSize(int(screen_width * 0.5), int(screen_height * 0.5))  # Minimum window resolution at 50%

    @staticmethod
    def find_point(point_signal, point_time, start_index, end_index=None, direction=max):
        """ Поиск точек на графике """
        if not end_index:
            end_index = len(point_signal)
        point_val = direction(point_signal[start_index:end_index])
        point_index = point_signal.index(point_val)
        point_time = point_time[point_index]
        return point_val, point_time

    @staticmethod
    def find_point_index(point_signal, point_time, start_index, end_index=None, direction=max):
        """ Поиск точек на графике """
        if not end_index:
            end_index = len(point_signal)
        point_val = direction(point_signal[start_index:end_index])
        point_index = point_signal.index(point_val)
        point_time = point_time[point_index]
        return point_val, point_time, point_index

    @staticmethod
    def find_start_point(point_signal, point_time, point, direction=min, offset=0):
        """ Поиск начальной точки """
        point_val = direction(point_signal[:point_time.index(point[1]) + offset])
        point_index = point_signal.index(point_val)
        point_time = point_time[point_index]
        return point_val, point_time

    @staticmethod
    def find_nearest_value(lst, target):
        closest_value = min(lst, key=lambda x: abs(x - target))
        index = lst.index(closest_value)
        return closest_value, index