import os
import subprocess

def download_youtube_video(url):
    if not url:
        print("No URL provided.")
        return
    
    # Save to the directory where the script is run
    download_path = r"C:/Users/Dexte/Videos"
    
    # Command to download video
    command = f"yt-dlp -o '{download_path}' {url}"
    subprocess.run(command, shell=True)
    
    print("Download complete.")

if __name__ == "__main__":
    video_url = input("Enter YouTube URL: ")
    download_youtube_video(video_url)
