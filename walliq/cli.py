"""Utilities and entrypoints for walliq CLI usage."""

from argparse import ArgumentParser

from tabulate import tabulate

from walliq.models.image import Image


def _init_arg_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog="waliq",
        description="Identifies wallpaper image data from image files.",
    )
    parser.add_argument(
        'file',
        help="The file to analyze.",
        metavar="FILE",
    )
    return parser


def _tabulate_image_data(image: Image) -> str:
    data = [
        ["Resolution", f"{image.width}x{image.height}"],
        ["Aspect Ratio", f"{image.aspect_ratio.numerator}:{image.aspect_ratio.denominator}"],
        ["Aspect Ratio Is Exact", "Yes" if image.aspect_ratio_is_exact else "No"],
        ["Colors"] + [color for color in image.colors],
    ]
    return tabulate(
        data,
        tablefmt="simple",
    )


def main() -> None:
    """Main entrypoint for walliq CLI invocation."""
    args = _init_arg_parser().parse_args()
    image = Image.from_file(args.file)
    print(_tabulate_image_data(image))


if __name__ == "__main__":
    main()
