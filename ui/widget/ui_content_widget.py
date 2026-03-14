from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QStackedWidget,
)
from PySide6.QtCore import Qt
from ui.widget.ui_data_unit_test_widget import DataUnitTestWidget
from ui.ui_content_enum import content_enum


class ContentWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_content()

    def init_content(self):

        self.setAttribute(Qt.WA_StyledBackground, True)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.stack = QStackedWidget(self)
        layout.addWidget(self.stack)

        self.data_unit_test_widget = DataUnitTestWidget()

        self.stack.addWidget(self.data_unit_test_widget)

        # Set default index
        self.stack.setCurrentIndex(int(content_enum.UNIT_TEST.value))

    def update_content(self, text):
        # 単体テスト観点生成
        if content_enum.UNIT_TEST.value == text:
            self.stack.setCurrentIndex(int(content_enum.UNIT_TEST.value))
