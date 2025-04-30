"""Models representing images."""

from fractions import Fraction
from pathlib import Path
from typing import List, Tuple

from walliq.assertions import (
    assert_is_hexadecimal_color_str,
    assert_is_path_or_str,
    assert_is_positive_nonzero_int,
)
from walliq.loaders import (
    load_pil_image_from_file_path,
    read_image_colors_from_file_path,
)


class Image:
    """An Image.

    Attributes:
        width (int):
            Resolution width.
        height (int):
            Resolution height.
        aspect_ratio (Fraction):
            Aspect ratio.
        aspect_ratio_is_exact (bool):
            Indicates whether the aspect ratio of the image is pixel-perfect,
            or whether it's slightly off, and the aspect ratio is the closest
            estimate to common wallpaper aspect ratios.
        colors (List[str]):
            A list containing the 6 most dominant colors of the image as RGB
            hexadecimal color strings (e.g. '#12DB42').
        VALID_ASPECT_RATIOS (List[Fraction]):
            List of recognized aspect ratios.
    """

    # Sort with:
    # for f in sorted(Image.VALID_ASPECT_RATIOS):
    #     print(f"Fraction({f.numerator}, {f.denominator}),\t# {format(f, '.4g')}")
    VALID_ASPECT_RATIOS = [
        # Portrait
        Fraction(9, 22),    # 0.4091
        Fraction(3, 7),     # 0.4286
        Fraction(9, 20),    # 0.45
        Fraction(6, 13),    # 0.4615
        Fraction(9, 19),    # 0.4737
        Fraction(1, 2),     # 0.5
        Fraction(9, 16),    # 0.5625
        Fraction(5, 8),     # 0.625
        # Square
        Fraction(1, 1),     # 1
        # Landscape
        Fraction(5, 4),     # 1.25
        Fraction(4, 3),     # 1.333
        Fraction(3, 2),     # 1.5
        Fraction(8, 5),     # 1.6
        Fraction(5, 3),     # 1.667
        Fraction(16, 9),    # 1.778
        Fraction(7, 3),     # 2.333
        Fraction(32, 9),    # 3.556
        Fraction(16, 3),    # 5.333
    ]

    @staticmethod
    def _identify_aspect_ratio(width: int, height: int) -> Tuple[Fraction, bool]:
        actual_aspect_ratio = Fraction(width, height)
        if actual_aspect_ratio in Image.VALID_ASPECT_RATIOS:
            return (actual_aspect_ratio, True)

        closest_aspect_ratio: Fraction = Fraction(1, 1)
        closest_delta = abs(actual_aspect_ratio - closest_aspect_ratio)
        for current_aspect_ratio in Image.VALID_ASPECT_RATIOS:
            new_delta = abs(actual_aspect_ratio - current_aspect_ratio)
            if new_delta < closest_delta:
                closest_delta = new_delta
                closest_aspect_ratio = current_aspect_ratio
        return (closest_aspect_ratio, False)

    def __init__(self, width: int, height: int, colors: List[str]):
        """Initializes an Image.

        Args:
            width (int): Resolution width.
            height (int): Resolution height.
            colors (List[str]): List of colors.
        """
        for attr, attr_name in [(width, "width"), (height, "height")]:
            try:
                assert_is_positive_nonzero_int(attr)
            except (TypeError, ValueError) as e:
                raise type(e)(f"Invalid {attr_name}: {e}") from e
        for color in colors:
            assert_is_hexadecimal_color_str(color)

        self.width: int = width
        self.height: int = height
        self.aspect_ratio, self.aspect_ratio_is_exact = Image._identify_aspect_ratio(width, height)
        self.colors = colors

    @classmethod
    def from_file(cls, path: Path | str) -> "Image":
        """Loads and initializes an Image from a file path.

        Args:
            pil_image (PilImage): The PIL Image to load.

        Returns:
            Image: An initialized Image.

        Raises:
            FileNotFoundError: If the file at the specified path does not exist.
        """
        assert_is_path_or_str(path)
        path = Path(path).expanduser().resolve()
        if not path.is_file():
            raise FileNotFoundError(f"Cannot load image (no such file): {path}")

        pil_image = load_pil_image_from_file_path(path)
        width, height = pil_image.size
        colors = read_image_colors_from_file_path(path)

        return cls(width=width, height=height, colors=colors)

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}("
            f"width={self.width!r}, "
            f"height={self.height!r}, "
            f"aspect_ratio={self.aspect_ratio!r}, "
            f"aspect_ratio_is_exact={self.aspect_ratio_is_exact!r}, "
            f"colors={self.colors!r}"
            f")"
        )
