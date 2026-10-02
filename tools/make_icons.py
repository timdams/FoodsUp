"""Generate the PWA icons in src/icons/ (run: python tools/make_icons.py).

Draws a steaming bowl in the app's amber on its dark background. All artwork
stays inside the central safe zone, so the same image works as a maskable icon.
"""
import math
from pathlib import Path
from PIL import Image, ImageDraw

BG = (26, 20, 16)        # --bg
ACCENT = (232, 162, 58)  # --accent
ACCENT2 = (196, 98, 45)  # --accent2
S = 1024                 # draw large, downsample for smooth edges

OUT = Path(__file__).resolve().parent.parent / 'src' / 'icons'


def draw(rounded: bool) -> Image.Image:
    img = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if rounded:
        d.rounded_rectangle([0, 0, S - 1, S - 1], radius=int(S * 0.22), fill=BG)
    else:
        d.rectangle([0, 0, S, S], fill=BG)

    # Bowl: lower half of an ellipse plus a rim and a foot
    cx, rim_y = S // 2, int(S * 0.52)
    w = int(S * 0.27)
    d.chord([cx - w, rim_y - w, cx + w, rim_y + w], 0, 180, fill=ACCENT)
    d.rounded_rectangle([cx - w - 22, rim_y - 20, cx + w + 22, rim_y + 18], radius=18, fill=ACCENT)
    d.rounded_rectangle([cx - 90, rim_y + w - 18, cx + 90, rim_y + w + 22], radius=16, fill=ACCENT2)

    # Steam: three wavy lines rising from the bowl
    for dx in (-110, 0, 110):
        x0 = cx + dx
        # Stamp dense dots along the curve: smoother than a polyline with joints
        for i in range(0, 401):
            t = i / 400
            y = rim_y - 60 - t * 190
            x = x0 + 26 * math.sin(t * 2 * math.pi)
            d.ellipse([x - 17, y - 17, x + 17, y + 17], fill=ACCENT)
    return img


def save(img: Image.Image, size: int, name: str, flatten: bool = False) -> None:
    out = img.resize((size, size), Image.LANCZOS)
    if flatten:
        bg = Image.new('RGB', out.size, BG)
        bg.paste(out, mask=out.split()[3])
        out = bg
    out.save(OUT / name, optimize=True)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rounded, square = draw(True), draw(False)
    save(rounded, 192, 'icon-192.png')
    save(rounded, 512, 'icon-512.png')
    save(square, 512, 'icon-maskable-512.png')
    save(square, 180, 'apple-touch-icon.png', flatten=True)  # iOS rounds corners itself
    save(rounded, 32, 'favicon-32.png')
    print('icons written to', OUT)


if __name__ == '__main__':
    main()
