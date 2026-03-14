import traceback
from PySide6.QtCore import QThread, Signal
from ui.interface.ui_interface_enum import content_result_enum
from logic._schema.path_config import OUTPUT_DIR


class UnitTestThread(QThread):

    progress_signal = Signal(str)
    path_signal = Signal(list)

    def __init__(self, input_field_files: str):
        super().__init__()
        self.con_desc_doc_files = input_field_files
        self.layout_paths = []

    def run(self):
        """
        単体テスト観点生成を実行
        """
        start_message = f'#### コードファイルの読み出しを開始'
        self.progress_signal.emit(start_message)
        md_files = []
        for file in self.con_desc_doc_files:
            # ファイル種類確認
            try:
                # org_json = generate_ut_viewpoints_and_details(
                #     in_file=file,
                #     out_md_dir=OUTPUT_DIR,
                #     out_json_dir=OUTPUT_DIR,
                #     progress_signal=self.progress_signal
                # )
                # print(org_json)
                # md_files.append(org_json["out_md_path"])
                # with open(org_json["out_md_path"], encoding="utf-8") as f:
                #     md_content = f.read()
                # self.progress_signal.emit(md_content)
                success_message = f'#### <span style="color: green;"> {file}単体テスト観点を生成しました </span>'
                self.progress_signal.emit(success_message)
            except Exception as e:
                error_info = traceback.format_exc()
                print(f"エラーが発生しました:\n{str(e)}")
                self.progress_signal.emit(f'#### <span style="color: red;"> エラーが発生しました: <br> {str(e)} </span>')
                print(f"詳細:\n{error_info}")
                # self.progress_signal.emit(f"詳細:\n <pre> {error_info} </pre>")

            self.path_signal.emit(md_files)
            success_message = f'#### <span> 資料内容の読み出しが完了 </span>'
            self.progress_signal.emit(success_message)
