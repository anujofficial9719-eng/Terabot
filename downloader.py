import requests
import os
from urllib.parse import urlparse
import re

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def download(url: str) -> str:
    """
    Downloads file from TeraBox or Terashare link.
    Returns local file path, empty string if failed.
    """
    filename = os.path.basename(urlparse(url).path)
    if not filename:
        filename = "file_" + str(abs(hash(url)))
    path = os.path.join(DOWNLOAD_FOLDER, filename)

    # ===== Terashare link handling =====
    if "terasharelink.com" in url:
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            
            # Parse direct download URL (Terashare pages usually contain 'download' href)
            m = re.search(r'href="(https://.*?/download.*?)"', r.text)
            if not m:
                raise Exception("Direct download URL not found")
            direct_url = m.group(1)

            with requests.get(direct_url, stream=True, timeout=60) as resp:
                resp.raise_for_status()
                with open(path, "wb") as f:
                    for chunk in resp.iter_content(chunk_size=1024*1024):
                        if chunk:
                            f.write(chunk)
            return path
        except Exception as e:
            print(f"Terashare download error: {e}")
            return ""

    # ===== TeraBox / direct links =====
    try:
        with requests.get(url, stream=True, timeout=60) as r:
            r.raise_for_status()
            with open(path, "wb") as f:
                for chunk in r.iter_content(chunk_size=1024*1024):
                    if chunk:
                        f.write(chunk)
        return path
    except Exception as e:
        print(f"TeraBox download error: {e}")
        return ""
