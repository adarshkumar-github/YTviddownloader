# import subprocess

# def install_if_needed(package):
#     try:
#         import importlib
#         importlib.import_module(package)
#     except ImportError:
#         subprocess.check_call(["pip", "install", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


# # Example usage
# install_if_needed("requests")
# install_if_needed("selenium")
# install_if_needed("webdriver-manager")
# install_if_needed("pytube")
# install_if_needed("pyQt5")
# install_if_needed("PyQt5.QtWidgets")
# install_if_needed("qt_material")

import sys
import threading
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QLineEdit, QCheckBox, QPushButton, QLabel, QWidget, QApplication
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from qt_material import apply_stylesheet
import time
from pytube import YouTube

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YT Downloader")
        self.setFixedSize(300, 380)
        
        self.la = QVBoxLayout()
        
        self.title_label = QLabel("Enter the title:")
        self.title_label.setFixedHeight(20)  # Set a fixed height for the label
        
        self.text = QLineEdit()
        
        self.che1 = QCheckBox("Video")
        self.che1.setChecked(True)
        
        self.che2 = QCheckBox("audio only")
        self.button = QPushButton("Download")
        self.labi = QLabel()
        self.labi.setFixedSize(275, 150)
        
        self.la.addWidget(self.title_label)
        self.la.addWidget(self.text)
        self.la.addWidget(self.button)
        self.la.addWidget(self.che1)
        self.la.addWidget(self.che2)
        self.la.addWidget(self.labi)
        self.labi.setStyleSheet("border: 1px solid yellow;")
        
        widget = QWidget()
        widget.setLayout(self.la)
        self.setCentralWidget(widget)
        self.button.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        self.labi.setText("Working on it......")
        threading.Thread(target=self.download_video).start()

    def download_video(self):
        video_title = self.text.text()
        search_query = '+'.join(video_title.split())
        chrome_service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=chrome_service)
        url = f"https://www.youtube.com/results?search_query={search_query}"
        driver.get(url)
        
        first_video_link = driver.execute_script('''
            return document.querySelector('#contents ytd-video-renderer a#video-title').href;
        ''')

        driver.quit()
        print("Working on it......")

        # Download Part
        link = first_video_link
        url = YouTube(link)

        save_location = r"C:\Users\adars\OneDrive\Documents\Experiment"

        print()
        print("Video title: ", url.title)
        print("Number of views on the video: ", url.views)
        print("Length of the video ", url.length, "seconds")
        print("Description:", url.description)
        print()

        video = url.streams.get_highest_resolution()
        audio = url.streams.get_audio_only()

        if self.che1.isChecked():
            try:
                print("Downloading video.............")
                self.labi.setText("Working on it......\nDownloading video...........")
                video.download(save_location)
                print("Video downloaded successfully!!!")
                self.labi.setText("Working on it......\nDownloading video...........\nVideo downloaded successfully!!!")
            except Exception as e:
                print("Error downloading video:", e)
                self.labi.setText("Working on it......\nDownloading video...........\nError downloading video.")

        if self.che2.isChecked():
            try:
                print("Downloading audio.............")
                self.labi.setText("Working on it......\nDownloading audio..........")
                audio.download(save_location)
                print("Audio downloaded successfully!!!")
                self.labi.setText("Working on it......\nDownloading audio..........\nAudio downloaded successfully!!!")
            except Exception as e:
                print("Error downloading audio:", e)
                self.labi.setText("Working on it......\nDownloading audio..........\nError downloading audio.")

if __name__ == "__main__":
    app = QApplication([])
    apply_stylesheet(app, theme='dark_amber.xml')
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
