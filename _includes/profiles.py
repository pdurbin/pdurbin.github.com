#!/usr/bin/env python3
import os
import time
from pathlib import Path
from urllib.parse import urlparse

import requests
import yaml

HOME = os.environ.get("HOME", "")
checkout = Path(HOME) / "github" / "pdurbin" / "pdurbin.github.com"
googfav = "http://www.google.com/s2/u/0/favicons?domain="
grabicon = "http://grabicon.com/"
favicondir = Path("images") / "favicons"
includedir = checkout / "_includes"
profileout = includedir / "profiles.html"
profiles_yaml = includedir / "profiles.yaml"

checkout.mkdir(parents=True, exist_ok=True)
includedir.mkdir(parents=True, exist_ok=True)
favicondir.mkdir(parents=True, exist_ok=True)

os.chdir(checkout)

with profiles_yaml.open("r") as f:
    profs = yaml.safe_load(f)

html_lines = ['<ul style="padding: 0px; margin: 0em; margin-left: 20px">']

for proff in profs:
    parsed = urlparse(proff)
    host = parsed.hostname or parsed.netloc
    if not host:
        continue

    grabhost = f"{grabicon}{host}.png.16"

    png_path = favicondir / f"{host}.png"
    if not png_path.exists():
        try:
            resp = requests.get(grabhost, timeout=10)
            resp.raise_for_status()
            png_path.parent.mkdir(parents=True, exist_ok=True)
            with png_path.open("wb") as fh:
                fh.write(resp.content)
            time.sleep(0.5)
        except Exception:
            pass

    path = parsed.path
    if path == "/":
        path = ""
    nohttp = f"{host}{path}"

    png_url = "/" + png_path.as_posix()
    li = f'<li style="list-style-image:url(\'{png_url}\')"><a rel="me" href="{proff}">{nohttp}</a></li>'
    html_lines.append(li)

html_lines.append("</ul>")

with profileout.open("w") as fh:
    fh.write("\n".join(html_lines) + "\n")
