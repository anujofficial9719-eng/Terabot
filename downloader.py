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
        d = aria2.add_uris(
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

        while not d.is_complete:
            d.update()
            print(f"⬇️ {d.progress_string()} | 🚀 {d.download_speed_string()}")
            time.sleep(1)

        # ❌ failed download check
        if d.has_failed:
            print("❌ Download failed")
            return None

        return d.files[0].path

    except Exception as e:
        print(f"❌ Download Error: {e}")
        return None
