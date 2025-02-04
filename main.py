import yt_dlp
import os
import platform


def download_video(url, output_path="."):
    # Set up options
    ydl_opts = {
        "format": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",  # Download the best quality video
        "outtmpl": f"{output_path}/%(title)s.%(ext)s",  # Save the video with its title as filename
    }

    # Download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    # Get the current user's desktop path based on the OS
    system_name = platform.system()

    if system_name == "Windows":  # For Windows
        desktop_path = os.path.join(os.environ["USERPROFILE"], "Desktop")
    elif system_name == "Linux" or system_name == "Darwin":  # For Linux or macOS
        desktop_path = os.path.join(os.environ["HOME"], "Desktop")
    else:
        print(f"Unsupported OS: {system_name}")
        exit(1)

    # Ask for the video URL
    video_url = input("Enter the YouTube video URL: ")

    # Call the download function and set the desktop as the output path
    download_video(video_url, desktop_path)
