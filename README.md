# YouTube HD Downloader 🎬

A desktop application for downloading YouTube videos in Full HD (1080p) quality with a clean, user-friendly GUI.

## Features

✨ **High-Quality Downloads**
- Download in Full HD (1080p), HD (720p), SD (480p), 360p
- Extract audio only (MP3)
- Fast and reliable downloads

🎨 **User-Friendly Interface**
- Clean and intuitive PyQt6 GUI
- Real-time download status
- Progress tracking

📁 **Easy File Management**
- Browse and select download destination
- Default saves to Downloads folder
- Organized video storage

## Prerequisites

- Python 3.8 or higher
- FFmpeg (required for audio conversion)

### Install FFmpeg

**Windows:**
```bash
# Using chocolatey
choco install ffmpeg

# Or download from: https://ffmpeg.org/download.html
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install ffmpeg
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/adklandmark-dotcom/youtube-hd-downloader.git
cd youtube-hd-downloader
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

## Usage

1. **Paste YouTube URL** - Copy any YouTube link and paste it into the URL field
2. **Select Quality** - Choose desired video quality (1080p, 720p, 480p, 360p, or Audio only)
3. **Choose Destination** - Click "Browse" to select where to save the video
4. **Download** - Click the red "Download" button to start

## Supported Quality Options

| Quality | Description |
|---------|-------------|
| 1080p (Full HD) | Highest quality video |
| 720p (HD) | High definition |
| 480p (SD) | Standard definition |
| 360p | Lower bandwidth option |
| Audio Only | Extract as MP3 |

## Requirements

See `requirements.txt`:
- `PyQt6` - GUI framework
- `yt-dlp` - YouTube downloader
- `requests` - HTTP library

## Troubleshooting

### "FFmpeg not found" Error
Install FFmpeg following the prerequisite section above.

### "Invalid URL" Error
Make sure you've copied the correct YouTube URL. It should start with `https://www.youtube.com/` or `https://youtu.be/`

### Download Fails
- Check your internet connection
- Try a different video
- Update yt-dlp: `pip install --upgrade yt-dlp`

## Legal Notice

This tool is for downloading content you have rights to. Always respect YouTube's Terms of Service and copyright laws. Only download videos you have permission to download.

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## Author

Created with ❤️ by adklandmark-dotcom

## Support

Found an issue? Please open a GitHub issue with details about the problem.
