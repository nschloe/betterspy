"""
Better spy() function for Scipy sparse matrices.
"""
import tempfile

import matplotlib.colors as colors
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy
import png  # purepng


def plot(A, border_width=0, border_color="0.5", colormap=None):
    with tempfile.NamedTemporaryFile() as fp:
        write_png(
            fp.name,
            A,
            border_width=border_width,
            border_color=border_color,
            colormap=colormap,
        )
        img = mpimg.imread(fp.name)
        plt.imshow(img, origin="upper", interpolation="nearest")


def show(*args, **kwargs):
    plot(*args, **kwargs)
    plt.show()


class RowIterator:
    def __init__(self, A, border_width, border_color, colormap):
        self.A = A.tocsr()
        self.border_width = border_width

        rgb = numpy.array(colors.to_rgb(border_color))
        border_color_is_bw = numpy.all(rgb[0] == rgb) and rgb[0] in [0, 1]
        border_color_is_gray = numpy.all(rgb[0] == rgb)

        if colormap is None and (border_width == 0 or border_color_is_bw):
            self.mode = "binary"
            self.border_color = False
            self.bitdepth = 1
            self.dtype = bool

        elif colormap is None and border_color_is_gray:
            self.mode = "grayscale"
            self.bitdepth = 8
            self.dtype = numpy.uint8
            self.border_color = numpy.uint8(numpy.round(rgb[0] * 255))

        else:
            self.mode = "rgb"
            self.border_color = numpy.round(rgb * 255).astype(numpy.uint8)
            self.dtype = numpy.uint8
            self.bitdepth = 8

        if colormap is None:
            if self.mode == "binary":

                def convert_values(idx, vals):
                    out = numpy.ones(self.A.shape[1], dtype=self.dtype)
                    out[idx] = False
                    return out

            elif self.mode == "grayscale":

                def convert_values(idx, vals):
                    out = numpy.full(self.A.shape[1], 255, dtype=self.dtype)
                    out[idx] = 0
                    return out

            else:
                assert self.mode == "rgb"

                def convert_values(idx, vals):
                    out = numpy.full((self.A.shape[1], 3), 255, dtype=self.dtype)
                    out[idx, :] = 0
                    return out.flatten()

        else:
            assert self.mode == "rgb"
            # Convert the string into a colormap object with `to_rgba()`,
            # <https://stackoverflow.com/a/15140118/353337>.
            import matplotlib.cm as cmx

            cm = plt.get_cmap(colormap)
            c_norm = colors.Normalize(
                vmin=min(0.0, self.A.data.min()), vmax=max(0.0, self.A.data.max())
            )
            scalar_map = cmx.ScalarMappable(norm=c_norm, cmap=cm)

            def convert_values(idx, vals):
                x = numpy.zeros(self.A.shape[1])
                x[idx] = vals
                out = scalar_map.to_rgba(x)[:, :3] * 255
                out = numpy.round(out).astype(self.dtype)
                return out.flatten()

        self.convert_values = convert_values
        self.current = 0
        return

    def __iter__(self):
        return self

    def __next__(self):
        m = self.A.shape[0]
        b = self.border_width

        if self.current >= m + 2 * b:
            raise StopIteration

        if b == 0:
            row = self.A[self.current]
            out = self.convert_values(row.indices, row.data)
        else:
            if self.current < b or self.current > m + b - 1:
                out = numpy.tile(self.border_color, self.A.shape[1] + 2 * b).astype(
                    self.dtype
                )
            else:
                row = self.A[self.current - b]
                border = numpy.tile(self.border_color, b)
                out = numpy.concatenate(
                    [border, self.convert_values(row.indices, row.data), border]
                )

        self.current += 1
        return out


def write_png(filename, A, border_width=0, border_color="0.5", colormap=None):
    iterator = RowIterator(A, border_width, border_color, colormap)

    m, n = A.shape
    w = png.Writer(
        n + 2 * border_width,
        m + 2 * border_width,
        greyscale=iterator.mode != "rgb",
        bitdepth=iterator.bitdepth,
    )

    with open(filename, "wb") as f:
        w.write(f, iterator)
