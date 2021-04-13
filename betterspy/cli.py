import sys
import tarfile
import tempfile
from pathlib import Path

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


def _read_matrix(filename):
    return {".mtx": scipy.io.mmread, ".mm": scipy.io.mmread, ".rb": scipy.io.hb_read}[
        filename.suffix
    ](filename)


def main(argv=None):
    # Parse command line arguments.
    parser = _get_parser()
    args = parser.parse_args(argv)

    infile = args.infile
    if infile.suffixes == [".tar", ".gz"]:
        with tarfile.open(infile, "r:gz") as tar:
            A = None
            for m in tar.getmembers():
                if Path(m.name).suffix in [".mtx", ".rb"]:
                    with tempfile.TemporaryDirectory() as tmpdir:
                        tar.extract(m, path=tmpdir)
                        filename = Path(tmpdir) / Path(m.name)
                        A = _read_matrix(filename)
                    break
            assert A is not None, f"Couldn't find matrix file in {infile}."
    else:
        A = _read_matrix(infile)

    if args.outfile is None:
        show(A)
    else:
        write_png(args.outfile, A, args.border_width, args.border_color, args.colormap)


def _get_parser():
    import argparse

    parser = argparse.ArgumentParser(
        description=("Show sparsity structure of matrix"),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument("infile", type=Path, help="input matrix market file")

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
