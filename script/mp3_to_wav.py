#!/usr/bin/env python3
import os
import subprocess

def mp3_to_wav(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".mp3"):
            mp3_path = os.path.join(folder_path, filename)
            wav_filename = os.path.splitext(filename)[0] + ".wav"
            wav_path = os.path.join(folder_path, wav_filename)

            print(f"Converting: {filename} → {wav_filename}")
            subprocess.run([
                "ffmpeg", "-y", "-i", mp3_path, wav_path
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print("Conversion complete.")

if __name__ == "__main__":
    folder = input("Enter the folder path containing MP3 files: ").strip()
    if os.path.isdir(folder):
        mp3_to_wav(folder)
    else:
        print("Invalid folder path.")
