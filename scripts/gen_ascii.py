import re
import urllib.request
from pathlib import Path

from PIL import Image

BASE = Path(__file__).resolve().parents[1]
ASSETS = BASE / "assets"


def fetch_portfolio_images() -> list[str]:
    html = urllib.request.urlopen("https://tanish-doorsala.github.io/").read().decode(
        "utf-8", "ignore"
    )
    return re.findall(r'src=["\']([^"\']+)["\']', html, re.I)


def image_to_ascii(path: Path, width: int = 26) -> str:
    img = Image.open(path).convert("L")
    w, h = img.size
    size = min(w, h)
    left = (w - size) // 2
    top = (h - size) // 2
    img = img.crop((left, top, left + size, top + size))
    height = max(12, int(width * 0.5))
    img = img.resize((width, height))

    chars = "@#%*+=-:. "
    lines: list[str] = []
    for y in range(height):
        row = "".join(chars[img.getpixel((x, y)) * (len(chars) - 1) // 255] for x in range(width))
        lines.append(row)

    while lines and not lines[0].strip(" ."):
        lines.pop(0)
    while lines and not lines[-1].strip(" ."):
        lines.pop()
    return "\n".join(lines)


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    images = fetch_portfolio_images()
    print("found", len(images), "src tags")
    for src in images:
        if any(k in src.lower() for k in ("tanish", "veera", "profile", "head", "about", "hero")):
            print("candidate:", src)

    avatar = ASSETS / "avatar.png"
    urllib.request.urlretrieve(
        "https://avatars.githubusercontent.com/u/181492446?s=400", avatar
    )
    ascii_art = image_to_ascii(avatar, width=24)
    (ASSETS / "face-ascii.txt").write_text(ascii_art, encoding="utf-8")
    print(ascii_art)


if __name__ == "__main__":
    main()
