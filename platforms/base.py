class PlatformDownloader:
    def download(self, url, output=None):
        raise NotImplementedError("Download method must be implemented by the platform subclass")
