from .base import PlatformDownloader

class MojDownloader(PlatformDownloader):
    def download(self, url, output=None):
        print("Downloading video from Moj:", url)
        # TODO: Implement actual download logic
        if output:
            print(f"Video saved to {output}")
        return True
