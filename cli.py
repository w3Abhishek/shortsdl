import argparse
from .downloader import download_video

def main():
    parser = argparse.ArgumentParser(description="Short Video Downloader")
    parser.add_argument("url", help="Video URL to download")
    parser.add_argument("-o", "--output", help="Output file name", default=None)
    args = parser.parse_args()
    try:
        download_video(args.url, args.output)
        print("Download completed.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
