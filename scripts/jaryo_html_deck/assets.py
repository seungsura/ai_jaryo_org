from __future__ import annotations

import base64
import html
from io import BytesIO
from pathlib import Path

try:
    from PIL import Image
except ImportError:  # pragma: no cover - fallback for lean environments
    Image = None

from .config import ICON_ROOT, TOOLCARD_ICON_ROOT

def processed_icon_data_uri(path: Path) -> str:
    if path.suffix == ".svg" or path.name != "opencode_icon.png" or Image is None:
        return asset_data_uri(path)

    source = Image.open(path).convert("RGBA")
    mask = Image.new("L", source.size)
    pixels = source.get_flattened_data() if hasattr(source, "get_flattened_data") else source.getdata()
    mask.putdata([
        255 if alpha and max(red, green, blue) < 226 else 0
        for red, green, blue, alpha in pixels
    ])
    bbox = mask.getbbox()
    if bbox is None:
        return asset_data_uri(path)

    cropped = source.crop(bbox)
    cropped.putalpha(mask.crop(bbox))
    width, height = cropped.size
    side = max(width, height)
    padding = max(24, side // 12)
    canvas = Image.new("RGBA", (side + padding * 2, side + padding * 2), (255, 255, 255, 0))
    canvas.alpha_composite(cropped, ((side - width) // 2 + padding, (side - height) // 2 + padding))
    canvas.thumbnail((160, 160), Image.Resampling.LANCZOS)

    payload = BytesIO()
    canvas.save(payload, format="PNG")
    return f"data:image/png;base64,{base64.b64encode(payload.getvalue()).decode('ascii')}"

def asset_data_uri(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".svg":
        mime = "image/svg+xml"
    elif suffix in {".jpg", ".jpeg"}:
        mime = "image/jpeg"
    else:
        mime = "image/png"
    payload = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{payload}"

def render_asset_figure(path: Path, class_name: str, alt: str | None = None) -> str:
    return (
        f'<figure class="{html.escape(class_name)}" data-asset-name="{html.escape(path.name)}">'
        f'<img src="{asset_data_uri(path)}" alt="{html.escape(alt or path.name)}">'
        "</figure>"
    )

def render_document_icon(icon_key: str, tool_name: str) -> str:
    icon_paths = {
        "claude": ICON_ROOT / "claude_code_icon.svg",
        "cursor": TOOLCARD_ICON_ROOT / "cursor-icon.svg",
        "copilot": TOOLCARD_ICON_ROOT / "github-copilot-octicon.svg",
        "codex": ICON_ROOT / "codex_icon.png",
    }
    path = icon_paths.get(icon_key)
    if path is None:
        raise ValueError(f"unknown document icon: {icon_key}")
    return (
        '<span class="doc-icon" aria-hidden="true">'
        f'<img src="{processed_icon_data_uri(path)}" alt="{html.escape(tool_name)} icon">'
        "</span>"
    )

def render_tool_icons() -> str:
    icons = [
        ("claude-code", ICON_ROOT / "claude_code_icon.svg"),
        ("codex", ICON_ROOT / "codex_icon.png"),
        ("opencode", ICON_ROOT / "opencode_icon.png"),
    ]
    items = "".join(
        f'<span class="tool-icon tool-icon-{html.escape(label)}">'
        f'<img src="{processed_icon_data_uri(path)}" alt="{html.escape(label)} icon">'
        "</span>"
        for label, path in icons
    )
    return (
        '<aside class="tool-icons" aria-label="toolchain">'
        f"{items}"
        "</aside>"
    )
