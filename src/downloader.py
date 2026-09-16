import yt_dlp
import os
from pathlib import Path

class YouTubeDownloader:
    QUALITY_MAP = {
        "1080p": "best[height<=1080][ext=mp4]/best[height<=1080]",
        "720p": "best[height<=720][ext=mp4]/best[height<=720]",
        "480p": "best[height<=480][ext=mp4]/best[height<=480]",
        "360p": "best[height<=360][ext=mp4]/best[height<=360]",
        "Audio": "bestaudio/best"
    }
    
    def __init__(self):
        self.ydl_opts = {
            'quiet': False,
            'no_warnings': False,
        }
    
    def download(self, url, output_path, quality="1080p"):
        """
        Download a YouTube video
        
        Args:
            url (str): YouTube video URL
            output_path (str): Directory to save the video
            quality (str): Video quality (1080p, 720p, 480p, 360p, Audio)
        
        Returns:
            tuple: (success: bool, message: str)
        """
        try:
            # Ensure output directory exists
            Path(output_path).mkdir(parents=True, exist_ok=True)
            
            # Set format based on quality
            format_str = self.QUALITY_MAP.get(quality, self.QUALITY_MAP["1080p"])
            
            ydl_opts = {
                'format': format_str,
                'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
                'quiet': False,
                'no_warnings': False,
            }
            
            # Add audio-only format if requested
            if quality == "Audio":
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                
            return True, f"Downloaded: {os.path.basename(filename)}"
        
        except Exception as e:
            return False, f"Download failed: {str(e)}"
