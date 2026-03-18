import aria2p
import os
import time

aria2 = aria2p.API(
    aria2p.Client(
        host="http://localhost",
        port=6800,
        secret=""  # agar RPC secret use kar rahe ho to yaha daalo
    )
)

def download(url):
    os.makedirs("downloads", exist_ok=True)

    try:
        download = aria2.add_uris(
            [url],
            options={
                "dir": "downloads",
                "split": "16",
                "max-connection-per-server": "16",
                "min-split-size": "1M",
                "file-allocation": "none",
                "summary-interval": "1"
            }
        )

        while not download.is
