from urllib.parse import urlparse
from .platforms import tiktok, instagram, chingari, josh, moj, triller, sharechat, mitron, roposo, litlot

def get_platform_downloader(url):
    domain = urlparse(url).netloc.lower()
    if 'tiktok.com' in domain:
        return tiktok.TikTokDownloader()
    elif 'instagram.com' in domain:
        return instagram.InstagramDownloader()
    elif 'chingari' in domain:
        return chingari.ChingariDownloader()
    elif 'josh' in domain:
        return josh.JoshDownloader()
    elif 'moj' in domain:
        return moj.MojDownloader()
    elif 'triller' in domain:
        return triller.TrillerDownloader()
    elif 'sharechat' in domain:
        return sharechat.ShareChatDownloader()
    elif 'mitron' in domain:
        return mitron.MitronDownloader()
    elif 'roposo' in domain:
        return roposo.RoposoDownloader()
    elif 'litlot' in domain:
        return litlot.LitLotDownloader()
    else:
        raise ValueError("Unsupported platform for URL: " + url)

def download_video(url, output=None):
    downloader = get_platform_downloader(url)
    print(f"Using {downloader.__class__.__name__} for URL: {url}")
    return downloader.download(url, output)
