# setup.py
from setuptools import setup, find_packages

setup(
    name="AudioLyric2SRT",
    version="0.1.0",
    author="Takeshi Juan",
    author_email="takeshi.juan@icloud.com",
    description="A package to generate SRT subtitle files by syncing an MP3 audio file with a text file containing lyrics.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/takesi0627/AudioLyric2SRT",
    packages=find_packages(),
    install_requires=[
        "pydub",
    ],
    entry_points={
        "console_scripts": [
            "audio-lyric2srt = AudioLyric2SRT.__init__:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
