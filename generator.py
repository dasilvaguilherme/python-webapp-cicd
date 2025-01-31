"""
Módulo para gerar imagens do conjunto de Mandelbrot.
"""

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
    c = np.meshgrid(np.linspace(re_min, re_max, w), np.linspace(im_min, im_max, h))
    c = c[0] + 1j * c[1]  # Combinar para criar números complexos
    z = np.zeros_like(c, dtype=complex)
    mask = np.full_like(c, True, dtype=bool)
    n = np.full_like(c, 0, dtype=int)

    for i in range(max_iter):
        z[mask] = z[mask] * z[mask] + c[mask]
        mask &= np.abs(z) <= 2
        n[mask] = i

    hsv = np.dstack((n / max_iter, np.ones_like(n), ~mask))
    rgb = matplotlib.colors.hsv_to_rgb(hsv)

    return Image.fromarray((rgb * 255).astype("uint8"))
