from PySide6.QtWidgets import QWidget, QHBoxLayout
from PySide6.QtCore import Qt
from ui.widget.ui_menu_widget import MenuWidget
from ui.widget.ui_content_widget import ContentWidget
from ui import ui_config
from ui import ui_lang


class ui_window(QWidget):
    def __init__(self):
        super().__init__()
        self.menu_widget = None
        self.content_widget = None
        self.init_ui_window()

    def init_ui_window(self):

        # 現在言語取得
        lang_key = ui_lang.fetch_current_lang()

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowTitle(ui_lang.LANGUAGES[lang_key]["APP_TITLE"])
        self.resize(ui_config.WINDOW_WIDTH, ui_config.WINDOW_HEIGHT)
        self.setFixedWidth(ui_config.WINDOW_WIDTH)
        self.setFixedHeight(ui_config.WINDOW_HEIGHT)
        self.setStyleSheet(ui_config.WINDOW_STYLE)

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.menu_widget = MenuWidget(self)
        self.content_widget = ContentWidget(self)

        main_layout.addWidget(self.menu_widget)
        main_layout.addWidget(self.content_widget)

        # Send Signal from MenuWidget to ContentWidget
        self.menu_widget.button_clicked.connect(self.content_widget.update_content)

        self.setLayout(main_layout)
