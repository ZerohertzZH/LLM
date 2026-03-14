from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QSizePolicy, QLabel, QFrame
)
from PySide6.QtCore import Signal, Qt
from ui import ui_config, ui_lang
from ui.ui_content_enum import content_enum


class MenuWidget(QWidget):

    button_clicked = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.buttons = {}
        self.current_button = None
        self.init_menu()

    def init_menu(self):

        lang_key = ui_lang.fetch_current_lang()

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(ui_config.MENU_STYLE)
        self.setFixedWidth(ui_config.MENU_WIDTH)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        # ===== 上部説明エリア =====
        title_label = QLabel(ui_lang.LANGUAGES[lang_key]["MENU_GEN_UNIT_TEST_HEADER_TITLE"])
        title_label.setStyleSheet(ui_config.MENU_HEADER_TITLE_STYLE)

        desc_label = QLabel(ui_lang.LANGUAGES[lang_key]["MENU_GEN_UNIT_TEST_HEADER_DESC"])
        desc_label.setStyleSheet(ui_config.MENU_HEADER_DESC_STYLE)
        desc_label.setWordWrap(True)

        layout.addWidget(title_label)
        layout.addWidget(desc_label)

        # ===== 区切り線 =====
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet(ui_config.MENU_HEADER_DIVIDER_STYLE)
        layout.addWidget(line)

        # ===== メニューボタン =====
        self.add_menu_button(
            layout,
            ui_lang.LANGUAGES[lang_key]["MENU_GEN_UNIT_TEST_VIEWPOINTS"],
            content_enum.UNIT_TEST.value
        )
        layout.addStretch()
        # デフォルトのボタンを設定する
        self.set_active(content_enum.UNIT_TEST.value)

    def add_menu_button(self, layout, text, value):
        btn = QPushButton(text)
        btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        btn.setCursor(Qt.PointingHandCursor)
        btn.setFixedHeight(44)

        btn.setProperty("menuValue", value)
        btn.setStyleSheet(ui_config.MENU_BUTTON_STYLE)

        btn.clicked.connect(self.on_menu_clicked)
        layout.addWidget(btn)
        self.buttons[value] = btn

    def on_menu_clicked(self):
        button = self.sender()
        value = button.property("menuValue")

        self.set_active(value)
        self.button_clicked.emit(value)

    def set_active(self, value):
        for v, btn in self.buttons.items():
            if v == value:
                btn.setStyleSheet(ui_config.MENU_BUTTON_ACTIVE_STYLE)
                self.current_button = btn
            else:
                btn.setStyleSheet(ui_config.MENU_BUTTON_STYLE)
