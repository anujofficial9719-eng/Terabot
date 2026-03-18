import aria2p
import os

aria2 = aria2p.API(
    aria2p.Client(host="http://localhost", port=6800)
)

def download(url):
    os.makedirs("downloads", exist_ok=True)

    d = aria2.add_uris([url], options={
        "dir": "downloads",
        "split": "16",
        "max-connection-per-server": "16"
    })

    while not d.is_complete:
        d.update()

    return d.files[0].path
