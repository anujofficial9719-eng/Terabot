import aria2p
import os

aria2 = aria2p.API(
    aria2p.Client(host="http://localhost", port=6800)
)

def download_file(url, path="downloads"):
    os.makedirs(path, exist_ok=True)

    download = aria2.add_uris([url], options={
        "dir": path,
        "split": "16",
        "max-connection-per-server": "16"
    })

    while not download.is_complete:
        download.update()

    return download.files[0].path
