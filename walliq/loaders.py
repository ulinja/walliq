"""Utilities for loading image data from various sources."""

from pathlib import Path
from typing import List

from PIL import Image as PilImage
import pywal

from walliq.assertions import assert_is_path_or_str


def load_pil_image_from_file_path(path: Path | str) -> PilImage:
    """Initialized a PIL Image from the specified file path.

    Args:
        path (Path): Path to the image file to load.

    Returns:
        PilImage: A PIL Image.
    """
    assert_is_path_or_str(path)
    path = Path(path).expanduser().resolve()
    if not path.is_file():
        raise FileNotFoundError(f"Cannot load image (no such file): {path}")
    return PilImage.open(path)


def read_image_colors_from_file_path(path: Path | str) -> List[str]:
    """Loads a list of Image colors from a file (using pywal).

    Args:
        path (Path): Path to the image file to load.

    Returns:
        List[str]: A list of RGB hex strings of the image's main colors.
    """
    COLOR_COUNT = 6

    assert_is_path_or_str(path)
    path = Path(path).expanduser().resolve()
    if not path.is_file():
        raise FileNotFoundError(f"Cannot load image (no such file): {path}")
    scan_result = pywal.colors.get(str(path))
    colors: List[str] = []
    for i in range(COLOR_COUNT):
        colors.append(scan_result["colors"][f"color{i}"])
    return colors
