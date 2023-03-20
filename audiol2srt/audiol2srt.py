import argparse

from pydub import AudioSegment


def generate_srt(audio_file, lyrics_file, output_file):
    audio = AudioSegment.from_mp3(audio_file)
    total_duration = len(audio)

    with open(lyrics_file, 'r') as f:
        lyrics = [line.strip() for line in f.readlines()]

    duration_per_line = total_duration / len(lyrics)

    with open(output_file, 'w') as f:
        for idx, line in enumerate(lyrics):
            start_time = idx * duration_per_line
            end_time = (idx + 1) * duration_per_line

            f.write(f"{idx + 1}\n")
            f.write(f"{format_timestamp(start_time)} --> {format_timestamp(end_time)}\n")
            f.write(f"{line}\n\n")


def format_timestamp(milliseconds):
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d},{int(milliseconds):03d}"


def main():
    parser = argparse.ArgumentParser(
        description="Generate SRT subtitle files by syncing an MP3 audio file with a text file containing lyrics.")
    parser.add_argument("audio_file", help="Path to the input MP3 audio file.")
    parser.add_argument("lyrics_file", help="Path to the input text file containing lyrics.")
    parser.add_argument("output_file", help="Path to the output SRT file.")

    args = parser.parse_args()

    generate_srt(args.audio_file, args.lyrics_file, args.output_file)


if __name__ == "__main__":
    main()
