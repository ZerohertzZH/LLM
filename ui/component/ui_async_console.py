from markdown_it import MarkdownIt
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, guess_lexer
from PySide6.QtCore import Qt, QTimer, Signal, Slot
from PySide6.QtGui import QKeySequence, QTextCursor
from PySide6.QtWidgets import QMenu, QTextEdit

from ui import ui_config


def _pygments_highlight(*args, **kwargs):
    """ """
    code = args[0]
    info = args[1] if len(args) > 1 else ""
    lang = info.split()[0] if info else ""
    try:
        lexer = get_lexer_by_name(lang, stripall=True)
    except Exception:
        try:
            lexer = guess_lexer(code)
        except Exception:
            lexer = get_lexer_by_name("text", stripall=True)
    formatter = HtmlFormatter(nowrap=True)
    return highlight(code, lexer, formatter)

_md = (
    MarkdownIt(
        "commonmark",
        {
            "html": True,
            "linkify": True,
            "typographer": True,
            "highlight": _pygments_highlight,
        },
    )
    .enable("table")
    .enable("fence")
)

class AsyncConsoleOutput(QTextEdit):
    update_signal = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setReadOnly(True)
        self.setStyleSheet(ui_config.CODE_GEN_CONSOLE_STYLE)

        self.setTextInteractionFlags(
            Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard
        )

        self.setMinimumHeight(200)
        self.setMaximumHeight(300)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.pending_text = []
        self.current_text = ""
        self.current_pos = 0
        self.full_text = ""
        self._first_segment = True

        self.update_signal.connect(self._append_text)

        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self._process_pending)
        self.update_timer.start(7)

    @Slot(str)
    def _append_text(self, text):

        self.pending_text.append(text)

    def _process_pending(self):

        if not self.current_text and self.pending_text:
            self.current_text = self.pending_text.pop(0)
            self.current_pos = 0
            if self._first_segment:
                self._first_segment = False
            else:
                self.moveCursor(QTextCursor.End)
                self.insertPlainText("\n")

        if self.current_text:
            if self.current_pos < len(self.current_text):

                self.moveCursor(QTextCursor.End)
                self.insertPlainText(self.current_text[self.current_pos])
                self.current_pos += 1
                self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())
            else:

                segment = self.current_text
                self.current_text = ""
                self.current_pos = 0

                self.full_text += segment + "\n"

                html_body = _md.render(self.full_text)
                style = HtmlFormatter().get_style_defs()

                custom_css = """
                    pre { white-space: pre-wrap; }
                    code { white-space: pre-wrap; }
                    table { border-collapse: collapse; }
                    table, th, td { border: 1px solid #ccc; }
                    th, td { padding: 4px; }
                    """
                full_html = f"<html><head><style>{style}{custom_css}</style></head><body>{html_body}</body></html>"

                self.moveCursor(QTextCursor.End)
                self.setHtml(full_html)
                self.moveCursor(QTextCursor.End)
                self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())

                if self.pending_text:
                    self._process_pending()

    def contextMenuEvent(self, event):

        menu = QMenu(self)
        menu.addAction("Copy", self.copy, QKeySequence.Copy)
        menu.addAction("Select All", self.selectAll, QKeySequence.SelectAll)
        menu.exec(event.globalPos())

    def keyPressEvent(self, event):

        if event.matches(QKeySequence.Copy) or event.matches(QKeySequence.SelectAll):
            super().keyPressEvent(event)
        else:
            event.ignore()

    def async_append_text(self, text):
        self.update_signal.emit(text)

    def clear(self):

        super().clear()
        self.pending_text.clear()
        self.current_text = ""
        self.current_pos = 0
        self.full_text = ""
        self._first_segment = True
