#!/usr/bin/env python3
import os
import subprocess
import sys

def convert_mp4_to_mp3(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(".mp4"):
            mp4_path = os.path.join(directory, filename)
            mp3_filename = os.path.splitext(filename)[0] + ".mp3"
            mp3_path = os.path.join(directory, mp3_filename)
            print(f"Converting {filename} to {mp3_filename}...")
            try:
                subprocess.run([
                    "ffmpeg", "-i", mp4_path, "-vn", "-acodec", "libmp3lame", "-y", mp3_path
                ], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: <directory>")
        sys.exit(1)
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"{directory} is not a valid directory.")
        sys.exit(1)
    convert_mp4_to_mp3(directory)
