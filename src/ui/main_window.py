from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QPushButton, QLabel, QProgressBar, 
                             QComboBox, QFileDialog, QTextEdit, QMessageBox)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont, QIcon
from src.downloader import YouTubeDownloader
import os

class DownloadThread(QThread):
    progress = pyqtSignal(str)
    finished = pyqtSignal(bool, str)
    
    def __init__(self, url, output_path, quality):
        super().__init__()
        self.url = url
        self.output_path = output_path
        self.quality = quality
        self.downloader = YouTubeDownloader()
    
    def run(self):
        try:
            self.progress.emit("Starting download...")
            success, message = self.downloader.download(self.url, self.output_path, self.quality)
            self.finished.emit(success, message)
        except Exception as e:
            self.finished.emit(False, f"Error: {str(e)}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube HD Downloader")
        self.setGeometry(100, 100, 800, 600)
        self.download_thread = None
        
        self.init_ui()
    
    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        
        # Title
        title = QLabel("YouTube HD Downloader")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        main_layout.addWidget(title)
        
        # URL Input
        url_layout = QHBoxLayout()
        url_label = QLabel("Video URL:")
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Paste YouTube URL here...")
        url_layout.addWidget(url_label)
        url_layout.addWidget(self.url_input)
        main_layout.addLayout(url_layout)
        
        # Quality Selection
        quality_layout = QHBoxLayout()
        quality_label = QLabel("Quality:")
        self.quality_combo = QComboBox()
        self.quality_combo.addItems(["1080p (Full HD)", "720p (HD)", "480p (SD)", "360p", "Audio Only"])
        quality_layout.addWidget(quality_label)
        quality_layout.addWidget(self.quality_combo)
        quality_layout.addStretch()
        main_layout.addLayout(quality_layout)
        
        # Output Path
        output_layout = QHBoxLayout()
        output_label = QLabel("Save To:")
        self.output_path_input = QLineEdit()
        self.output_path_input.setText(os.path.expanduser("~/Downloads"))
        self.browse_btn = QPushButton("Browse...")
        self.browse_btn.clicked.connect(self.browse_folder)
        output_layout.addWidget(output_label)
        output_layout.addWidget(self.output_path_input)
        output_layout.addWidget(self.browse_btn)
        main_layout.addLayout(output_layout)
        
        # Download Button
        self.download_btn = QPushButton("Download")
        self.download_btn.setStyleSheet("background-color: #FF0000; color: white; font-weight: bold; padding: 10px;")
        self.download_btn.clicked.connect(self.start_download)
        main_layout.addWidget(self.download_btn)
        
        # Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        main_layout.addWidget(self.progress_bar)
        
        # Status/Log
        status_label = QLabel("Status:")
        main_layout.addWidget(status_label)
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setMaximumHeight(200)
        main_layout.addWidget(self.log_text)
        
        central_widget.setLayout(main_layout)
    
    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Download Folder")
        if folder:
            self.output_path_input.setText(folder)
    
    def start_download(self):
        url = self.url_input.text().strip()
        output_path = self.output_path_input.text().strip()
        quality = self.quality_combo.currentText().split()[0]  # Extract resolution
        
        if not url:
            QMessageBox.warning(self, "Error", "Please enter a YouTube URL")
            return
        
        if not os.path.isdir(output_path):
            QMessageBox.warning(self, "Error", "Invalid output directory")
            return
        
        self.download_btn.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.log_text.clear()
        self.log_text.append(f"Starting download: {url}")
        self.log_text.append(f"Quality: {quality}")
        self.log_text.append(f"Output: {output_path}\n")
        
        self.download_thread = DownloadThread(url, output_path, quality)
        self.download_thread.progress.connect(self.update_log)
        self.download_thread.finished.connect(self.download_finished)
        self.download_thread.start()
    
    def update_log(self, message):
        self.log_text.append(message)
    
    def download_finished(self, success, message):
        self.download_btn.setEnabled(True)
        self.progress_bar.setVisible(False)
        
        if success:
            self.log_text.append("\n✓ Download completed successfully!")
            QMessageBox.information(self, "Success", message)
        else:
            self.log_text.append(f"\n✗ Download failed: {message}")
            QMessageBox.critical(self, "Error", message)
