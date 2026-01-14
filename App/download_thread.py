from PySide6.QtCore import QThread, Signal
from libs import media

class DownloadWorker(QThread):
    progress = Signal(int)
    completed = Signal(bool, str)

    def __init__(self, *, url, output_path, only_audio, resolution=None):
        super().__init__()
        self.url = url
        self.output_path = output_path
        self.only_audio = only_audio
        self.resolution = resolution

    def progress_hook(self, d):
        if d["status"] == "downloading":
            total = d.get("total_bytes") or d.get("total_bytes_estimate")
            downloaded = d.get("downloaded_bytes", 0)

            if total:
                percent = int(downloaded * 100 / total)
                self.progress.emit(percent)

        elif d["status"] == "finished":
            self.progress.emit(100)

    def run(self):
        try:
            if self.only_audio:
                media.download_audio(
                        self.url,
                        self.output_path,
                        progress_hook=self.progress_hook,
                )
            else:
                media.download_video(
                        self.url,
                        self.output_path,
                        resolution=self.resolution,
                        progress_hook=self.progress_hook,
                )
        except Exception as e:
            self.completed.emit(False, str(e))   
        else:
            self.completed.emit(True, "")

