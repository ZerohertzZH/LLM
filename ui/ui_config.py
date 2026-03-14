#########################################################
# APP
#########################################################
from config import HEIGHT_RATIO


WINDOW_WIDTH = 1400 * HEIGHT_RATIO
WINDOW_HEIGHT = 700 * HEIGHT_RATIO
WINDOW_STYLE = """
    background-color: #E0E0E0;
"""

#########################################################
# MENU
#########################################################
MENU_WIDTH = 240
MENU_STYLE = """
QWidget {
    background-color: #F5F7F6;
}
"""

MENU_BUTTON_STYLE = """
QPushButton {
    text-align: left;
    padding-left: 16px;
    border: none;
    font-size: 13px;
    background-color: transparent;
}

QPushButton:hover {
    background-color: #E8F3EE;
}
"""

MENU_BUTTON_ACTIVE_STYLE = """
QPushButton {
    text-align: left;
    padding-left: 12px;
    border: none;
    font-size: 13px;
    background-color: #DDEFE6;
    border-left: 4px solid #4CAF7A;
}
"""

MENU_HEADER_TITLE_STYLE = """
    font-size:16px;
    font-weight:600;
    color:#333333;
"""

MENU_HEADER_DESC_STYLE = """
    font-size:12px;
    color:#666666;
"""

MENU_HEADER_DIVIDER_STYLE = """
    color:#DDDDDD;
"""

MENU_BUTTON_CLICK_STYLE = """
QPushButton {
    border: none;
    background-color: rgba(100, 180, 140, 1.0);
    color: #333333;
    font-size: 13px;
    padding: 10px;
}
"""

#########################################################
# CODE GENERATION
#########################################################
CODE_GEN_STYLE = """
    QWidget {
        background-color: #E6E6E6;
    }
    QPushButton#CODE_GEN_START_BUTTON {
        background-color: rgba(100, 180, 140, 1.0);
        color: #333333;
        border: none;
        font-size: 14px;
        border-radius: 5px;
        text-align: center;
        font-weight: bold;
    }
    QPushButton#CODE_GEN_START_BUTTON:hover {
        background-color: rgba(100, 180, 140, 0.8);
    }

    QPushButton#CODE_GEN_START_BUTTON:pressed {
        background-color: rgba(100, 180, 140, 0.9);
    }
"""

CODE_GEN_CONSOLE_STYLE = """
        QTextEdit {
            background: #FFFFFF;
            border-radius: 6px;
            padding: 0px;
            color: #000000;
        }
        QTextEdit::viewport {
            background-color: #FFFFFF;
            border-radius: 4px;
            color: #000000;
        }
"""

CODE_GEN_LABEL_STYLE = "color: #333333; font-size: 15px; font-weight: bold;"

CODE_GEN_FILE_CARD_STYLE = """
    QFrame#fileCard {
        background-color: #f4f6f8;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
    }
"""

CODE_GEN_TITLE_LABEL_STYLE = """
    font-size: 15px;
    font-weight: 600;
    color: #2d3748;
    background: transparent;
"""

CODE_GEN_HEADER_BUTTON_STYLE = """
    QPushButton {
        background-color: #4f8f7f;
        color: white;
        border-radius: 6px;
        padding: 6px 14px;
    }
    QPushButton:hover {
        background-color: #3f7c6d;
    }
"""

CODE_GEN_START_BUTTON_KEY = "CODE_GEN_START_BUTTON"

CODE_GEN_INPUT_FIELD_STYLE = """
QLineEdit {
    color: #333333;
    background-color: #ffffff;
    border: 1px solid #cbd5e0;
    border-radius: 5px;
    font-weight: normal;
    height: 30px;
    padding-left: 5px;
    padding-top: 1px;
    font-size: 14px;
    font-family: 'Segoe UI', 'Meiryo', sans-serif;
}

QLineEdit::placeholder {
    color: #9aa0a6;
    font-weight: normal;
}
"""

CODE_GEN_MSG_BOX_STYLE = """
                QLabel {
                    color: #333333;
                    font-weight: bold;
                }
            """

CODE_GEN_MSG_BUTTON_STYLE = "background-color: rgba(100, 180, 140, 1.0); color: #333333; border: none; padding: 5px 15px; border-radius: 5px;"

CODE_GEN_MSG_CALENDAR_STYLE = """
    QCalendarWidget QWidget#qt_calendar_navigationbar {
        background-color: rgb(0, 80, 160);
    }
    QCalendarWidget QToolButton {
        background-color: rgb(0, 80, 160);
        color: white;
    }
    QCalendarWidget QSpinBox {
        background-color: rgb(0, 80, 160);
        color: white;
    }
    QCalendarWidget QAbstractItemView::item:selected {
        background-color: rgb(200, 230, 255);
        color: black;
    }
"""

CODE_GEN_MSG_CALENDAR_CLICK_STYLE = """
QTableView::item:selected {
    background-color: rgb(0, 80, 160);
    color: white;
}
"""
