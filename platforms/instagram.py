from .base import PlatformDownloader

class InstagramDownloader(PlatformDownloader):
    def download(self, url, output=None):
        print("Downloading video from Instagram:", url)
        # TODO: Implement actual download logic
        if output:
            print(f"Video saved to {output}")
        return True
