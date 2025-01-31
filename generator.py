import matplotlib
import numpy as np
from PIL import Image


def generate(w, h, max_iter, bounds):
    """
    Gera uma imagem do conjunto de Mandelbrot com os parâmetros fornecidos.

    Args:
        w (int): Largura da imagem.
        h (int): Altura da imagem.
        max_iter (int): Número máximo de iterações.
        bounds (tuple): Intervalos reais e imaginários (re_min, re_max, im_min, im_max).

    Returns:
        Image: Imagem gerada do conjunto de Mandelbrot.
    """
    re_min, re_max, im_min, im_max = bounds
    x = np.linspace(re_min, re_max, num=w).reshape((1, w))
    y = np.linspace(im_min, im_max, num=h).reshape((h, 1))
    c = x + 1j * y
    z = np.zeros((h, w), dtype=complex)
    mask = np.full((h, w), True, dtype=bool)
    n = np.zeros((h, w), dtype=int)

    for i in range(max_iter):
        z[mask] = z[mask] * z[mask] + c[mask]
        mask[np.abs(z) > 2] = False
        n[mask] = i

    hsv = np.dstack((n / max_iter, np.ones_like(n), np.where(mask, 0, 1)))
    rgb = matplotlib.colors.hsv_to_rgb(hsv)

    return Image.fromarray((rgb * 255).astype("uint8"))
