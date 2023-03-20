# AudioLyric2SRT

AudioLyric2SRT is a Python package that allows you to generate subtitle files (SRT) by syncing an audio file (MP3) with a text file containing lyrics. The package automatically aligns the audio with the lyrics, making it an efficient tool for creating accurate subtitles for your audio content.

## Features

- Load MP3 audio files and text files containing lyrics
- Sync the audio with the lyrics using silence detection
- Generate SRT subtitle files based on the synced audio and lyrics

## Installation

To install AudioLyric2SRT, run the following command:
```
pip install git+https://github.com/your_username/AudioLyric2SRT.git
```
Replace `your_username` with your GitHub username.

## Usage

You can use AudioLyric2SRT as a command-line tool or within a Python script.

### Command-line Usage

To use AudioLyric2SRT from the command line, run the following command:
```
audio-lyric2srt <mp3_file> <lyrics_file> <output_srt>
```
Replace `<mp3_file>`, `<lyrics_file>`, and `<output_srt>` with the respective paths to the MP3 file, lyrics text file, and output SRT file.

### Python Script Usage

To use AudioLyric2SRT in a Python script, follow this example:

```python
from AudioLyric2SRT import load_audio, load_lyrics, sync_lyrics_with_audio, create_srt_file

mp3_file = "path/to/mp3_file.mp3"
lyrics_file = "path/to/lyrics
```

