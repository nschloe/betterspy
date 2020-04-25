import sys

import scipy.io

from .__about__ import __version__
from .main import show, write_png


def _get_version_text():
    return "\n".join(
        [
            "betterspy {} [Python {}.{}.{}]".format(
                __version__,
                sys.version_info.major,
                sys.version_info.minor,
                sys.version_info.micro,
            ),
            "Copyright (c) 2018-2020 Nico Schlömer <nico.schloemer@gmail.com>",
        ]
    )


def main(argv=None):
    # Parse command line arguments.
    parser = _get_parser()
    args = parser.parse_args(argv)

    A = scipy.io.mmread(args.infile)
    if args.outfile is None:
        show(A)
    else:
        write_png(args.outfile, A, args.border_width, args.border_color, args.colormap)

    return


def _get_parser():
    import argparse

    parser = argparse.ArgumentParser(
        description=("Show sparsity structure of matrix"),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument("infile", type=str, help="input matrix market file")

    parser.add_argument(
        "outfile", type=str, nargs="?", default=None, help="output png file (optional)"
    )

    parser.add_argument(
        "--border-width",
        "-w",
        required=False,
        type=int,
        default=0,
        help="border width (default: 0)",
    )

    parser.add_argument(
        "--border-color",
        "-b",
        required=False,
        type=str,
        default="0.5",
        help="border color (default: 0.5, gray)",
    )

    parser.add_argument(
        "--colormap",
        "-c",
        required=False,
        type=str,
        default=None,
        help="border color (default: 0.5, gray)",
    )

    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version=_get_version_text(),
        help="display version information",
    )
    return parser
